import os

def main():
	print_header()
	main_logic()

def print_header():
	os.system('clear')
	print('####################')
	print('# Gym Tracker v1.0 #')
	print('####################')

def main_logic():
	entries = []

	opt = None

	while opt != 'x':
		print("Chose one of the following options:")
		opt = input('[G]roup Training, [S]elf Training, [T]otal Points, E[x]it: ')
		opt = opt.lower()
		if opt == 'g':
			print_header()
			print("Group Training added. Good Job!")
			add_event(entries, 6)
		elif opt == 's':
			print_header()
			print("Self Training added. Way to go!")
			add_event(entries, 3)
		elif opt == 't':
			print_header()
			total_points(entries)
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

if __name__ == '__main__':
	main()
