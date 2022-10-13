#!/usr/bin/env python3

# Open Python_06.seq.txt
# Print out the reverse complement
# Note: each line is in the following format:
#	seqName\tsequence\n
# Make sure to print in fasta format
#	including sequence name and note that it is rev complement
# PRINT TO STDOUT

fasta = ""
with open("Python_06.seq.txt","r") as seqset:
	for line in seqset:
		line = line.rstrip()	
		seqname,seq = line.split()
		fasta += "\n>" + seqname + "\n" + seq
print(fasta) # STILL NEED TO MAKE REV COMP
