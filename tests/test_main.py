import pytest
from fastapi.testclient import TestClient
from main import app  # Assuming main.py is where your FastAPI app is instantiated

# Create a TestClient instance using FastAPI's app
client = TestClient(app)

def test_get_employee_hires_by_department_and_quarter():
    # Send a GET request to your endpoint
    response = client.get("/metrics/employee_hires_by_department_and_quarter")
    
    # Check if the status code is 200 (OK)
    assert response.status_code == 200
    
    # Print raw content for debugging
    print("Response content:", response.text)
    
    # Check if the response JSON has the expected structure
    data = response.json()
    
    # Assuming the response is a list of dictionaries
    assert isinstance(data, list)
    
    # Example: Ensure the response contains a department and job
    if len(data) > 0:
        assert "department" in data[0]
        assert "job" in data[0]
        assert "Q1" in data[0]
        assert "Q2" in data[0]
        assert "Q3" in data[0]
        assert "Q4" in data[0]

def test_get_top_hiring_departments():
    # Send a GET request to another endpoint
    response = client.get("/metrics/top_hiring_departments")
    
    # Check if the status code is 200 (OK)
    assert response.status_code == 200
    
    # Check if the response JSON has the expected structure
    data = response.json()
    
    # Assuming the response is a list of dictionaries
    assert isinstance(data, list)
    
    # Example: Ensure the response contains a department and hired count
    if len(data) > 0:
        assert "department" in data[0]
        assert "hired" in data[0]

