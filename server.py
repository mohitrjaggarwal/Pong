import socket
import _thread


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

def read_pos(arr):
	arr = arr.split(",")
	return int(arr[0]) , int(arr[1])

def make_pos(tup):
	return str(tup[0]) + "," + str(tup[1])


current_client = 0
client_pos = [(15,175),(685,175)]                                          # starting position of clients

def threaded_client(connection,current_client):                            # when client.connect() executes in Network.py 
	if current_client == 0:                                                
		other_player_pos = 1
	else:
		other_player_pos = 0

	send_start_pos = make_pos(client_pos[current_client])                  # "15,175"
	send_other_player_pos = make_pos(client_pos[other_player_pos])         
	connection.send(str.encode(send_start_pos))
	connection.send(str.encode(send_other_player_pos))                     # sending other clients position to current client

	
	while True:
		data = connection.recv(2048).decode()                  

		if not data:
			print("Disconnected!!")
			break
		else:
			data = read_pos(data) 
			client_pos[current_client] = data                               # update current clients pos on server

			reply = client_pos[other_player_pos]                            # sending other client pos to current client
			# print("Received...", data)
			# print("Sending....", reply)
			connection.send(str.encode(make_pos(reply)))

	print(f"Closing connection....{connection.getpeername()}")
	connection.close()


while True:
	conn, addr = s.accept()
	if addr:
		print("Connnected to :", addr)
		_thread.start_new_thread(threaded_client,(conn,current_client))
		current_client += 1



