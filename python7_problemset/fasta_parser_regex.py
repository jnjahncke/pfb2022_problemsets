#!/usr/bin/env python3

import re

# Create dictionary: {header, sequence}
with open("Python_07.fasta","r") as fasta_in:
	fastaDict = {}
	isseq = 0
	for line in fasta_in:
		line = line.rstrip()
		if len(re.findall(">",line)) > 0: 
			seqname = line[1:]
			fastaDict[seqname] = ""
			isseq = 0
		else:
			isseq += 1 
			if isseq > 0:
				fastaDict[seqname] = fastaDict[seqname]+line

for k,v in fastaDict.items():
	print(k + "\n" + v)
