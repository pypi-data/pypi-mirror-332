# SIFT dev-logger (v2.0)

A lightweight Python logging SDK that provides structured logging for Flask and FastAPI applications. This new version uses a custom implementation without OpenTelemetry dependencies.

---

## Installation

### Using `pip`

```bash
pip install sift-dev-logger
```

**With optional Flask support:**

```bash
pip install "sift-dev-logger[flask]"
```

**With optional FastAPI support:**

```bash
pip install "sift-dev-logger[fastapi]"
```

**With all optional dependencies:**

```bash
pip install "sift-dev-logger[all]"
```

## Features

- Simple structured logging without dependencies on OpenTelemetry
- Batching of logs for better performance
- Customizable configuration through environment variables or code
- Support for Flask and FastAPI web frameworks
- Ability to send logs to a custom endpoint or fallback to console output

## Configuration

Configure the logger via environment variables:

```bash
# Required for sending logs to a custom endpoint
export SIFT_DEV_ENDPOINT="https://your-log-endpoint.com/logs"
export SIFT_DEV_API_KEY="your-api-key"

# Optional configuration
export SIFT_DEV_SERVICE_NAME="your-service-name"
export SIFT_DEV_SERVICE_INSTANCE_ID="your-instance-id"
export ENV="production"  # or development, staging, etc.
```

Or configure programmatically:

```python
from sift_dev_logger import configure, SiftDevConfig

# Configure once at application startup
configure(SiftDevConfig(
    service_name="my-service",
    service_instance_id="instance-1",
    endpoint="https://your-log-endpoint.com/logs",
    api_key="your-api-key",
    env="production",
    batch_size=10,  # Number of logs to batch before sending
    batch_delay_millis=5000  # Maximum time to wait before sending a batch
))
```

## Basic Usage

```python
from sift_dev_logger import getLogger

# Get a logger (automatically configured with SiftDevHandler)
logger = getLogger("my_module")

# Log messages with different severity levels
logger.info("This is an informational message")
logger.warning("This is a warning message")
logger.error("This is an error message")

# Log with additional context
logger.info("User logged in", extra={"user_id": "12345", "ip_address": "192.168.1.1"})

# Log with structured data
logger.info("API request completed", extra={
    "request_id": "req-abc-123",
    "duration_ms": 42,
    "status_code": 200,
    "user": {
        "id": "user-123",
        "role": "admin"
    }
})

# Make sure all logs are flushed before application exit
from sift_dev_logger import flush_logs
flush_logs()
```

---

## How to build and publish

1. **Install build tools**:

    ```bash
    pip install build
    ```

2. **Build the package**:

    ```bash
    python -m build
    ```

3. **Test the package locally**:

    ```bash
    pip install sift_dev_logger-0.1.0.tar.gz
    ```

4. **Upload to PyPI** (you'll need to create an account first):

    ```bash
    python -m twine upload dist/*
    ```

---

## Key Features

1. **Optional Dependencies**: Users can install just what they need (core, Flask, or FastAPI support).  
2. **Modern Build System**: Uses `hatchling` for a clean, modern build.  
3. **Clear Documentation**: README shows installation and basic usage.  
4. **Version Management**: Easy to update version in one place.  
5. **Development Tooling**: Development dependencies separated from runtime requirements.

---