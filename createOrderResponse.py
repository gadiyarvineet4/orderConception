from createOrderRequest import CreateOrderRequest

class CreateOrderResponse(object):

    status: str
    message: str
    orderNumber: int
    countryCode: str

    def setResponseAttributes(self, orderMSG:CreateOrderRequest):
        self.status="Success"
        self.message="Order has been Created in Order Management System"
        self.orderNumber=orderMSG.orderNumber
        self.countryCode=orderMSG.countryCode

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