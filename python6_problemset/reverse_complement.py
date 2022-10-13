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
	# iterate through lines of file
	for line in seqset:
		line = line.rstrip() # strip whitespace on the end of the line
		seqname,seq = line.split() # split at whitespace into list
		# make complement
		seq = seq.lower()
		seq = seq.replace('a','T')
		seq = seq.replace('t','A')
		seq = seq.replace('g','C')
		seq = seq.replace('c','G')
		# make into fasta format and reverse it
		fasta += "\n>" + seqname + "\tReverse complement\n" + seq[::-1]
print(fasta)
