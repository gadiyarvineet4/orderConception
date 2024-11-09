from fastapi import APIRouter, HTTPException
from createOrder import CreateOrderAPI
from createOrderRequest import CreateOrderRequest
import json

router=APIRouter()

@router.post("/router/createOrder")
async def createOrderAPI(request: CreateOrderRequest):
    create_order=CreateOrderAPI()
    response=create_order.createOrder(request)
    return response
    