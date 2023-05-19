import requests
import json
import pytest

@pytest.fixture
def api_url():
    return "https://automationexercise.com/api/productsList"

def test_products_list(api_url):
    response = requests.get(api_url)

    # Test Case 1: List of Products returned by this API
    response_json = response.json()
    assert "products" in response_json.keys()
    products = response.json()['products']
    print(products)

def test_status_code(api_url):
    response = requests.get(api_url)

    # Test Case 2: Validate and assert Status code
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

def test_content(api_url):

    # Test Case 3: Validate and assert the content
    expected_content = "Adidas"
    response = requests.get(api_url)
    response_content = json.loads(response.content)
    assert response_content == expected_content
    assert 'Adidas' in response_content

def test_length(api_url):
    response = requests.get(api_url)

    # Test Case 4: Validate and assert length
    expected_length = 34  # Replace with expected length
    assert len(response.json()['products']) == expected_length, "Unexpected length of products list"
