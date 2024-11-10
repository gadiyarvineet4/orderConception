from pydantic import BaseModel
from decimal import Decimal

class PaymentInfo(BaseModel):
    status: str
    paymentType: str
    total: int
    itemTotal: int
    deliveryTotal: int
    tax: int