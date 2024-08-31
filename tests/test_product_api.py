import requests
import json

def test_should_get_list_of_products():
    response = requests.get("https://humble-space-winner-pww66x9vvgjf6j5r-8000.app.github.dev/products")

    print(response)

test_should_get_list_of_products()