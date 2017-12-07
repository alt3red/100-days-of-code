"""Delete Files
The following script will delete all files included as separate lines in a txt
file given as an argument

ex. # python3 del_files.py list.txt

"""
import sys
import os
# read filename as argument
filename = sys.argv[1]

# read file and create a list of files to be deleted
with open(filename, 'r') as filein:
    files = filein.readlines()
    files = [x.strip() for x in files]

# go through the list and delete files if they exist
for file in files:
    if os.path.isfile(file):
        print('Deleting {}!'.format(file))
        os.remove(file)
    else:
        print('No Such File ({})!'.format(file))
