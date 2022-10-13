#!/usr/bin/env python3

# In Python_07_nobody.txt
#	Find every occurrence of 'Nobody'
#	Print out the position

import re

linenum = 0
positions = []
with open("Python_07_nobody.txt","r") as nobody:
	
	for line in nobody:
		linenum += 1
		line = line.rstrip()
		for instance in re.finditer(r"(Nobody)",line):
			start = instance.start(1)+1
			positions.append([linenum,start])


print("Here are all of the instances of 'Nobody' in Nobody by Shel Silverstein and the positions of each instance. Positions are represented as [line number, character number].")
print(positions)
		
