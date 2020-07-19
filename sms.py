#!/bin/python3

from ipaddress import IPv4Address
from pyairmore.request import AirmoreSession
from pyairmore.services.messaging import MessagingService

def get_data_connection():
    ip  = input("phone ip:")
    port = int(input("port(defualt=2333):"))
    ip4 = IPv4Address(ip)
    return ip4 , port

def connection():
    global session
    if session.is_server_running:
        print("server is up")
    if  session.request_authorization() :
        print("yah, you`r connect")
    else:
        connection()

def sending():
    global session
    rucontinue = "y"
    while rucontinue == "y":
        phone_number = input("insert your taget phone number:")
        count_massage = int(input("how many times?"))
        massage = input("your massage:")
        service = MessagingService(session)
        for i in range (0,count_massage):
            print ("massage %s is seding" %str(i+1))
            service.send_message(phone_number, massage)
        rucontinue = input("are you want to continue?(y for continue)")

ip4 , port = get_data_connection()
session = AirmoreSession(ip4 ,port)
connection()
sending()