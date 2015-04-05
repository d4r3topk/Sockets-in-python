#  This script is a TCP client script, which connects to a socket(server) 
#  and sends data to it.

from socket import *
import errno,sys

def connect(ipaddr, port):
	try:
		s = socket(AF_INET, SOCK_STREAM)
		s.connect((ipaddr, port))
	except ConnectionRefusedError:
		print("There is no socket at port ",port,". (Please run tcps.py)")
		sys.exit()
	except socket.error:
		print("Failed to create socket.")
		sys.exit()

	while(True):
		try:
			message = input("Enter Message : ")
			if(message!='exit'):
				s.send(message.encode('ascii'))
			else:
				break
		except IOError as e:
			if e.errno == errno.EPIPE:
				print("Connection ended from server")
				break
	
	s.close()

if __name__ == '__main__':
	ipaddr = '127.0.0.1'
	port = 40202
	connect(ipaddr, port)
