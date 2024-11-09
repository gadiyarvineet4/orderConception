from pydantic import BaseModel

class WorkOrder(BaseModel):
    workOrderNumber: int
    workOrderSGR: str
    appointmentStartTime: str
    appointmentEndTime: str