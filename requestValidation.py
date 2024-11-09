import psycopg2
from error import Error
from createOrderRequest import CreateOrderRequest

class RequestValidation(object):

    def validateCustomerPhoneAndPaymentInfo(self,creationRequestMsg:CreateOrderRequest,didValidationPass):

    #print("validatecustomerPhoneAndPaymentInfo: begin")-- can be used for logging/debugging

        error=Error()
       
        if len(str(creationRequestMsg.shipToAddress.customerPhoneNumber)) != 10 and didValidationPass:
            #print("Invalid Request: Incorrect length of customer phone number")
            didValidationPass=False
            error.setResponseAttributes("Bad Request Error",400,"Incorrect length of customer phone number","customerPhoneNumber")
            return didValidationPass,error.errorResponse()
        
        if creationRequestMsg.paymentInfo.status not in ['Paid','Unpaid'] and didValidationPass: 
            #print("Invalid Request: Invalid Payment Status")
            didValidationPass=False
            error.setResponseAttributes('Bad Request Error',400,"Invalid Payment Status","status")
            return  didValidationPass,error.errorResponse()
            
        elif creationRequestMsg.paymentInfo.status == 'Paid' and didValidationPass: 
            if creationRequestMsg.paymentInfo.paymentType not in ['Online','Cash']:
                #print("Invalid Request: Invalid Payment Type")
                didValidationPass=False
                error.setResponseAttributes('Bad Request Error',400,"Invalid Payment Type","paymentType")
                return didValidationPass,error.errorResponse()

        elif creationRequestMsg.paymentInfo.status == 'Unpaid' and didValidationPass:
            if creationRequestMsg.paymentInfo.paymentType != 'COD': 
                #print("Invalid Request: Invalid Payment Type")
                didValidationPass=False
                error.setResponseAttributes('Bad Request Error',400,"Invalid Payment Type","paymentType")
                return didValidationPass,error.errorResponse()
            
        didValidationPass=True
        return didValidationPass, error.nullErrorResponse()
            
    #print("validatecustomerPhoneAndPaymentInfo: end")-- can be used for logging/debugging

    def validateDataFromOrgTable(self,creationRequestMsg:CreateOrderRequest,didValidationPass): 

    #print("validateDataFromOrgTable: begin")-- can be used for logging/debugging
        error=Error()

        conn=psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Vineet1$",
            host="localhost",
            port="5433"
        )       
        cursor=conn.cursor()
        query="SELECT * FROM ORGANIZATION WHERE ORGANIZATION_CODE=%s"
        cursor.execute(query,(creationRequestMsg.seller,))
        row=cursor.fetchone()
        cursor.close()
        conn.close()

        if row is None and didValidationPass: 
            didValidationPass=False
            error.setResponseAttributes('Bad Request Error',400,"Invalid Seller Code","seller")
            return didValidationPass,error.errorResponse()
    
        dbOrganizationCode=row[1]
        dbParentOrgCode=row[3]

        if dbOrganizationCode != creationRequestMsg.seller and didValidationPass : 
            #print("Invalid Request: Request Seller Code doesn't match Data in DB")
            didValidationPass=False
            error.setResponseAttributes('Bad Request Error',400,"Request Seller Code doesn't match Data in DB","seller")
            return didValidationPass,error.errorResponse()

        if dbParentOrgCode != creationRequestMsg.countryCode and didValidationPass: 
            #print("Invalid Request: Request Country Code doesn't match Data in DB")
            didValidationPass=False
            error.setResponseAttributes('Bad Request Error',400,"Request Country Code doesn't match Data in DB","countryCode")
            return didValidationPass,error.errorResponse()
        
        didValidationPass=True
        return didValidationPass, error.nullErrorResponse()
          
    #print("validateDataFromOrgTable: end")-- can be used for logging/debugging

    def validateShipNode(self,creationRequestMsg:CreateOrderRequest,didValidationPass):

        #print("validateShipNode: begin")-- can be used for logging/debugging

        error=Error()

        conn=psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="Vineet1$",
                host="localhost",
                port="5433"
            )       
        cursor=conn.cursor()
       
        for requestItemLines in creationRequestMsg.itemLines:

            query="SELECT * FROM ORGANIZATION WHERE ORGANIZATION_CODE=%s"
            cursor.execute(query,(requestItemLines.ship_node,))
            row=cursor.fetchone()

            if row is None and didValidationPass: 
                #print("Invalid Request: Invalid Ship Node")
                didValidationPass=False
                error.setResponseAttributes('Bad Request Error',400,"Invalid Ship Node","ship_node")
                return didValidationPass,error.errorResponse()
            
        cursor.close()
        conn.close()

        didValidationPass=True
        return didValidationPass, error.nullErrorResponse()

    #print("validateShipNode: end")-- can be used for logging/debugging

    def validateDataFromServiceSkillTable(self,creationRequestMsg:CreateOrderRequest,didValidationPass):

    #print("validateDataFromServiceSkillTable: begin")-- can be used for logging/debugging
        
        error=Error()

        conn=psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Vineet1$",
            host="localhost",
            port="5433"
        )       
        cursor=conn.cursor()
        query="SELECT * FROM SERVICE_SKILL WHERE ORGANIZATION_CODE=%s"
        cursor.execute(query,(creationRequestMsg.countryCode,))
        row=cursor.fetchone()
        cursor.close()
        conn.close()

        if row is None and didValidationPass: 
            #print("Invalid Request: Invalid Work Order SGR")
            didValidationPass=False
            error.setResponseAttributes('Bad Request Error',400,"Invalid Work Order SGR","workOrderSGR")
            return didValidationPass,error.errorResponse()
        
        dbOrgCode=row[2]
        if creationRequestMsg.countryCode != dbOrgCode and didValidationPass: 
            #print("Internal Error: Service Skill not present for Organization")
            didValidationPass=False
            error.setResponseAttributes('Bad Request Error',400,"Service Skill not present for Organization","workOrderSGR")
            return didValidationPass,error.errorResponse()
        
        dbServiceSkillType=row[4]
        if creationRequestMsg.orderType != dbServiceSkillType and didValidationPass: 
            #print("Invalid Request: Invalid Order Type")
            didValidationPass=False
            error.setResponseAttributes('Bad Request Error',400,"Invalid Order Type","orderType")
            return didValidationPass,error.errorResponse()
        
        dbServiceSkillID=row[1]
        if (creationRequestMsg.workOrder.workOrderSGR) != dbServiceSkillID and didValidationPass: 
            #print("Invalid Request: Invalid Work Order SGR ")
            didValidationPass=False
            error.setResponseAttributes('Bad Request Error',400,"Invalid Work Order SGR","workOrderSGR")
            return didValidationPass,error.errorResponse()
        
        didValidationPass=True
        return didValidationPass, error.nullErrorResponse()
        
    #print("validateDataFromServiceSkillTable: end")-- can be used for logging/debugging

    def validateDataFromItemTable(self,creationRequestMsg:CreateOrderRequest,didValidationPass):

    #print("validateDataFromItemTable: begin")-- can be used for logging/debugging
        
        error=Error()

        conn=psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="Vineet1$",
            host="localhost",
            port="5433"
        )       
        cursor=conn.cursor()

        for requestItemLines in creationRequestMsg.itemLines:

            query = "SELECT * FROM ITEM WHERE ORGANIZATION_CODE=%s AND ITEM_ID = %s"
            cursor.execute(query, (creationRequestMsg.countryCode, requestItemLines.itemId,))
            row=cursor.fetchone()

            if row is None and didValidationPass: 
                #print("Invalid Request: Item ID's aren't present")
                didValidationPass=False
                error.setResponseAttributes('Bad Request Error',400,"Item ID's aren't present","itemLines")
                return didValidationPass,error.errorResponse()

            dbItemID=row[1]
            dbOrgCode=row[10]
            if dbItemID != requestItemLines.itemId and didValidationPass: 
                #print("Invalid Request: Item not present")
                didValidationPass=False
                error.setResponseAttributes('Bad Request Error',400,"Item not present","itemLines")
                return didValidationPass,error.errorResponse()
                
            if creationRequestMsg.countryCode != dbOrgCode and didValidationPass: 
                #print("Internal Error: Item Table Organization Code doesn't match Request Code")
                #change to internalservererror method
                didValidationPass=False
                error.setResponseAttributes('Bad Request Error',500,"Item Table Organization Code doesn't match Request Code","itemLines")
                return didValidationPass,error.errorResponse()
            
        cursor.close()
        conn.close()  

        didValidationPass=True
        return didValidationPass, error.nullErrorResponse()

#print("validateDataFromItemTable: end")-- can be used for logging/debugging