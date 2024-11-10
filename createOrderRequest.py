from addressModel import Address
from paymentInfoModel import PaymentInfo
from itemLinesModel import ItemLines
from workOrderModel import WorkOrder
from pydantic import BaseModel
from typing import List


class CreateOrderRequest(BaseModel):

    #start order header
    orderNumber: int
    countryCode: str
    seller: str
    orderType: str
    orderDate: str
    shipToAddress: Address
    billToAddress: Address
    #end order header
    paymentInfo: PaymentInfo
    itemLines: List[ItemLines]
    workOrder: WorkOrder