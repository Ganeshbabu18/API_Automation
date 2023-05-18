import requests
import pytest

url = 'https://automationexercise.com/api/brandsList'

def put_all_brand():
    updated_data = {
        'brandName': 'India cement',
        'brandStatus': 'Active'
    }
    response = requests.put(url, json=updated_data)

    # assert the status code is 200 or 204
    assert response.status_code in [200, 204]

    # assert the response data is the same as the updated data
    assert response.json() == updated_data