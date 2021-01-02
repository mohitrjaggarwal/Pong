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
		reply1 = self.client.recv(2048)
		reply2 = self.client.recv(2048)
		return reply1.decode() , reply2.decode()

	def send(self,data):
		try:
			self.client.send(str.encode(data))
		except socket.error as e:
			print(e)

	def receive(self):
		try:
			return self.client.recv(2048).decode()
		except socket.error as e:
			print(e)

	def get_pos(self):
		return self.pos