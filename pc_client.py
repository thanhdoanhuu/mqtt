#!/usr/bin/python
 
# RasPi.vn
# import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import socket
import os
import json

class SendClass(object):
    def __init__(self):
        self.computerName = socket.gethostname()
        self.computerIpAdress = socket.gethostbyname(socket.getfqdn())
        self.message = 0

sendOject = SendClass()

#brokerHost = "172.21.33.24" #Rapian vituabox
#brokerHost = "172.20.10.10" #Iphone
brokerHost = "192.168.43.50" #Leo

topics = "raspivn/demo/led"

computerName = socket.gethostname()
computerIpAdress = socket.gethostbyname(socket.getfqdn())
print(computerName)
print(computerIpAdress)
input = raw_input("type [on] to turn on LED or type [off] to turn off LED, type [exit] to exit:\n")
print("Ban chon " + input + "!")

run = True
while(run):
	if(input == 'off'):
		sendOject.message = 0
	# publish.single(topics, "0", hostname = brokerHost) 
	elif(input == 'on'):
		sendOject.message = 1
	# publish.single(topics, "1", hostname = brokerHost) 
	elif(input == 'exit'):
		break

	sendMessage = json.dumps(sendOject.__dict__) 
	print(sendMessage)
	publish.single(topics, sendMessage, hostname = brokerHost)

	input = raw_input("")
	print("Ban chon " + input + "!")

print ("Chuong trinh vua thoat")


