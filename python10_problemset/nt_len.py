#!/usr/bin/env python3

# Function to format DNA string
# INPUT: a string of DNA WITHOUT newlines
#	AND a desired line length
# OUTPUT: a string of DNA with lines no more than 60 nucleotides long

import re

def sequence_format(seq = "",length = 60):
	seq = re.sub(r"\s","",seq) # make sure there is no white space
	length = int(length)
	newseq = ""
	match = r"(\w{1," + str(length) + r"})"
	for found in re.finditer(match, seq):
		if len(found.group(1)) == length:
			newseq = newseq + found.group(1) + "\n"
		else:
			newseq = newseq + found.group(1)
	return(newseq)


dna = input("DNA sequence: ")
length = input("Desired length: ")
print(sequence_format(dna, length))
