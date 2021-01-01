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

def threaded_client(connection):
	connection.send(str.encode("Connected!!"))    # when client.connect() executes in Network.py 

	while True:
		data = connection.recv(2048)

		if not data:
			print("Disconnected!!")
			break
		else:
			reply = data.decode('utf-8')
			print("Received...", reply)
			msg_to_send = 'Fuck Off Bitch!!'
			connection.send(str.encode(msg_to_send))

	print("Closing connection")
	connection.close()


while True:
	conn, addr = s.accept()
	print("Connnected to :", addr)
	_thread.start_new_thread(threaded_client,(conn,))



