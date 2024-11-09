from pydantic import BaseModel

class Charges(BaseModel):
    total: int
    itemTotal: int
    deliveryTotal: int
    tax: int