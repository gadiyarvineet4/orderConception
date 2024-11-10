from pydantic import BaseModel

class WorkOrder(BaseModel):
    workOrderNumber: int
    workOrderSGR: str
    deliveryLineNo: int
    appointmentStartTime: str
    appointmentEndTime: str