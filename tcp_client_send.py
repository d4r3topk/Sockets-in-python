#  This script is a TCP client script, which connects to a socket(server) 
#  and sends data to it.

from socket import *
import errno,sys

def connect(proxyip,proxyport,ipaddr, port):
	try:
		s = socket(AF_INET, SOCK_STREAM)
		s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		s.connect((proxyip, proxyport))
	except ConnectionRefusedError:
		print("There is no socket at port ",proxyport,".")
		sys.exit()
	except socket.error:
		print("Failed to create socket.")
		sys.exit()
	print("Proxy connected")
	s.send(ipaddr.encode('utf8'))
	s.send(port.encode('utf8'))
	while(True):
		try:
			message = input("Enter Message : ")
			if(message!='exit'):
				s.send(message.encode('utf8'))
			else:
				break
		except IOError as e:
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
