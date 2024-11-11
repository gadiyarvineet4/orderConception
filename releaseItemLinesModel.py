from pydantic import BaseModel

class ItemLines(BaseModel):
    itemType: str
    itemId: int
    itemName: str
    quantity: int
    itemLineNo: int
    description: str