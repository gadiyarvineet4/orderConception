from dataclasses import dataclass

@dataclass
class WorkOrder(object):
    workOrderNumber: int
    workOrderSGR: str
    appointmentStartTime: str
    appointmentEndTime: str