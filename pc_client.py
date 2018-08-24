import time
import paho.mqtt.client as paho
import os
import json
import define 

brokerHost = define.brokerHost
topic = define.topic
topicReceive = define.topicReceive
sendOject = define.SendClass()

print("Your broker is " + brokerHost +"  press enter, is not please input your broker address.")
input = raw_input("")
if input != "":
	brokerHost = input

#define callback
def on_message(client, userdata, message):
    print("received: ",str(message.payload.decode("utf-8")))
    # print("message topic=",message.topic)
    # print("message qos=",message.qos)
    # print("message retain flag=",message.retain)

client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
client.will_set(topic, payload='{"computerName": "reconnect", "message": 0, "computerIpAdress": "172.21.33.25"}', qos=0, retain=False)
#####
print("Connecting to broker " + brokerHost)
client.connect(brokerHost)#connect
client.loop_start() #start loop to process received messages
print("subscribing " + topicReceive)
client.subscribe(topicReceive)#subscribe
# client.subscribe(topic)#subscribe

input = raw_input("type [on] to turn on LED or type [off] to turn off LED, type [exit] to exit:\n")
print("Your choose " + input + "!")


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
