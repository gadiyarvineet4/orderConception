import psycopg2
import json
from createOrderRequest import CreateOrderRequest

def persistToDB(orderMSG:CreateOrderRequest) -> None: 
    orderDict=str(orderMSG)

    conn=psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Vineet1$",
        host="localhost",
        port="5433"
    )       
    cursor=conn.cursor()
    query="INSERT INTO customerOrder (ordernumber,orderdata) VALUES (%s,%s)"
    cursor.execute(query,(orderMSG.orderNumber,orderDict))
    conn.commit()
    cursor.close()
    conn.close()