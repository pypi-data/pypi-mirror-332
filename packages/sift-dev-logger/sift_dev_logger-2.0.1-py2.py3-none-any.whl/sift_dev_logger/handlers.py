import logging
import json
import time
from datetime import datetime
import threading
from typing import Dict, Any, Optional
import requests
from .config import SiftDevConfig, get_current_config
import os

# Enable requests debug logging
logging.getLogger('requests').setLevel(logging.DEBUG)

class SiftDevHandler(logging.Handler):
    """
    A handler that exports logs to SiftDev with a custom implementation (no OpenTelemetry).
    
    This handler is designed to work in complex scenarios including:
    1. Async web frameworks (FastAPI, ASGI)
    2. Multiple handler instances with different configurations
    3. Streaming responses and middleware contexts
    """
    
    # Class-level storage for batching and configurations
    _log_batches = {}
    _configs = {}
    _batch_timers = {}
    
    def __init__(self, config=None, formatter=None):
        super().__init__()
        self.config = config or get_current_config()
        if formatter:
            self.setFormatter(formatter)
        
        # Create config key
        config_key = (
            f"{self.config.service_name}:"
            f"{self.config.sift_dev_endpoint}:"
            f"{self.config.service_instance_id}"
        )
        
        # Store config
        self.__class__._configs[config_key] = self.config
        
        # Initialize batch for this config if it doesn't exist
        if config_key not in self.__class__._log_batches:
            self.__class__._log_batches[config_key] = []
            # Start a timer for this batch
            self._start_batch_timer(config_key)
            
        self._config_key = config_key
    
    def _start_batch_timer(self, config_key):
        """Start a timer to periodically send batched logs"""
        if config_key in self.__class__._batch_timers:
            # Cancel existing timer if there is one
            self.__class__._batch_timers[config_key].cancel()
            
        # Create a new timer
        timer = threading.Timer(2.0, self._timer_callback, args=[config_key])
        timer.daemon = True  # Ensure timer doesn't prevent app from exiting
        timer.start()
        self.__class__._batch_timers[config_key] = timer
        
    def _timer_callback(self, config_key):
        """Called when the batch timer expires"""
        try:
            # Send the batch
            self._send_batch(config_key)
            # Start a new timer
            self._start_batch_timer(config_key)
        except Exception as e:
            # Critical error in the timer, log it
            print(f"Error in batch timer: {str(e)}")



    async def emit_async(self, record):
        """Async version of emit"""
        if not hasattr(self, '_config_key'):
            return
            
        try:
            self._process_record(record)
        except Exception:
            self.handleError(record)

    def emit(self, record):
        """Handle log emission"""
        if not hasattr(self, '_config_key'):
            return
            
        try:
            self._process_record(record)
        except Exception:
            self.handleError(record)
    
    def _process_record(self, record):
        """Process the log record and add it to the batch"""
        # formatted_message = record.getMessage()
        formatted_message = self.format(record) if self.formatter else record.getMessage()
        # Get config key
        if not hasattr(self, '_config_key'):
            # This should never happen, but just in case
            return
            
        # Add to batch
        attributes = self._get_attributes(record)
        
        # Create log entry
        timestamp = datetime.fromtimestamp(record.created).astimezone().isoformat()
        
        log_entry = {
            "timestamp": timestamp,
            "level": record.levelname,
            "severity_number": self._get_severity_number(record.levelname),
            "message": formatted_message,
            "attributes": attributes,
            "resources": {
                "service.name": self.config.service_name,
                "host.name": self.config.service_instance_id
            }
        }
        
        # Add to batch
        self.__class__._log_batches[self._config_key].append(log_entry)
        
        # Check if we should send batch now (if it's full)
        if len(self.__class__._log_batches[self._config_key]) >= 10:
            self._send_batch(self._config_key)
            
        # If it's an ERROR or higher, send immediately
        if record.levelno >= logging.ERROR:
            self._send_batch(self._config_key)
    
    def _get_attributes(self, record):
        """Extract all attributes from the record"""
        attributes = {
            "logger.name": record.name,
            "thread.name": record.threadName,
            "file.name": record.filename,
            "line.number": record.lineno,
        }
        
        # Process all record attributes
        for key, value in record.__dict__.items():
            if (key not in {"args", "exc_info", "exc_text", "msg", "message", 
                           "stack_info", "created", "msecs", "relativeCreated", 
                           "levelno", "levelname", "pathname", "filename", 
                           "module", "lineno", "funcName", "processName", 
                           "process", "thread", "threadName", "name", "taskName"} and 
                not key.startswith("_")):
                # No longer flattening dictionaries, store them directly
                attributes[key] = value
        
        # Process extra attributes if present
        if hasattr(record, "extra"):
            for key, value in record.extra.items():
                # No longer flattening dictionaries, store them directly
                attributes[key] = value
        
        return attributes
    
    def _send_batch(self, config_key):
        """Send the batch of logs to the desired endpoint"""
        # Safety check for config existence
        if config_key not in self.__class__._configs:
            return
            
        config = self.__class__._configs[config_key]
        
        # Check for a valid endpoint
        if not config.sift_dev_endpoint:
            return
            
        # Safety check for batch existence
        if config_key not in self.__class__._log_batches:
            return
            
        # Check if batch has logs
        logs_to_send = self.__class__._log_batches[config_key]
        if not logs_to_send:
            # No logs to send
            return
            
        try:
            # Format logs in the desired structure
            formatted_logs = logs_to_send
            
            # Send logs to endpoint
            if config.sift_dev_endpoint:
                headers = {
                    "Content-Type": "application/json",
                    "Authorization": config.sift_dev_ingest_key or ""
                }
                
                try:
                    # Ensure proper URL format
                    endpoint = config.sift_dev_endpoint
                    if not endpoint.endswith("/"):
                        endpoint += "/"
                    
                    
                    # Convert to JSON string using a custom default function
                    payload = json.dumps(formatted_logs, default=lambda o: str(o))
                    response = requests.post(endpoint, data=payload, headers=headers)
                    # response = requests.post(endpoint, json=formatted_logs, headers=headers)
                    
                    if response.status_code >= 400:
                        print(f"SiftDev: Error sending logs: HTTP {response.status_code}")
                except Exception as e:
                    print(f"SiftDev: Exception during HTTP request: {str(e)}")
                
                # Clear the batch after sending, regardless of success or failure
                self.__class__._log_batches[config_key] = []
            else:
                # Clear the batch without printing to console
                self.__class__._log_batches[config_key] = []
                
        except Exception as e:
            print(f"SiftDev: Error in _send_batch: {str(e)}")
    
    def _get_severity_number(self, level_name):
        """Convert log level name to severity number"""
        severity_map = {
            "CRITICAL": 17,
            "ERROR": 13,
            "WARNING": 9,
            "INFO": 5,
            "DEBUG": 1,
            "NOTSET": 0
        }
        return severity_map.get(level_name, 0)
        
    def flush(self):
        """
        Flush any buffered log records for this handler's config
        """
        if hasattr(self, '_config_key') and self._config_key in self.__class__._log_batches:
            if self.__class__._log_batches[self._config_key]:
                self._send_batch(self._config_key)
            
    def close(self):
        """
        Clean up resources for this handler's config
        """
        self.flush()
        if hasattr(self, '_config_key'):
            config_key = self._config_key
            
            # Stop timer
            if config_key in self.__class__._batch_timers:
                self.__class__._batch_timers[config_key].cancel()
                del self.__class__._batch_timers[config_key]
                
            # Clean up batches
            if config_key in self.__class__._log_batches:
                del self.__class__._log_batches[config_key]
                
            # Clean up configs
            if config_key in self.__class__._configs:
                del self.__class__._configs[config_key]
                
        super().close()

    @classmethod
    def from_dict(cls, config: dict, **kwargs):
        """Factory method for dictConfig integration"""
        sift_config = SiftDevConfig(**config)
        return cls(config=sift_config, **kwargs) 