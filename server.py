import socket
import threading
import pickle
import random as r
from mechanics import Player, Ball


def init():        # INITIAL REQUIREMENTS
	global s

	server = 'my local IP'                         #'0.0.0.0'
	port = 5555
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	try:
		s.bind((server,port))
	except socket.error as e:
		print(e)


	s.listen(2)
	print("Server started, waiting for connection....")

init()

player_ever_joined = False
current_client = 0
ball = Ball()                                                              # Ball initiation
players = [Player((15,175)),Player((685,175))]                             # Player instantiation cum database

def threaded_client(connection,current_client):                             
	if current_client == 0:                                                
		other_player = 1
	else:
		other_player = 0

	send_player = pickle.dumps(players[current_client])                    
	send_other_player = pickle.dumps(players[other_player])
	send_ball = pickle.dumps(ball)                                         
	connection.send(send_player)                                           # send player object to current client
	connection.send(send_other_player)                                     # sending other clients object to current client
	connection.send(send_ball)                                             # send ball object to client

	
	while True:
		data = pickle.loads(connection.recv(2048))

		if len(data)==0:
			print("Disconnected!!")
			break

		else:
			players[current_client] = data                                  # update current client on server

			reply = pickle.dumps(players[other_player])                     # sending other client to current client
			send_ball = pickle.dumps(ball)
			connection.send(reply)
			connection.send(send_ball)

	print(f"Closing connection....{connection.getpeername()}")
	current_client -= 1
	connection.close()


while True:
	conn, addr = s.accept()        
	if addr:                                                            # when client.connect() executes in Network.py
		print("Connnected to :", addr)
		thread = threading.Thread(target=threaded_client, args=(conn,current_client))
		thread.start()
		print("Thread started..[ACTIVE CONNECTIONS] = {}".format(threading.activeCount()-1))
		current_client += 1
		player_ever_joined = True

	if current_client==2:
		ball.move(players)                                    

	if player_ever_joined and current_client==0:              # Close the connection if both clients have disconnected.
		s.close()
		print("Server socket closed!")
