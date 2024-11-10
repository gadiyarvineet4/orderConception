from createOrderResponse import CreateOrderResponse
from createOrderRequest import CreateOrderRequest
from requestValidation import RequestValidation
from persistOrderDB import PersistOrderDB

class CreateOrderAPI(object):

    def __init__(self) -> None:
        pass

    def createOrder(self, orderCreationObj:CreateOrderRequest):

            didValidationPass=True
            valiationHelper=RequestValidation()
            
            if didValidationPass:
               
               didValidationPass, errorResponse=valiationHelper.validateCustomerPhoneAndPaymentInfo(orderCreationObj,didValidationPass)
               
               if didValidationPass is False:
                   return errorResponse
                     
            if didValidationPass:

                didValidationPass, errorResponse=valiationHelper.validateDataFromOrgTable(orderCreationObj,didValidationPass)
               
                if didValidationPass is False:
                   return errorResponse
                   
            if didValidationPass:

                didValidationPass, errorResponse=valiationHelper.validateShipNode(orderCreationObj,didValidationPass)
                
                if didValidationPass is False:
                   return errorResponse
                   
            if didValidationPass:

                didValidationPass, errorResponse=valiationHelper.validateDataFromServiceSkillTable(orderCreationObj,didValidationPass)
                
                if didValidationPass is False:
                   return errorResponse
                   
            if didValidationPass:

                didValidationPass, errorResponse=valiationHelper.validateDataFromItemTable(orderCreationObj,didValidationPass)
                
                if didValidationPass is False:
                   return errorResponse
                   
            if didValidationPass:

                saveOrderToDB=PersistOrderDB()
                saveOrderToDB.persistOrderDB(orderCreationObj)
                response=CreateOrderResponse()
                response.setResponseAttributes(orderCreationObj)
                
            return response.successResponse()