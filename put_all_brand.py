import requests
import pytest

@pytest.fixture
def api_url():
    return "https://automationexercise.com/api/brandsList"

def test_content_with_status(api_url):
    # Test Case 1: Assert with Status
    response = requests.put(api_url)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_content = response.json()
    assert "brands" in response_content.keys(), "Response does not contain 'brands' key"
    brands = response_content["brands"]
    print(brands)

def test_content_with_response_message(api_url):
    # Test Case 2: Assert content with Response message
    response = requests.put(api_url)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_content = response.json()
    assert "message" in response_content.keys(), "Response does not contain 'message' key"
    response_message = response_content["message"]
    expected_message = "All brands list updated successfully"
    assert response_message == expected_message, f"Unexpected response message: {response_message}"
