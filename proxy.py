#This is a TCP proxy script which accepts all the data from the client 
#who is sending data and forwards it to the destination client.

from socket import *
import sys,time

def start_proxy(ipaddr, port):
	try:						#create sockets
		s = socket(AF_INET, SOCK_STREAM)	#for listening and receiving data
		s1 = socket(AF_INET, SOCK_STREAM)	#for connecting and sending data
		s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	except socket.error:
		print("Failed to create socket.")
	s.bind((ipaddr, port))				#bind socket to (ipaddr,port)
	s.listen(1)					#start listening through socket, s
	client, addr = s.accept()			#connection found
	print("applying proxy for ",addr)
	time.sleep(1)
	destip = client.recv(9).decode('utf8')		#receiving destination IP address from source client
	time.sleep(1)
	destport = client.recv(4).decode('utf8')	#receiving destination port from source client
	s1.connect((str(destip),int(destport)))		#connect to destination client through socket, s1
	while(True):
		data = client.recv(1024).decode('utf8')	#receive from source client
		if not data:
			break
		print("Message received : ",data)
		print("Sending data to destination")
		s1.send(data.encode('utf8'))		#send to destination client
		
	client.close()					#closing sockets
	s.close()
	s1.close()

if __name__ == '__main__':
	if(len(sys.argv)<3):
		print("Usage : python3 proxy.py bind_proxyip bind_proxyport")
		sys.exit()
	ipaddr = str(sys.argv[1])
	port = int(sys.argv[2])
	start_proxy(ipaddr, port)
