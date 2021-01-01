import socket

class Network:
	server = '192.168.1.8'
	port = 5555

	def __init__(self):
		self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.addr = (self.server,self.port)
		self.pos = self.connect()

	def connect(self):
		self.client.connect(self.addr)
		reply = self.client.recv(2048)
		return reply.decode()

	def send(self,data):
		self.client.send(str.encode(data))
		x = self.client.recv(2048).decode()

	def get_pos(self):
		return self.pos




