#!/usr/bin/env python3

import re

# Find all the header lines in Python_07.fasta
# If a line is a FASTA header,
#	Extract the sequence name and description

with open("Python_07.fasta","r") as fastafile:
	for line in fastafile:
		line = line.rstrip()
		if len(re.findall(">",line)) > 0:
			for i in re.finditer(">(.+?)\s(.+)",line):
				seqName = i.group(1)
				description = i.group(2)
				print(f'id: {seqName:<30}	desc: {description:<50}')
