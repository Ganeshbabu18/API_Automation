import requests

url = "https://automationexercise.com/api/productsList"

response = requests.get(url)

# Validate status code
code = response.status_code
assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
print("The status code is ", response.status_code)

# Validate response content
assert code == 200 ,"Code doesn't match "
print(response.json())
response_json = response.json()

# Validate the length
if len(response_json):
    print("Length is:", len(response_json))
else:
    print("Response data is empty")

# Validate the list returned by the API
products = response.json()['products']
print(products)
