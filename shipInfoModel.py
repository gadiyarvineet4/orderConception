from pydantic import BaseModel

class ShipInfoModel(BaseModel):

    ship_node: str
    ship_date: str