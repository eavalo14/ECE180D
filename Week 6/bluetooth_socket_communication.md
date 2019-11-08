Steps to get both devices paired and connected:

1: Pair Raspberry Pi's
	
	- in order to pair the devices go ahead and follow the steps in the link below
	Note: to recall in the last lab section that we tried to connect bluetooth, 
	I had problems with bluetoothctl. To fix this issue I installed the newest 
	version of Rasbian and it fixed my problem when running bluetoothctl

	link: https://bluedot.readthedocs.io/en/latest/pairpipi.html
	
	-exit bluetoothctl
		type quit

2: Note the master(server) and slave's (client) bluetooth MAC address

	-on respected server and client go to github and clone the rfcomm-server.py in the server's directory
	and clone rfcomm-client.py onto the clients local directory

	-On servers command prompt run hciconfig and record MAC address
	-Copy MAC address and replace with the one in rfcomm-client.py

3. Install Bluetooth libraries for python development

	sudo apt-get install bluetooth libbluetooth-dev
	sudo pip install pybluez

4:Run scripts in order

	1. Server: python rfcomm-server.py
	2. Client: python rfcomm-client.py

	-verify that the connection is established and data is transmitting sockets 




Issues I ran accross and resolved:
1. When I tried pairing and running discoverable on, I would recieve and error
the way I resolved this is by following the link below

https://github.com/intel/edison-linux/issues/14


Note: In a bluetooth connection, we can pair as many devices as we can; however, we 
can only connect to 7 devices at the same time. (in our design, we can assume that
the devices are all paired)

