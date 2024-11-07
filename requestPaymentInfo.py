from dataclasses import dataclass

@dataclass
class PaymentInfo(object):
    status: str
    paymentType: str