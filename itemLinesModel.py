from pydantic import BaseModel

class ItemLines(BaseModel):
    itemType: str
    itemId: int
    itemName: str
    quantity: int
    price: float
    sku: str
    description: str
    ship_node: str