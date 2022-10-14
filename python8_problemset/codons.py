#!/usr/bin/env python3

# Take fasta from user input
#fasta_input = input("FASTA file: ")
fasta_file = "Python_08.fasta"

import re

seq_dict = {}
with open(fasta_file,"r") as fasta_in:
	# Iterate through lines, extract sequence name and sequences
	isseq = 0
	for line in fasta_in:
		line = line.rstrip()
		if len(re.findall(">",line)) > 0: 
			for found in re.finditer(r"^>(.+?)\s",line):
				seqname = found.group(1)
				seq_dict[seqname] = {"seq" : "",
									 "codons" : [] } # Create empty list for codons
			isseq = 0
		else:		
			isseq += 1
			if isseq > 0:
				seq_dict[seqname]["seq"] = seq_dict[seqname]["seq"] + line

# Iterate through sequences and extract codons
# 	Write to "Python_08.codons-3frames.nt"
with open("Python_08.codons-3frames.nt","w") as codons_out:
	for sequence in seq_dict: # iterate through sequences (called by name = sequence):
		 # find matches for three letters
		for found in re.finditer(r"(\w\w\w)",seq_dict[sequence]["seq"].upper()):
			seq_dict[sequence]["codons"].append(found.group(1)) # save codons
		# write to output file
		codons_out.write(f'{sequence}-frame-1-codons\n')
		codons_out.write(" ".join(seq_dict[sequence]["codons"]))
		codons_out.write("\n")
