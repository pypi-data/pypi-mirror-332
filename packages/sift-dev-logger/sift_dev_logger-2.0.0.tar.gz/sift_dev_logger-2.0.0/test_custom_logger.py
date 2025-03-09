import time
from sift_dev_logger import configure, getLogger, SiftDevConfig, flush_logs, get_current_config
from dotenv import load_dotenv

load_dotenv()

# Configure the logger with a smaller batch size and delay
configure(SiftDevConfig(
    service_name="test-service",
    service_instance_id="test-instance",
    batch_size=2,  # Send after 2 logs
    batch_delay_millis=2000,  # Or after 2 seconds
    # Set endpoint if you have a custom endpoint
    # endpoint="https://your-log-endpoint.com/logs",
    # api_key="your-api-key"
))

print("Config:", get_current_config().__dict__)

# Get a logger instance
logger = getLogger("test_logger")

print("\n--- Basic logging ---")
# Log some messages
logger.info("This is an info message")
logger.warning("This is a warning message")
# These two logs should trigger batch sending due to batch_size=2

print("\n--- Structured logging ---")
# Log with extra attributes
logger.error("This is an error message")
logger.info("Message with extra attributes", extra={
    "user_id": "12345",
    "request_id": "req-abc-123",
    "custom_data": {
        "key1": "value1",
        "key2": "value2"
    }
})
# These two logs should trigger another batch sending

print("\n--- Wait for timer-based batch ---")
# Only add one log, so it should be sent by the timer
logger.warning("This log should be sent by the timer")
print("Waiting for batch timer (2 seconds)...")
time.sleep(3)  # Wait for batch timer (2 seconds + buffer)

print("\n--- Logging with additional context ---")
# Get a logger with attached context
context_logger = getLogger("context_logger", extra={
    "session_id": "session-abc-123",
    "environment": "testing"
})

# All logs from this logger will have the context attached
context_logger.info("Log with attached context")
context_logger.warning("Another log with the same context")

# Force flush logs before exit
print("\n--- Forcing log flush ---")
flush_logs()
print("Done!") 