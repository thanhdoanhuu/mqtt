#!/usr/bin/python
 
# RasPi.vn
 
import paho.mqtt.client as client
import json
#import RPi.GPIO as GPIO 
 
gpio_pin = 14 
#brokerHost = "172.21.33.24" #Rapian vituabox
#brokerHost = "172.20.10.10" #Iphone
brokerHost = "192.168.43.50" #Leo

topic = "raspivn/demo/led"
 
#GPIO.setmode(GPIO.BCM) # chon kieu danh so chan GPIO la BCM
#GPIO.setup(gpio_pin, GPIO.OUT)

def on_connect(mqttc, obj, flags, rc):
	pass
 
def on_message(mqttc, obj, msg):
	print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

	objReceive = json.loads(msg.payload)
	print (objReceive["computerName"])
	print (objReceive["computerIpAdress"])
	print (objReceive["message"])

	if(msg.topic == topic):
		if(objReceive["message"] == 1): #bat LED
			#GPIO.output(gpio_pin, GPIO.HIGH)
			print('ON')
		elif(objReceive["message"] == 0): #tat LED
	 		# GPIO.output(gpio_pin, GPIO.LOW)
			print('OFF')

		# client.publish(topic,str(msg.payload))#publish
 
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