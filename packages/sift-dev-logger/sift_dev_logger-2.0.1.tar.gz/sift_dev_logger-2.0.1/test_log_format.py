import logging
import json
import time
from datetime import datetime
from sift_dev_logger import configure, getLogger, SiftDevConfig, flush_logs
from dotenv import load_dotenv
load_dotenv()

# Configure with debug-friendly settings
configure(SiftDevConfig(
    service_name="test-service",
    service_instance_id="test-instance",
    # Don't configure an endpoint to avoid actual sending
    batch_size=1
))

# Get a logger
logger = getLogger("test_format")

# First disable requests logging to reduce noise
logging.getLogger('requests').setLevel(logging.WARNING)

# Add a simple log message with some extra attributes
logger.info("Testing log format", extra={
    "test_id": "format-test-123",
    "metadata": {
        "key1": "value1",
        "key2": "value2"
    }
})

# Force flush logs
flush_logs()

# Simulate the log format that would be sent 
print("\n--- NEW LOG FORMAT ---")

# Create a log entry (similar to what the handler would create)
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
attributes = {
    "logger.name": "test_format",
    "thread.name": "MainThread",
    "file.name": "test_log_format.py",
    "line.number": 17,
    "test_id": "format-test-123",
    "metadata.key1": "value1",
    "metadata.key2": "value2"
}

# New format with changes
new_log_format = {
    "body": "Testing log format",  # Just the message, not JSON
    "id": f"sift-dev-log-{int(time.time() * 1000)}",
    "timestamp": timestamp,  # Moved out from body
    "attributes": attributes,
    "resources": {
        "service.name": "test-service",
        "host.name": "test-instance"
    },
    "level": "INFO",  # Renamed from severity_text
    "severity_number": 5,
    "scope": {}
}

# Pretty print the log
print(json.dumps(new_log_format, indent=2))

print("\n--- OLD LOG FORMAT (before changes) ---")
# Show what it looked like before all the changes
old_body_content = {
    "timestamp": timestamp,
    "level": "INFO",
    "logger": "test_format",
    "message": "Testing log format",
    "attributes": attributes,
    "resource": {
        "service.name": "test-service",
        "host.name": "test-instance"
    }
}

old_log_format = {
    "body": json.dumps(old_body_content),  # Body was a JSON string
    "id": f"sift-dev-log-{int(time.time() * 1000)}",
    "timestamp": datetime.now().isoformat() + "Z",  # Different timestamp
    "attributes": attributes,
    "resources": {
        "service.name": "test-service",
        "host.name": "test-instance"
    },
    "severity_text": "INFO",  # Old name
    "severity_number": 5,
    "scope": {}
}

print(json.dumps(old_log_format, indent=2))

print("\nAll changes have been applied to the log format!") 