from addressModel import Address
from chargesModel import Charges
from paymentInfoModel import PaymentInfo
from itemLinesModel import ItemLines
from workOrderModel import WorkOrder
from pydantic import BaseModel
from typing import List


class CreateOrderRequest(BaseModel):

    orderNumber: int
    countryCode: str
    seller: str
    orderType: str
    orderDate: str
    shipToAddress: Address
    billToAddress: Address
    charges: Charges
    paymentInfo: PaymentInfo
    itemLines: List[ItemLines]
    workOrder: WorkOrder