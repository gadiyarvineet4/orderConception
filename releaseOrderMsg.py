from pydantic import BaseModel
from addressModel import Address
from releaseItemLinesModel import ItemLines
from workOrderModel import WorkOrder

class ReleaseOrderMsg(BaseModel):

    shipAdviceNo: str
    shipNode: str
    orderType: str
    expectedShipDate: str
    shipToAddress: Address
    itemLines: ItemLines
    workOrder: WorkOrder