#program to search for input in master file, both files are assumed to be tab seperated and can have multiple columns
import sys
import re
import os
#import replace_list   #custom import file for word replacement
from argparse import ArgumentParser

parser = ArgumentParser(description='To find in master file the contents of input file print into matched.txt and not matchedd.txt \n\rBoth files are tab seperated and can have multiple columns'+
						"How to Run?\n" +
						"python3 " + sys.argv[0] + " -i=inputfie"
						)

parser.add_argument("-i", "--input", dest="inputfile",
					help="provide .txt file name",required=True)
#parser.add_argument("-r", "--replace", dest="replaceFlag",
#					help="replace anywhere in the string",required=False)
parser.add_argument("-l", "--masterfile", dest="masterfile",
					help="specify a master file", required=True)
#parser.add_argument("-o", "--outfile", dest="outfile",
#					help="specify output file name", required=True)

args = parser.parse_args()

inputfile = args.inputfile
masterfile = args.masterfile

#open input file using open file mode
fp1 = open(inputfile, encoding="utf-8") # Open file on read mode
inputs = fp1.read().split("\n") # Create a list containing all lines
fp1.close() # Close file

#open list file using open file mode
fp2 = open(masterfile, encoding="utf-8") # Open file on read mode
masters = fp2.read().split("\n") # Create a list containing all lines
fp2.close() # Close file

fw1 = open("result.txt","w", encoding="utf-8")

master_hash1 = {}
master_hash2 = {}

for master in masters:
	if(master == ""):
		continue
	cols = master.strip().split("\t")
	master_hash1[cols[0]] = 1
	master_hash2[cols[1]] = 1

for inp in inputs:
	if(inp == ""):
		continue
	cols = inp.strip().split("\t")
	if(cols[0] in master_hash1):
		fw1.write(inp + "\t" + "1")
	else:
		fw1.write(inp + "\t" + "0")

	if(cols[1] in master_hash2):
		fw1.write("\t" + "1" + "\n")
	else:
		fw1.write("\t" + "0" + "\n")

fw1.close()