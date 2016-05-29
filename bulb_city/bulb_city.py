import threading
import queue
import json
import time
import pprint
import csv



class BulbCity(object):
	
	def __init__(self):
		self.bulb = []
		self.queue = queue.Queue()
		self.threads = []
		self.electricity = threading.Event()
		self.thread_num = 0
		return
	
	def load_json(self, file_name):
		with open(file_name) as data_file:
			self.graph_info = json.load(data_file)
		return
		
	def load_csv(self, file_name):
		with open(file_name) as data_file:
			data = csv.reader(data_file, quotechar = "\'")
			
			line = list(data)
			
			self.graph_info = dict()
			self.graph_info["vertices"] = int(line[0][0])
			edges = []
			
			for row in line[1:]:
				edge = {"source": int(row[0]), "dest": int(row[1])}
				edges.append(edge)
			
			self.graph_info["edges"] = edges
		return
	
	def build(self):
		vertices = self.graph_info["vertices"]
		
		for i in range(vertices):
			new_bulb = threading.Semaphore(0)
			self.bulb.append(new_bulb)
		
		edges = self.graph_info["edges"]
		
		self.electricity.set()
		
		lightup = threading.Thread(target = self.lightup)
		lightup.start()
		
		self.threads.append(lightup)
		for i in range(len(edges)):
			source = edges[i]["source"]
			dest = edges[i]["dest"]
			new_thread = threading.Thread(target = self.conduct, args = (source, dest))
			new_thread.start()
			self.threads.append(new_thread)
		return
	
	def lightup(self):
		while self.electricity.is_set():
			
			if self.queue.empty():
				print()
				time.sleep(0.8)
			
			item = self.queue.get()
			print("{0:<3}".format(item), end=' ')
			self.queue.task_done()
		return
	
	def conduct(self, source, dest):
		while self.electricity.is_set():
			self.bulb[source].acquire()
			
			self.queue.put(dest)
			time.sleep(1)
			
			self.bulb[dest].release()
		return
	
	def supply(self, list):
		self.thread_num = len(list)
		
		for i in list:
			self.bulb[i].release()
		return
	
	def power_cut(self):
		self.electricity.clear()
		for bulb in self.bulb:
			bulb.release()
		
		for thread in self.threads:
			thread.join()
		return
		
# End # BulbCity

def main():
	try:
		bulb_city = BulbCity()
	
		bulb_city.load_csv("city_graph.csv")
		bulb_city.build()
	
		bulb_city.supply([1])
		
		try:
			while True:
				time.sleep(1)
		except KeyboardInterrupt:
			bulb_city.power_cut()
			print()
			print("Keyboard Interrupt!")
			print()
			
	except Exception as e:
		print()
		print(e)
		print()
		
	return

if __name__ == "__main__":
	main()
		