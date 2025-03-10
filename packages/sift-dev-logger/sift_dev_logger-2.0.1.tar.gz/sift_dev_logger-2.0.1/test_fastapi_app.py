from fastapi import FastAPI, HTTPException
import uvicorn
from sift_dev_logger import SiftDevConfig, configure, fastapi_logger, SiftDevHandler
from dotenv import load_dotenv
import logging 

app = FastAPI()
load_dotenv()

logger = logging.getLogger("test")
logger.setLevel(logging.INFO)
logger.addHandler(SiftDevHandler())

config = SiftDevConfig(
    sift_dev_ingest_key="test-key",
    service_name="test-fastapi",
)
configure(config)
fastapi_logger(app)

@app.get("/")
async def root():
    logger.info("Received request from fastapi")
    return {"message": "Hello World"}

@app.get("/error")
async def error_route():
    logger.error("This is an error log")
    raise HTTPException(status_code=500, detail="This is a test error")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 