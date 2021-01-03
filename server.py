import socket
import _thread
import pickle
from Player import Player


def init():        # INITIAL REQUIREMENTS
	global s

	server = '192.168.1.8'
	port = 5555
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	try:
		s.bind((server,port))
	except socket.error as e:
		print(e)


	s.listen(2)
	print("Server started, waiting for connection....")

init()

current_client = 0
players = [Player((15,175)),Player((685,175))]                             # Player instantiation

def threaded_client(connection,current_client):                            # when client.connect() executes in Network.py 
	if current_client == 0:                                                
		other_player = 1
	else:
		other_player = 0

	send_player = pickle.dumps(players[current_client])                    
	send_other_player = pickle.dumps(players[other_player])
	connection.send(send_player)
	connection.send(send_other_player)                                     # sending other clients object to current client

	
	while True:
		data = connection.recv(2048)                 

		if not data:
			print("Disconnected!!")
			break
		else:
			data = pickle.loads(data) 
			players[current_client] = data                                  # update current client on server

			reply = pickle.dumps(players[other_player])                     # sending other client to current client
			connection.send(reply)

	print(f"Closing connection....{connection.getpeername()}")
	connection.close()


while True:
	conn, addr = s.accept()
	if addr:
		print("Connnected to :", addr)
		_thread.start_new_thread(threaded_client,(conn,current_client))
		current_client += 1



