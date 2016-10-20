import subprocess
from multiprocessing.connection import Client


def create_new_console():
	listener = subprocess.Popen(["python", "ipc_listener.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

def main():
	create_new_console()
	
	client = Client(('localhost', 6000), authkey=b"bulb_city")
	
	print()
	
	while True:
		msg = input("[{0:>10}]: ".format("You"))
		client.send(msg)
		
		if msg == "terminate":
			break
	
	return
	
if __name__ == "__main__":
	main()