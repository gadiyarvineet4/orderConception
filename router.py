from fastapi import APIRouter, HTTPException
from createOrder import CreateOrderAPI

router=APIRouter()

@router.post("/router/createOrder")
async def createOrderAPI():
    create_order=CreateOrderAPI()
    response=create_order.createOrder()
    return response
    