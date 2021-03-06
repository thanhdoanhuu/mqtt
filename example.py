import time
import paho.mqtt.client as paho
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

topic = "raspivn/demo/led"
topicReceive = "rapivn/status"

#define callback
def on_message(client, userdata, message):
    print("received: ",str(message.payload.decode("utf-8")))

client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
#####
print("connecting to broker ",brokerHost)
client.connect(brokerHost)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe(topicReceive)#subscribe

input = raw_input("type [on] to turn on LED or type [off] to turn off LED, type [exit] to exit:\n")
print("Ban chon " + input + "!")
run = True
while(run):
	if(input == 'off'):
		sendOject.message = 0
	elif(input == 'on'):
		sendOject.message = 1
	elif(input == 'exit'):
		break
	else:
		sendOject.message = 2

	sendMessage = json.dumps(sendOject.__dict__) 
	# print("publishing: ", sendMessage)
	
	client.publish(topic,sendMessage)#publish

	input = raw_input("")
	print("Your choose: " + input + "!")

client.disconnect() #disconnect
client.loop_stop() #stop loop
