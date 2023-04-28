import requests
import json
import pytest

url = 'https://automationexercise.com/api/productsList'

def test_products_list():
    response = requests.get(url)

    # Validate status code
    assert response.status_code == 200, "API is not returning a 200 status code"
    assert response.reason == "OK", "API is not returning a OK status line"

    # Validate content
    assert response.content
    response_json = response.json()
    assert "products" in response_json.keys()

    # Validate the length
    length = response.json()
    assert len(length) == 2
    assert len(response_json["products"]) >= 1

    # Validate the list returned by the API
    products = response.json()['products']
    print(products)
