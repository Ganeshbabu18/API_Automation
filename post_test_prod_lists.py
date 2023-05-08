import requests

def test_api_post():
    # set up the request data
    url = "https://automationexercise.com/api/productsList"
    headers = {'Content-Type': 'application/json'}
    data = {'id': '50', 'name': 'fashioned T shirt'}

    # POST request
    response = requests.post(url, headers=headers, json=data)

    # validate the response status
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    # validate the response message
    expected_message = "Success"
    actual_message = response.json().get('message')
    assert actual_message == expected_message, f"Expected message '{expected_message}', but got '{actual_message}'"
