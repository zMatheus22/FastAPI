from pydantic import BaseModel # type: ignore


class Release(BaseModel):
    date: str
    description: str
    price: float
    type: str
