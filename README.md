
#start mqtt broker
sudo /etc/init.d/mosquitto start 

#stop mqtt broker
sudos  /etc/init.d/mosquitto stop


#Install the dependencies
	$ sudo apt-get update
	$ sudo apt-get install build-essential python quilt python-setuptools python3
	$ sudo apt-get install libssl-dev
	$ sudo apt-get install cmake
	$ sudo apt-get install libc-ares-dev
	$ sudo apt-get install uuid-dev
	$ sudo apt-get install daemon
	$ sudo apt-get install libwebsockets-dev
#Download mosquitto
	$ cd Downloads/
	$ wget http://mosquitto.org/files/source/mosquitto-1.4.10.tar.gz
	$ tar zxvf mosquitto-1.4.10.tar.gz
	$ cd mosquitto-1.4.10/
	$ sudo nano config.mk
#Edit config.mk
	WITH_WEBSOCKETS:=yes
#Build mosquitto
	$ make
	$ sudo make install
	$ sudo cp mosquitto.conf /etc/mosquitto
#Configure ports for mosquitto
#Add the following lines to /etc/mosquitto/mosquitto.conf in the "Default Listener" section:
	port 1883
	listener 9001
	protocol websockets
#Add user for mosquitto
$ sudo adduser mosquitto
Reeboot computer
$ reboot
Run mosquitto
$ mosquitto -c /etc/mosquitto/mosquitto.conf
