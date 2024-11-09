from pydantic import BaseModel

class Address(BaseModel):
    
    customerFirstName: str
    customerLastName: str
    customerPhoneNumber: int
    customerAddressLine1: str
    customerAddressLine2: str
    customerState: str
    customerZipCode: int