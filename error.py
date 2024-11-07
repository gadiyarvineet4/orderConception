from dataclasses import dataclass, field

@dataclass
class Error(object):
    
    status: str = field(default="error")
    errorType: str = None
    errorCode: int = None
    errorRelatedMoreInfo: str = None
    attribute: str = None

    #should be called in respective error methods
    def setResponseAttributes(self,errorType,errorCode,errorRelatedMoreInfo,attribute):
        self.status="error"
        self.errorType=errorType
        self.errorCode=errorCode
        self.errorRelatedMoreInfo=errorRelatedMoreInfo
        self.attribute=attribute


    def errorResponse(self):
        error={
            "status":self.status,
            "error_type":self.errorType,
            "error_code":self.errorCode,
            "attribute":self.attribute,
            "error_related_more_info":self.errorRelatedMoreInfo
        }
        return error
    
    def nullErrorResponse(self):
        error={
            "status":"null",
            "error_type":"null",
            "error_code":"null",
            "attribute":"null",
            "error_related_more_info":"null"
        }
        return error



    