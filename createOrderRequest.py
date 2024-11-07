from dataclasses import dataclass
from requestAddress import Address
from requestCharges import Charges
from requestPaymentInfo import PaymentInfo
from requestItemLines import ItemLines
from requestWorkOrder import WorkOrder

@dataclass
class CreateOrderRequest(object):

    orderNumber: int
    countryCode: str
    seller: str
    orderType: str
    orderDate: str
    shipToAddress: Address
    billToAddress: Address
    charges: Charges
    paymentInfo: PaymentInfo
    itemLines: ItemLines
    workOrder: WorkOrder