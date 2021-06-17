from pydantic import BaseModel


class Order(BaseModel):
    __collection_name__ = "Order"

    id: int
    stock: str
    quantity: int
    price: float
