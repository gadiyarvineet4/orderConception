from dataclasses import dataclass

@dataclass
class Charges(object):
    total: int
    itemTotal: int
    deliveryTotal: int
    tax: int