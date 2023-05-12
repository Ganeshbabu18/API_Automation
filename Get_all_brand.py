import requests
import json
import pytest

url = 'https://automationexercise.com/api/brandsList'

def test_api_status():
    response = requests.get(url)
    assert response.status_code == 200

def test_api_content():
    expected_content = "Biba"
    response = requests.get(url)
    response_content = json.loads(response.content)
    assert response_content == expected_content
    assert "Biba" in response_content

def test_api_length():
    response = requests.get(url)
    data = response.json()
    assert len(data) > 0
