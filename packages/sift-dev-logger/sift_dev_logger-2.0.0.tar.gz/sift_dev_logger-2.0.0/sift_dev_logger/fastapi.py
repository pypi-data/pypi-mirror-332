try:
    from fastapi import FastAPI, Request
    from starlette.types import ASGIApp, Receive, Scope, Send, Message
    from starlette.datastructures import URL, Headers
    from fastapi.responses import StreamingResponse
except ImportError:
    raise ImportError(
        "FastAPI is not installed. Please install it with 'pip install sift-dev-logger[fastapi]'"
    )
import logging
import time
import uuid
from .handlers import SiftDevHandler
from .config import SiftDevConfig
from .common import get_current_config
from typing import Set, List, Dict, Any, Optional, Callable

def fastapi_logger(
    app: FastAPI,
    config: SiftDevConfig = None,
    max_body_size: int = 100_000,
    ignored_paths: Set[str] = set(),
    capture_request_body: bool = True,
    capture_response_body: bool = False,
    additional_handlers: List[logging.Handler] = [],
):
    """
    Configure FastAPI application logging with SiftDev handler.
    
    Args:
        app: FastAPI application instance
        config: SiftDevConfig for logging configuration
        max_body_size: Maximum size of request/response bodies to log
        ignored_paths: Set of paths to ignore for logging
        capture_request_body: Whether to capture request bodies (default True)
        capture_response_body: Whether to capture response bodies (default False).
            This controls whether response bodies are included in logs, but requests
            will be logged regardless of this setting.
        additional_handlers: Additional logging handlers to add
    """
    if config is None:
        config = get_current_config()
        
    logger = logging.getLogger("sift_dev.fastapi")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    
    sift_dev_handler = SiftDevHandler(config)
    logger.addHandler(sift_dev_handler)
    for handler in additional_handlers:
        if isinstance(handler, logging.Handler):
            logger.addHandler(handler)
        else:
            logger.warning(f"Handler {handler} is not a valid logging.Handler")

    def log_request(
        method: str, 
        path: str, 
        status_code: int, 
        duration_ms: float,
        request_headers: Dict[str, str],
        response_headers: Dict[str, str],
        request_body: str,
        response_body: str,
        client_addr: str,
        query_params: Dict[str, str],
        error: Optional[str]
    ):
        """Centralized logging function"""
        level = logging.ERROR if status_code >= 500 else logging.INFO
        message = f"{method} {path} {status_code} completed in {duration_ms:.2f}ms"
        
        extra = {
            "request_id": str(uuid.uuid4()),
            "client_addr": client_addr,
            "method": method,
            "path": path,
            "status_code": status_code,
            "duration_ms": duration_ms,
            "request_headers": request_headers,
            "response_headers": response_headers,
            "request_body": request_body,
            "response_body": response_body,
            "query_params": query_params,
            "error": error
        }
        
        logger.log(level, message, extra=extra)
        sift_dev_handler.flush()

    class LoggingMiddleware:
        def __init__(self, app: ASGIApp):
            self.app = app

        async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
            if scope["type"] != "http" or scope["path"] in ignored_paths:
                return await self.app(scope, receive, send)

            request_time = time.time()
            
            # Extract HTTP information from scope in a robust way
            path = scope.get("path", "")
            method = scope.get("method", "UNKNOWN")
            
            # Get client address
            client = scope.get("client", None)
            client_addr = client[0] if client else "unknown"
            
            # Extract headers
            headers_list = scope.get("headers", [])
            headers = {}
            for header_name, header_value in headers_list:
                try:
                    headers[header_name.decode('utf-8')] = header_value.decode('utf-8')
                except:
                    # If decoding fails, use the raw bytes
                    headers[str(header_name)] = str(header_value)
            
            # Detect if we're in a test environment
            is_test_client = False
            if 'user-agent' in headers and 'testclient' in headers['user-agent'].lower():
                is_test_client = True
            
            # Extract query parameters safely
            query_params = {}
            query_string = scope.get("query_string", b"").decode('utf-8', errors='replace')
            if query_string:
                for param in query_string.split('&'):
                    if not param:
                        continue
                    if '=' in param:
                        key, value = param.split('=', 1)
                        query_params[key] = value
                    else:
                        query_params[param] = ''
            
            response_status = None
            response_headers = None
            response_chunks: List[bytes] = []
            request_body = b""

            async def receive_with_body():
                nonlocal request_body
                if not capture_request_body:
                    return await receive()
                    
                try:
                    message = await receive()
                    if (
                        message["type"] == "http.request"
                        and len(request_body) < max_body_size
                    ):
                        request_body += message.get("body", b"")
                except Exception:
                    # If body capture fails, just pass through original message
                    pass
                return message

            async def send_with_capture(message: Message) -> None:
                nonlocal response_status, response_headers

                try:
                    if message["type"] == "http.response.start":
                        response_status = message["status"]
                        # Get response headers directly from raw headers
                        response_headers = {}
                        for header_name, header_value in message.get("headers", []):
                            try:
                                name = header_name.decode('utf-8')
                                value = header_value.decode('utf-8')
                                response_headers[name] = value
                            except:
                                # If decoding fails, use the raw bytes
                                response_headers[str(header_name)] = str(header_value)

                    elif message["type"] == "http.response.body":
                        # Only capture response body if enabled
                        if capture_response_body:
                            if len(b"".join(response_chunks)) < max_body_size:
                                response_chunks.append(message.get("body", b""))

                        # Log when the response is complete regardless of capture_response_body setting
                        if not message.get("more_body", False):
                            # Request is complete, log it
                            duration_ms = (time.time() - request_time) * 1000
                            
                            # Process request body
                            request_body_str = "[Request body capture disabled]"
                            if capture_request_body:
                                try:
                                    if len(request_body) > max_body_size:
                                        req_body = request_body[:max_body_size] + b"... (truncated)"
                                    else:
                                        req_body = request_body
                                    request_body_str = req_body.decode('utf-8', errors='replace')
                                except Exception as e:
                                    request_body_str = "[Could not decode request body]"
                            
                            # Process response body
                            response_body_str = "[Response body capture disabled]"
                            if capture_response_body:
                                try:
                                    response_body_bytes = b"".join(response_chunks)
                                    if len(response_body_bytes) > max_body_size:
                                        response_body_bytes = response_body_bytes[:max_body_size] + b"... (truncated)"
                                    response_body_str = response_body_bytes.decode('utf-8', errors='replace')
                                except Exception as e:
                                    response_body_str = f"[Could not decode response body: {e}]"
                            
                            # Get response headers as a dictionary
                            response_headers_dict = response_headers if response_headers else {}
                            
                            # Log the request
                            log_request(
                                method=method,
                                path=path,
                                status_code=response_status or 500,
                                duration_ms=duration_ms,
                                request_headers=headers,  # Already a dict
                                response_headers=response_headers_dict,
                                request_body=request_body_str,
                                response_body=response_body_str,
                                client_addr=client_addr,
                                query_params=query_params,
                                error=None
                            )
                except Exception as e:
                    # If logging fails, we don't interrupt the response
                    logger.warning(f"Failed to log request: {e}")

                await send(message)

            try:
                await self.app(scope, receive_with_body, send_with_capture)
            except Exception as e:
                # If there's an unhandled exception, try to log it
                duration_ms = (time.time() - request_time) * 1000
                
                # Process request body for error log
                request_body_str = "[Request body unavailable]"
                if capture_request_body and request_body:
                    try:
                        if len(request_body) > max_body_size:
                            req_body = request_body[:max_body_size] + b"... (truncated)"
                        else:
                            req_body = request_body
                        request_body_str = req_body.decode('utf-8', errors='replace')
                    except:
                        pass
                
                # Log the error
                try:
                    log_request(
                        method=method,
                        path=path,
                        status_code=500,
                        duration_ms=duration_ms,
                        request_headers=headers,  # Already a dict
                        response_headers={},
                        request_body=request_body_str,
                        response_body="[Error occurred before response was generated]",
                        client_addr=client_addr,
                        query_params=query_params,
                        error=str(e)
                    )
                except Exception as log_err:
                    logger.error(f"Failed to log error: {log_err}")
                
                # Re-raise the original exception
                raise

    # Apply our ASGI middleware to the app
    app.add_middleware(LoggingMiddleware)
    
    return app

# For backwards compatibility
instrument_logging_middleware = fastapi_logger
