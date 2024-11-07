import psycopg2
import json

def persistToDB(orderMSG) -> None: 
    orderNumber=orderMSG["orderNumber"]
    orderJSON=json.dumps(orderMSG)

    conn=psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Vineet1$",
        host="localhost",
        port="5433"
    )       
    cursor=conn.cursor()
    query="INSERT INTO customerOrder (ordernumber,orderdata) VALUES (%s,%s)"
    cursor.execute(query,(orderNumber,orderJSON))
    conn.commit()
    cursor.close()
    conn.close()