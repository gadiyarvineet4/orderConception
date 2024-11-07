from parseRequest import parseRequest
from persistToDB import persistToDB
from createOrderResponse import CreateOrderResponse
from requestValidation import RequestValidation

class CreateOrderAPI(object):

    def __init__(self) -> None:
        pass

    def createOrder(self):
    
            orderCreationMSG=parseRequest()
            didValidationPass=True
            valiationHelper=RequestValidation()
            
            if didValidationPass:
               
               didValidationPass, errorResponse=valiationHelper.validateCustomerPhoneAndPaymentInfo(orderCreationMSG,didValidationPass)
               
               if didValidationPass is False:
                   return errorResponse
                     
            if didValidationPass:

                didValidationPass, errorResponse=valiationHelper.validateDataFromOrgTable(orderCreationMSG,didValidationPass)
               
                if didValidationPass is False:
                   return errorResponse
                   
            if didValidationPass:

                didValidationPass, errorResponse=valiationHelper.validateShipNode(orderCreationMSG,didValidationPass)
                
                if didValidationPass is False:
                   return errorResponse
                   
            if didValidationPass:

                didValidationPass, errorResponse=valiationHelper.validateDataFromServiceSkillTable(orderCreationMSG,didValidationPass)
                
                if didValidationPass is False:
                   return errorResponse
                   
            if didValidationPass:

                didValidationPass, errorResponse=valiationHelper.validateDataFromItemTable(orderCreationMSG,didValidationPass)
                
                if didValidationPass is False:
                   return errorResponse
                   
            if didValidationPass:

                persistToDB(orderCreationMSG)
                response=CreateOrderResponse()
                orderNumber=orderCreationMSG["orderNumber"]
                countryCode=orderCreationMSG["countryCode"]
                response.setResponseAttributes(orderNumber,countryCode)
            return response.successResponse()
      
app=CreateOrderAPI()
app.createOrder()


#requirements & improvements:
    #use req as object
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