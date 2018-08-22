#!/usr/bin/python
 
# RasPi.vn
 
import paho.mqtt.client as mqtt
#import RPi.GPIO as GPIO 
 
gpio_pin = 14 
 
#GPIO.setmode(GPIO.BCM) # chon kieu danh so chan GPIO la BCM
#GPIO.setup(gpio_pin, GPIO.OUT)
print('connect')
def on_connect(mqttc, obj, flags, rc):
 pass
 
def on_message(mqttc, obj, msg):
 print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
 if(msg.topic == "raspivn/demo/led"):
   if(str(msg.payload) == "1"): #bat LED
     #GPIO.output(gpio_pin, GPIO.HIGH)
       print('ON')
   elif(str(msg.payload) == "0"): #tat LED
     #GPIO.output(gpio_pin, GPIO.LOW)
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
 
mqttc.connect("172.21.33.24", 1883, 60) #dien IP cua Pi, vd: 192.168.1.77
mqttc.subscribe("raspivn/demo/led", 0) 
mqttc.loop_forever()