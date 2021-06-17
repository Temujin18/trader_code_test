from typing import List

from pydantic import BaseModel


class Order(BaseModel):
    __collection_name__ = "Order"

    user_id: int
    stock: str
    quantity: int
    price: float
