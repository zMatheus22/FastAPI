from product import Product
from pydantic import BaseModel # type: ignore
import json

class JsonDB(BaseModel):
    path: str

    def read_json(self):
        file = open(self.path)
        data = json.loads(file.read())
        file.close()

        return data

    def insert(self, product: Product):
        data = self.read_json()
        data["products"].append(product.dict())

        file = open(self.path, "w")
        file.write(json.dumps(data))
        file.close()
