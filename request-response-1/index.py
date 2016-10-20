import re
import pprint

def main():
	
	# Read map list from knowledge base
	try:
		with open('knowledge-base.data', 'r') as file:
			data = file.read()
	except Exception as e:
		print("<err>: {}".format(e))
		return

	fa = re.findall(r'\-\s*[\"\'](?P<recv>.*)[\"\']\s*,\s*[\"\'](?P<res>.*)[\"\']', data)
	
	map_list = list(map(lambda x: {'pattern': x[0], 'res': x[1]}, fa))
	
	print()

	while True:
		# Get command and arg from command prompt
		line = input("</>: ")

		m  = re.match('(?P<command>[^\s]*)\s?(?P<arg>.*)?', line)
		gd = m.groupdict()

		command = gd['command']
		arg     = gd['arg']
		
		# Process received command and arg
		if command == 'terminate':
			return
		elif command == 'echo':
			if arg is not None:
				
				for token in map_list:
					if re.match( re.compile(token['pattern']), arg ):
						res = re.sub(token['pattern'], token['res'], gd['arg'])
						print("<bot>: {}".format(res))
						break
				else:
					print("<bot>: I don't understand!'")
		else:
			pass
		print("\n======================")
	return

if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		pass