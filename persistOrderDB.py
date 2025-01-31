from createOrderRequest import CreateOrderRequest
from datetime import datetime
import random
import psycopg2

class PersistOrderDB(object):

    def __init__(self):

        self.orderHeaderKey=self.generateKey()
        self.workOrderKey=self.generateKey()
        self.shipAdviceNo=self.generateShipAdviceNo()
        self.orderLineKey=None

    def persistOrderDB(self,order:CreateOrderRequest):
        
        order_header_query=self.createOrderHeaderQuery()
        address_query=self.createAddressQuery()
        payment_query=self.createPaymentDetailsQuery()
        order_line_query=self.createOrderLineQuery()
        work_order_query=self.createWorkOrderQuery()
        order_status_query=self.createOrderStatusQuery()
        self.executeQueries(order, order_header_query, address_query,payment_query,order_line_query,work_order_query,order_status_query)

    def executeQueries(self,order:CreateOrderRequest, order_header_query, address_query,payment_query,order_line_query,work_order_query,order_status_query):
        #try: 
            conn=psycopg2.connect(
                    dbname="postgres",
                    user="postgres",
                    password="Vineet1$",
                    host="localhost",
                    port="5433"
                ) 
            cursor = conn.cursor()
            #try:
                #order_header_query
            cursor.execute(order_header_query, (self.orderHeaderKey,
                                    order.orderNumber,
                                    order.countryCode,
                                    order.seller,
                                    order.orderType,
                                    datetime.strptime(order.orderDate, "%Y-%m-%dT%H:%M:%S.%fZ"),100))
                    
                    #address_query: shipping
            cursor.execute(address_query,(self.orderHeaderKey,
                                    order.orderNumber,
                                    "shipping",
                                    order.shipToAddress.customerFirstName,
                                    order.shipToAddress.customerLastName,
                                    order.shipToAddress.customerPhoneNumber,
                                    order.shipToAddress.customerAddressLine1,
                                    order.shipToAddress.customerAddressLine2,
                                    order.shipToAddress.customerState,
                                    order.shipToAddress.customerZipCode))
                    
                    #address_query: billing
            cursor.execute(address_query,(self.orderHeaderKey,
                                    order.orderNumber,
                                    "billing",
                                    order.billToAddress.customerFirstName,
                                    order.billToAddress.customerLastName,
                                    order.billToAddress.customerPhoneNumber,
                                    order.billToAddress.customerAddressLine1,
                                    order.billToAddress.customerAddressLine2,
                                    order.billToAddress.customerState,
                                    order.billToAddress.customerZipCode))
                    
                    #payment_query
            cursor.execute(payment_query,(self.orderHeaderKey,
                                    order.orderNumber,
                                    order.paymentInfo.status,
                                    order.paymentInfo.paymentType,
                                    order.paymentInfo.total,
                                    order.paymentInfo.itemTotal,
                                    order.paymentInfo.deliveryTotal,
                                    order.paymentInfo.tax))
                    
                    #order_line_query
            for itemLines in order.itemLines:
                        self.orderLineKey=self.generateKey()
                        cursor.execute(order_line_query,(self.orderHeaderKey,
                                        self.orderLineKey,
                                        order.orderNumber,
                                        self.shipAdviceNo,
                                        itemLines.itemType,
                                        itemLines.itemId,
                                        itemLines.itemName,
                                        itemLines.quantity,
                                        itemLines.itemLineNo,
                                        itemLines.deliveryLineNo,
                                        itemLines.price,
                                        itemLines.sku,
                                        itemLines.description,
                                        itemLines.ship_node,
                                        datetime.strptime(itemLines.ship_date, "%Y-%m-%dT%H:%M:%S.%fZ"),
                                        100,
                                        False))
                    
                    #work_order_query
            cursor.execute(work_order_query,(self.workOrderKey,
                                    self.orderHeaderKey,
                                    order.workOrder.workOrderNumber,
                                    order.workOrder.workOrderSGR,
                                    order.workOrder.deliveryLineNo,
                                    datetime.strptime(order.workOrder.appointmentStartTime, "%Y-%m-%dT%H:%M:%S.%fZ"),
                                    datetime.strptime(order.workOrder.appointmentEndTime, "%Y-%m-%dT%H:%M:%S.%fZ"),
                                    order.workOrder.deliveryInstructions, 100
                                    ))
                    #order_status_query
            cursor.execute(order_status_query,(order.orderNumber,
                                    self.orderHeaderKey, 
                                    100,
                                    100,
                                    self.workOrderKey,
                                    1100,
                                    'preReleaseHold',
                                    datetime.strptime(order.orderDate, "%Y-%m-%dT%H:%M:%S.%fZ")
                                    ))
            conn.commit()

            #except psycopg2.IntegrityError as e:
                #conn.rollback()
                #raise(f"Integrity error: {e}")
                    
            #except psycopg2.DatabaseError as e:
               #conn.rollback()
                #raise(f"Database error: {e}")
                
            #except Exception as e:
               #conn.rollback()
                #raise(f"An unexpected error occurred: {e}")

        #except psycopg2.Error as e:
            #raise(f"Failed to connect to the database: {e}")
            cursor.close()
            conn.close()

        #finally:
            #if cursor:
                #cursor.close()
            #if conn:
                #conn.close()
            
    def createOrderHeaderQuery(self):

        order_header_query= "INSERT INTO order_header (order_header_key, order_number, country_code, seller, order_type, order_date, order_status) VALUES (%s, %s, %s, %s, %s, %s,%s)"
        return order_header_query

    def createAddressQuery(self):
        
        address_query= "INSERT INTO customer_addresses (order_header_key, order_number, address_type, customer_first_name, customer_last_name, customer_phone_number,customer_address_line1,customer_address_line2,customer_state,customer_zip_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        return address_query

    def createPaymentDetailsQuery(self):

        payment_query="INSERT INTO payment_info (order_header_key, order_number, payment_status, payment_type, total, item_total,delivery_total,tax) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        return payment_query

    def createOrderLineQuery(self):
        
        order_line_query="INSERT INTO order_line(order_header_key,order_line_key,order_number,ship_advice_no,item_type,item_id,item_name,quantity,item_line_no,delivery_line_no,price,sku,description,ship_node,ship_date,line_status,release_attempted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        return order_line_query

    def createWorkOrderQuery(self):
        work_order_query="INSERT INTO work_order(work_order_key,order_header_key,work_order_number,work_order_sgr,delivery_line_no,appointment_start_time,appointment_end_time,delivery_instructions,work_order_status) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)"
        return work_order_query
    
    def generateShipAdviceNo(self):
        return random.randint(999,9999)
    
    def createOrderStatusQuery(self):
        order_status_query="INSERT INTO sales_order_status(order_number, order_header_key,order_status,work_order_status,work_order_key,order_hold,order_hold_type,order_date) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
        return order_status_query

    def generateKey(self):    
        currDateTime = datetime.now().strftime("%Y%m%d%H%M%S")
        orderKey=currDateTime + str(random.randint(9999,99999))
        return orderKey