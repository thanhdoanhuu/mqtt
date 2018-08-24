import socket

class SendClass(object):
    def __init__(self):
        self.computerName = socket.gethostname()
        self.computerIpAdress = socket.gethostbyname(socket.getfqdn())
        self.message = 0

#brokerHost = "172.21.33.24" #Rapian vituabox
#brokerHost = "172.20.10.10" #Iphone
#brokerHost = "192.168.43.50" #Leo
 brokerHost = "172.21.33.25" #raspberry mac

topic = "raspivn/demo/led"
topicReceive = "rapivn/status"

gpio_pin = 14 
