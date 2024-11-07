from dataclasses import dataclass

@dataclass
class Address(object):
    
    customerFirstName: str
    customerLastName: str
    customerPhoneNumber: int
    customerAddressLine1: str
    customerAddressLine2: str
    customerState: str
    customerZipCode: int
