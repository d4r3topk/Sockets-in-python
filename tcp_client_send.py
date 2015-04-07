#  This script is a TCP client script, which connects to a socket(server) 
#  and sends data to it.

from socket import *
import errno,sys

def connect(proxyip,proxyport,ipaddr, port):
	try:							#Create socket
		s = socket(AF_INET, SOCK_STREAM)
		s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		s.connect((proxyip, proxyport))			#Connect to the proxy
	except ConnectionRefusedError:				#incase no socket at (proxyip,proxyport)
		print("There is no socket at ipaddress ",proxyip," port ",proxyport,".")
		sys.exit()
	except socket.error:
		print("Failed to create socket.")
		sys.exit()
	print("Proxy connected")
	time.sleep(1)
	s.send(ipaddr.encode('utf8'))				#send destination IP address
	time.sleep(1)
	s.send(port.encode('utf8'))				#send destination port number
	while(True):
		try:
			message = input("Enter Message : ")
			if(message!='exit'):
				s.send(message.encode('utf8'))	#send messages for destination
			else:
				break
		except IOError as e:				#incase the pipe is broken(one client ends abruptly)
			if e.errno == errno.EPIPE:
				print("Connection ended")
				break
	
	s.close()

if __name__ == '__main__':
	if(len(sys.argv)<5):
		print("Usage : python3 tcp_client_send.py proxyip proxyport destip destport")
		sys.exit()	
	proxyip = str(sys.argv[1]) 
	proxyport = int(sys.argv[2])
	ipaddr = sys.argv[3]
	port = sys.argv[4]
	connect(proxyip, proxyport, ipaddr, port)
