import requests
import json

base_url = "https://automationexercise.com/api/productsList"

Response = requests.get(base_url)
# print(Response)

#Validating the content and status code
code = Response.status_code
print("Status code is ", code)
assert code == 200 ,"Code doesn't match "
print(json.dumps(Response.json(), indent=4))
json_resp = Response.json()

#Return List
List = list(Response)
print(List)


#length
length = len(json.dumps(Response.json(), indent=4))
print("Current length is ", length)
assert length == 11073 ,"length does not match "
print("Validated length is ", length)

