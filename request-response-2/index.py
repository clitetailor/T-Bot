import re
import pprint

def main():
	
	print()

	while True:
		
		# Read map list from knowledge base
		try:
			with open('knowledge-base.data', 'r') as file:
				data = file.read()
		except Exception as e:
			print("<err>: {}".format(e))
			return

		fa = re.findall(r'\-\s*[\"\'](?P<recv>.*)[\"\']\s*,\s*[\"\'](?P<res>.*)[\"\']', data)
		
		map_list = list(map(lambda x: {'pattern': x[0], 'res': x[1]}, fa))
		
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

						for another_token in map_list:
							if (another_token is not token
							and re.match( re.compile(another_token['pattern']), arg )
							and re.match( re.compile(token['pattern']), another_token['pattern'])):
								break
						else:
							res = re.sub(token['pattern'], token['res'], arg )
							print("<bot>: {}".format(res))
		else:
			pass
		print("\n======================")
	return

if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		pass