import requests
import json
import pytest

# Define the API endpoint URL
url = 'https://automationexercise.com/api/productsList'

def test_products_list():
    response = requests.get(url)

    # Validate status code
    code = response.status_code
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
    print("The status code is ", response.status_code)

    # Validate content
    assert response.content
    response_json = response.json()
    assert "products" in response_json.keys()
    assert len(response_json["products"]) >= 1

    # Validate the length
    length = response.json()
    assert len(length) == 2

    # Validate the list returned by the API
    products = response.json()['products']
    print(products)
