#!/usr/bin/env python3

# Open fastq file
# Report:
#	Total number of lines
#	Total number of characters
#	Average line length

linenum = 0
charnum = 0
with open("Python_06.fastq", "r") as seq:
	
	for line in seq:
		line = line.rstrip()
		linenum += 1
		charnum += len(line)

print(f'''
Number of lines = {linenum}
Number of characters = {charnum}
Average line length = {charnum/linenum}
''')
