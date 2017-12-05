import os
import platform

def detect_os():
	if platform.system() == 'Windows':
		return 'cls'
	else:
		return 'clear'

clear_command = detect_os()
filename = 'tracker.txt'

def main():
	print_header()
	main_logic()

def print_header():
	os.system(clear_command)
	print('####################')
	print('# Gym Tracker v1.0 #')
	print('####################')

def main_logic():
	entries = load()
	opt = None

	while opt != 'x':
		print("Chose one of the following options:")
		opt = input('[G]roup Training * [A]lone Training * [T]otal Points * [S]ave * E[x]it: ')
		opt = opt.lower()
		if opt == 'g':
			print_header()
			print("Group Training added. Good Job!")
			add_event(entries, 6)
		elif opt == 'a':
			print_header()
			print("Self Training added. Way to go!")
			add_event(entries, 3)
		elif opt == 't':
			print_header()
			total_points(entries)
		elif opt == 's':
			print_header()
			print("Data saved.")
			save(entries)
		elif opt != 'x':
			print_header()
			print("Option does not exist. Please try again!")

def add_event(data, points):
	data.append(points)

def total_points(data):
	total = 0
	for entry in data:
		total += entry
	print("You have {} entries so far, with a total of {} points. You are doing great!".format(len(data), total))

def load():
	content = []
	try:
		with open(filename, 'r') as filein:
			content = filein.readlines()
		content = [int(x.strip()) for x in content]
	except IOError:
		pass
	return content

def save(data):
	with open(filename, 'w') as fileout:
		for points in data:
			fileout.write(str(points) + '\n')

if __name__ == '__main__':
	main()
