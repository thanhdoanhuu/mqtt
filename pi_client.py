#!/usr/bin/python
 
# RasPi.vn
 
import paho.mqtt.client as mqtt
import json
#import RPi.GPIO as GPIO 
 
gpio_pin = 14 
topics = "raspivn/demo/led"
broker = "172.21.33.24"
 
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

	if(msg.topic == topics):
		if(objReceive["message"] == 1): #bat LED
			#GPIO.output(gpio_pin, GPIO.HIGH)
			print('ON')
		elif(objReceive["message"] == 0): #tat LED
	 		GPIO.output(gpio_pin, GPIO.LOW)
			print('OFF')
 
def on_publish(mqttc, obj, mid):
	print("mid: "+str(mid))
 
def on_subscribe(mqttc, obj, mid, granted_qos):
	pass
 
def on_log(mqttc, obj, level, string):
	pass

print('start...')
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
 
mqttc.connect(broker, 1883, 60) #dien IP cua Pi, vd: 192.168.1.77
mqttc.subscribe(topics, 0) 
mqttc.loop_forever()