from flask import Flask, jsonify
from sift_dev_logger import configure, SiftDevConfig, flask_logger

# Create Flask app
app = Flask(__name__)

# Configure SiftDev logger
configure(SiftDevConfig(
    service_name="flask-example",
    service_instance_id="dev-instance",
    # Set endpoint if you have a custom endpoint
    # endpoint="https://your-log-endpoint.com/logs",
    # api_key="your-api-key"
))

# Apply the Flask logging middleware
flask_logger(app)

# Define some routes
@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/error')
def error():
    # This will trigger an error log
    raise ValueError("This is a test error")

@app.route('/custom-log')
def custom_log():
    # Get the app logger and add custom fields
    app.logger.info("Custom log message", extra={
        "custom_field": "custom value",
        "user_info": {
            "id": "12345",
            "role": "admin"
        }
    })
    return jsonify({"message": "Custom log sent"})

if __name__ == '__main__':
    # Run the app
    app.run(debug=True, port=5000) 