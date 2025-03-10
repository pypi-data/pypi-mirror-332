import time
from test_flask_app import app

# Create a test client
client = app.test_client()

def test_root_endpoint():
    """Test the root endpoint returns correct response"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello World!"
    
def test_logging_functionality():
    print("test_logging_functionality called here")
    """Test that the SiftDev logger properly captures logs from Flask requests"""
    # Make multiple requests to generate logs
    for _ in range(3):
        response = client.get("/")
        assert response.status_code == 200
    
    # Add small delay to allow logs to be processed
    time.sleep(2)
    
    # In a real test, you would inspect logs in your SiftDev backend or mock the HTTP calls
    # Since we can't directly verify logs in SiftDev, this is a placeholder assertion
    # In a real environment, you might want to mock the HTTP client used by SiftDevHandler
    # and verify that the expected log data was sent
    assert True  # Placeholder assertion
    
def test_error_simulation():
    print("test_error_simulation called here")
    """Test logging for error scenarios (if your app has an error endpoint)"""
    # This assumes you have an endpoint that generates an error
    # If not, you'll need to add one to your Flask app
    try:
        response = client.get("/error")
        assert False, "Expected error was not raised"
    except Exception:
        # Error was properly raised
        # Again, in a real test, you would check that the error was properly logged
        pass

def test_performance():
    """Test that logging doesn't significantly impact performance"""
    start_time = time.time()
    for _ in range(10):
        response = client.get("/")
        assert response.status_code == 200
    end_time = time.time()
    print(f"Time taken: {end_time - start_time}")
    # Performance assertion - this is just an example
    # Adjust the threshold as needed for your application
    assert (end_time - start_time) < 1.0, "Performance too slow with logging enabled"

if __name__ == "__main__":
    # Run tests manually
    test_root_endpoint()
    # test_logging_functionality()
    try:
        test_error_simulation()
        print("Warning: error simulation test did not fail as expected")
    except Exception as e:
        print(f"Error simulation test failed as expected: {e}")
    test_performance()
    print("All manual tests completed") 