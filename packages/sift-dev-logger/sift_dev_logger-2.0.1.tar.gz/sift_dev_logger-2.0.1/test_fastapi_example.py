from fastapi import FastAPI, Depends, HTTPException, Request
import uvicorn
import logging
from sift_dev_logger import configure, SiftDevConfig, fastapi_logger, getLogger

# Create FastAPI app
app = FastAPI()

# Configure SiftDev logger
configure(SiftDevConfig(
    service_name="fastapi-example",
    service_instance_id="dev-instance", 
    # Set endpoint if you have a custom endpoint
    # endpoint="https://your-log-endpoint.com/logs",
    # api_key="your-api-key"
))

# Apply the FastAPI logging middleware
fastapi_logger(app)

# Get a custom logger
logger = getLogger("custom_routes")

# Define some routes
@app.get("/")
async def home():
    return {"message": "Hello from FastAPI!"}

@app.get("/error")
async def error():
    # This will trigger an error log
    raise HTTPException(status_code=500, detail="This is a test error")

@app.get("/custom-log")
async def custom_log(request: Request):
    # Log with the custom logger and add request info
    request_headers = dict(request.headers)
    
    logger.info("Custom log message", extra={
        "custom_field": "custom value",
        "request_headers": request_headers,
        "user_info": {
            "id": "12345",
            "role": "admin"
        }
    })
    return {"message": "Custom log sent"}

if __name__ == "__main__":
    # Run the app
    uvicorn.run(app, host="0.0.0.0", port=8000) 