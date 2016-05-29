from multiprocessing.connection import Listener

def main():	
	listener   = Listener(("localhost", 6000), authkey = b"bulb_city")
	connection = listener.accept()
	
	print()
	
	while True:
		msg = connection.recv()
		print("Receive message: {0}".format(msg)) 
		
		if msg == 'terminate':
			connection.close() 
			break
	return

if __name__ == "__main__":
	main()