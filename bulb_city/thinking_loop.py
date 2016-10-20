import threading
import queue
import json
import time
import csv

class ThinkingLoop(object):
	def __init__(self):
		self.bulbs = []
		self.threads = []
		self.nervous = False
		return

	def build(self):
		self.bulbs.append(threading.Semaphore(0))
		self.bulbs.append(threading.Semaphore(0))

		thread1 = threading.Thread(target = self.conductAndRelease, args = (0, 1))
		thread1.start()
		thread2 = threading.Thread(target = self.conductWithCondition, args = (1, 0))
		thread2.start()
		return

	def conductWithCondition():
		while True:
			self.bulbs[source].acquire()
			if self.nervous == False:
				continue
			self.bulbs[dest].release()
		return

	def conductAndRelease(self, source, dest):
		while True:
			self.bulbs[source].acquire()
			self.bulbs[dest].release()
		return
	
	def trigger(self):
		self.nervous = True
		self.bulbs[0].release()
		return

	def stop(self):
		self.nervous = False
		return

	def mount(self, bulb):
		this.bulbs.append(bulb)

	def get(self, id):
		return bulbs[id]