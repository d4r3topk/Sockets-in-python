#  This script is a TCP server script, which has a unique port given to it 
#  and listens for connections from other sockets(clients) and displays the
#  data sent by them.

from socket import *

def start_listen(ipaddr, port):
	try:
		s = socket(AF_INET, SOCK_STREAM)
	except socket.error:
		print("Failed to create socket.")
	
	s.bind((ipaddr, port))
	print("Waiting for connection. Please run tcpc.py to initiate one")
	s.listen(1)
	client, addr = s.accept()
	print("Connected to IP address", str(addr[0]), "and port ", str(addr[1]))

	while(True):
		data = client.recv(1024).decode('ascii')  
		if not data:
			print("Connection ended by client")
			break
		print("From client : ",data)
	
	client.close()
	s.close()

if __name__ == '__main__':
	ipaddr = '127.0.0.1'
	port = 40202
	start_listen(ipaddr, port)
