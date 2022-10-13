#!/usr/bin/env python3

# Substitute every occurrence of 'Nobody' with a new name

import re

newpoem = ""
with open("Python_07_nobody.txt","r") as nobody, open("Python_07_somebody.txt","w") as somebody:

	for line in nobody:
		line = line.rstrip()
		if re.search(r"Nobody",line):
			newline = re.sub(r"Nobody", "Somebody", line)
			somebody.write(newline + "\n")
		else:
			somebody.write(line + "\n")	
