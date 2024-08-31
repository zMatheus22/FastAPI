from product import Product
import json

def read_json():
    file = open("./data/products.json")
    data = json.loads(file.read())
    file.close()

    return data["products"]
