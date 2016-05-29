from multiprocessing.connection import Client

def main():
	client = Client(('localhost', 6000), authkey = b'bulb_city')
	
	print()
	
	while True:
		msg = input("Enter message: ")
		client.send(msg)
		
		if msg == "terminate":
			break
	return
	
if __name__ == "__main__":
	main()