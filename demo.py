from socket import *
from threading import *
import time
import _thread

def fun1(ipaddr, port1):
	s1.bind((ipaddr, port1))
	s1.listen(1)
	client,addr = s1.accept()
	data = client.recv(1024).decode('ascii')
	print("Writing from socket 2 : ",data)
	client.close()
	s1.close()
	s2.close()

def fun2(ipaddr, port1):
	time.sleep(0.5)
	s2.connect((ipaddr, port1))
	message = input("Enter message to be sent(Reading from socket 1) : ")
	s2.send(message.encode('ascii'))

class MyThread(Thread) :
	def __init__(self, fn, ipaddr, port) :
		Thread.__init__(self, target=fn,args=(ipaddr,port))

if __name__ == '__main__':
	ipaddr = '127.0.0.1'
	port = 40202
	try:
		s1 = socket(AF_INET, SOCK_STREAM)
		s2 = socket(AF_INET, SOCK_STREAM)
	except socket.error:
		print("Failed to create socket.")
	s1.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	t1 = MyThread(fun1, ipaddr, port)
	t2 = MyThread(fun2, ipaddr, port)
	t1.start()
	t2.start()
