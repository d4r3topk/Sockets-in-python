#This is a TCP proxy script which accepts all the data from the client 
#who is sending data and forwards it to the destination client.

from socket import *
import sys,time

def start_proxy(ipaddr, port):
	try:
		s = socket(AF_INET, SOCK_STREAM)
		s1 = socket(AF_INET, SOCK_STREAM)
		s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	except socket.error:
		print("Failed to create socket.")
	s.bind((ipaddr, port))
	s.listen(1)
	client, addr = s.accept()
	print("applying proxy for ",addr)
	time.sleep(1)
	destip = client.recv(9).decode('utf8')
	time.sleep(1)
	destport = client.recv(4).decode('utf8')
	s1.connect((str(destip),int(destport)))
	while(True):
		data = client.recv(1024).decode('utf8')
		if not data:
			break
		print("Message received : ",data)
		print("Sending data to destination")
		s1.send(data.encode('utf8'))
		
	client.close()
	s.close()
	s1.close()

if __name__ == '__main__':
	if(len(sys.argv)<3):
		print("Usage : python3 proxy.py bind_proxyip bind_proxyport")
		sys.exit()
	ipaddr = str(sys.argv[1])
	port = int(sys.argv[2])
	start_proxy(ipaddr, port)
