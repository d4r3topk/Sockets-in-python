#  This script is a TCP client script, which has a unique port given to it 
#  and listens for connections from other sockets(clients) and displays the
#  data sent by them.

from socket import *
import sys

def start_listen(ipaddr, port):
	try:							#Create a socket
		s = socket(AF_INET, SOCK_STREAM)
		s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	except socket.error:
		print("Failed to create socket.")
	
	s.bind((ipaddr, port))					#bind it to a ip address and port
	print("Waiting for connection.")
	s.listen(1)						#Start listening for connections
	client, addr = s.accept()				#accept the first connection found
	print("Connected to IP address", str(addr[0]), "and port ", str(addr[1]))

	while(True):
		data = client.recv(1024).decode('utf8')  	#receive 1024 bytes of data from client
		if not data:					#end if no more data received
			print("Connection ended by client")
			break
		print("From client : ",data)
	
	client.close()						#closing sockets
	s.close()

if __name__ == '__main__':
	if(len(sys.argv)<3):
		print("Usage : python3 tcp_client_receive.py bind_ip bind_port")
		sys.exit()	
	ipaddr = str(sys.argv[1]) 
	port = int(sys.argv[2])
	start_listen(ipaddr, port)
