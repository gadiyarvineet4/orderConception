from dataclasses import dataclass

@dataclass
class CreateOrderResponse(object):

    status: str = None
    message: str = None
    orderNumber: int = None
    countryCode: str = None

    def setResponseAttributes(self, orderNumber, countryCode):
        self.status="Success"
        self.message="Order has been Created in Order Management System"
        self.orderNumber=orderNumber
        self.countryCode=countryCode

    def successResponse(self): 
        response={
            "status": self.status,
            "message": self.message,
            "data": {
                "order_number":self.orderNumber,
                "country_code":self.countryCode
            }
}
        return response