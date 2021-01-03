import socket
import pickle

class Network:
	server = '192.168.1.8'
	port = 5555

	def __init__(self):
		self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.addr = (self.server,self.port)
		self.players = self.connect()

	def connect(self):
		self.client.connect(self.addr)
		player1 = self.client.recv(2048)
		player2 = self.client.recv(2048)
		return pickle.loads(player1) , pickle.loads(player2)

	def send(self,data):
		try:
			self.client.send(pickle.dumps(data))
		except socket.error as e:
			print(e)

	def receive(self):
		try:
			return pickle.loads(self.client.recv(2048))
		except socket.error as e:
			print(e)

	def get_players(self):
		return self.players