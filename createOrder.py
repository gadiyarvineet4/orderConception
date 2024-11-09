from persistToDB import persistToDB
from createOrderResponse import CreateOrderResponse
from createOrderRequest import CreateOrderRequest
from requestValidation import RequestValidation

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

                persistToDB(orderCreationObj)
                response=CreateOrderResponse()
                response.setResponseAttributes(orderCreationObj)
            return response.successResponse()
      
#requirements & improvements:
    #change wrt cloud: input, db access
    #Try except block around db invoke
    #Try except block around implementation
    #Stack trace while catching exceptions
    #import local db into gcp
    #deploy on gcp
    #logging
    #improve logic for each method
    #improve control flow
    #improve schema
    #improve error codes/desc/desc/info
    #stress test
    #populate db with dummy data