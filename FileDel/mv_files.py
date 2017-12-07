"""Move Files
The following script will move all files included as separate lines in a txt
file given as an argument[1] to a folder given as argument[2]

ex. # python3 mv_files.py list.txt /tmp/tmp

"""
import os
import sys

# get arguments from command line
# assumes arguments are given
filename = sys.argv[1]
folder = sys.argv[2]

# read the file and put all filenames in a list
with open(filename, 'r') as filein:
    files = filein.readlines()
    files = [x.strip() for x in files]

# check if the destination folder exists and creates it if not
if not os.path.exists(folder):
    print('Folder ({}) does not exist, creating it!'.format(folder))
    os.makedirs(folder)

# goes through the list of files and moves them
for file in files:
    if os.path.isfile(file):
        print('Moving {} to {}!'.format(file, folder+'/'+os.path.basename(file)))
        os.replace(file, folder+'/'+os.path.basename(file))
    else:
        print('No Such File ({})!'.format(file))
