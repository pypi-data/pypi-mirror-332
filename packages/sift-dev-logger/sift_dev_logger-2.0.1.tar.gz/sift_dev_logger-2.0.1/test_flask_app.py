from flask import Flask
from sift_dev_logger import SiftDevConfig, configure, flask_logger, SiftDevHandler
from dotenv import load_dotenv
import logging

load_dotenv()

config = SiftDevConfig(
    sift_dev_ingest_key="test-key",
    service_name="test-flask"
)

configure(config)  # This stores the config globally

app = Flask(__name__)

# Create and configure loggers
logger = logging.getLogger("test")
logger.addHandler(SiftDevHandler())
logger.setLevel(logging.INFO)

flask_logger(app)  # Uses config from configure()

@app.route('/')
def hello():
    logger.info("Received request")
    return 'Hello World!'

@app.route('/error')
def error():
    logger.error("This is an error log")
    # Raise an exception to simulate an error
    raise Exception("Test error")

if __name__ == '__main__':
    app.run(debug=True, port=6000) 