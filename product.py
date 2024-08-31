from pydantic import BaseModel # type: ignore

class Product(BaseModel):
    name: str
    price: float
