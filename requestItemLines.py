from dataclasses import dataclass

@dataclass
class ItemLines(object):
    itemType: str
    itemId: int
    itemName: str
    quantity: int
    price: float
    sku: str
    description: str
    ship_node: str