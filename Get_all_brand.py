import requests
import pytest

API_URL = 'https://automationexercise.com/api/brandsList'


def test_api_status():
    response = requests.get(API_URL)
    assert response.status_code == 200


def test_api_content():
    response = requests.get(API_URL)
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json() != {}


def test_api_length():
    response = requests.get(API_URL)
    data = response.json()
    assert len(data) > 0
