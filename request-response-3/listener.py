import re
from multiprocessing.connection import Listener, Client

def main():
	listener = Listener(("localhost", 6000), authkey=b"t-bot")

	try:
		connection = listener.accept()
	except Exception as signal:
		signal_emitter.send(signal)
		return

	while True:
		msg = connection.recv()
		print(msg)
	return

if __name__ == "__main__":
	main()