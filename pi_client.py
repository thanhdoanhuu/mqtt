#!/usr/bin/python
 
# RasPi.vn
 
import paho.mqtt.client as client
import json
import socket
#import RPi.GPIO as GPIO 
 


class SendClass(object):
    def __init__(self):
        self.computerName = socket.gethostname()
        self.computerIpAdress = socket.gethostbyname(socket.getfqdn())
        self.message = 0

sendOject = SendClass()

gpio_pin = 14 
#brokerHost = "172.21.33.24" #Rapian vituabox
#brokerHost = "172.20.10.10" #Iphone
# brokerHost = "192.168.43.50" #Leo
brokerHost = "172.21.33.25" #raspberry mac

topic = "raspivn/demo/led"
topicSend = "rapivn/status"
 
#GPIO.setmode(GPIO.BCM) # chon kieu danh so chan GPIO la BCM
#GPIO.setup(gpio_pin, GPIO.OUT)

def on_connect(mqttc, obj, flags, rc):
	pass
 
def on_message(mqttc, obj, msg):
	print("Receive: " +msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

	objReceive = json.loads(msg.payload)
	sendOject.computerName = objReceive["computerName"] = socket.gethostname()
	sendOject.computerIpAdress = objReceive["computerIpAdress"] = socket.gethostbyname(socket.getfqdn())
	

	if(msg.topic == topic):
		if(objReceive["message"] == 1): #bat LED
			#GPIO.output(gpio_pin, GPIO.HIGH)
			print('ON')
			sendOject.message = "ON"
		elif(objReceive["message"] == 0): #tat LED
	 		# GPIO.output(gpio_pin, GPIO.LOW)
			print('OFF')
			sendOject.message = "OFF"
		else:
			print('Do nothing')
			sendOject.message = "Do nothing"

		sendMessage = json.dumps(sendOject.__dict__)
		client.publish(topicSend,sendMessage)#publish
 
def on_publish(mqttc, obj, mid):
	print("mid: "+str(mid))
 
def on_subscribe(mqttc, obj, mid, granted_qos):
	pass
 
def on_log(mqttc, obj, level, string):
	pass

print('start...')
client = client.Client()
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe
 
client.connect(brokerHost, 1883, 60) #dien IP cua Pi, vd: 192.168.1.77
client.subscribe(topic, 0) 
client.loop_forever()