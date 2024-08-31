from fastapi import FastAPI # type: ignore
from json_db import JsonDB
from product import Product

app = FastAPI()

productDB = JsonDB(path="./data/products.json")

@app.get("/products")
def get_Products():
    products = productDB.read_json()
    return {"products": products}


@app.post("/products")
def create_Products(product: Product):
    productDB.insert(product)

    return {"status": "ok"}
