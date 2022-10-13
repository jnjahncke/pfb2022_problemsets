#!/usr/bin/env python3

with open("Python_06.fasta","r") as fasta_in:
	fastaDict = {}
	isseq = 0
	for line in fasta_in:
		line = line.rstrip()
		if line[0] == ">":
			seqname = line[1:]
			fastaDict[seqname] = ""
			isseq = 0
		else:
			isseq += 1 
			if isseq > 0:
				fastaDict[seqname] = fastaDict[seqname]+line

print(fastaDict)
