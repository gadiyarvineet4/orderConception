from pydantic import BaseModel

class PaymentInfo(BaseModel):
    status: str
    paymentType: str