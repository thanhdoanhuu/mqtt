#!/usr/bin/python
 
# RasPi.vn
# import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

topics = "raspivn/demo/led"
brokerHost = "172.21.33.24"



input = raw_input("type [on] to turn on LED or type [off] to turn off LED, type [exit] to exit:\n")
print("Ban chon " + input + "!")

run = True
while(run):
 if(input == 'off'):
   publish.single(topics, "0", hostname = brokerHost) 
 elif(input == 'on'):
   publish.single(topics, "1", hostname = brokerHost) 
 elif(input == 'exit'):
   break
 input = raw_input("")
 print("Ban chon " + input + "!")
 #-------------------------------------------------------------------------------------------
 #m = subscribe.simple(topics, hostname="172.21.33.24", retained=False, msg_count=2)
 #for a in m:
 #   print(a.topic)
 #   print(a.payload)
#-------------------------------------------------------------------------------------------

print ("Chuong trinh vua thoat")
