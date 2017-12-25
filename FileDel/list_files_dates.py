"""File Dates
Lists all files included as separate lines in a txt file given as an argument and their 
last modified datetime

ex. # python3 del_files.py list.txt

"""
import sys
import os
import datetime

filename = sys.argv[1]

with open(filename, 'r') as filein:
    files = filein.readlines()
    files = [x.strip() for x in files]

for file in files:
    if os.path.isfile(file):
        print(file+','+datetime.datetime.fromtimestamp(int(os.path.getmtime(file))).strftime('%Y-%m-%d'))
    else:
        print(file+',NotFound')
