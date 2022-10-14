#!/usr/bin/env python3

# Function to format DNA string so that each line is no more than 60 NT long
# INPUT: a string of DNA WITHOUT newlines
# OUTPUT: a string of DNA with lines no more than 60 nucleotides long

import re

def sequence_format60(seq):
	seq = re.sub(r"\s","",seq) # make sure there is no white space
	newseq = ""
	for found in re.finditer(r"(\w{1,60})",seq):
		if len(found.group(1)) == 60:
			newseq = newseq + found.group(1) + "\n"
		else:
			newseq = newseq + found.group(1)
	return(newseq)


dna = input("DNA sequence: ")
print(sequence_format60(dna))
