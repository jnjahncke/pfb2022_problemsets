#!/usr/bin/env python3

# Take fasta from user input
fasta_file = input("FASTA file: ")

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
									 "codons-f1" : [],
									"codons-f2" : [],
									"codons-f3" : [] } # Create empty lists for codons
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
		# first reading frame
		for found in re.finditer(r"(\w\w\w)",seq_dict[sequence]["seq"].upper()):
			seq_dict[sequence]["codons-f1"].append(found.group(1)) # save codons
		# second reading frame
		for found in re.finditer(r"(\w\w\w)",seq_dict[sequence]["seq"].upper()[1:]):
			seq_dict[sequence]["codons-f2"].append(found.group(1)) # save codons
		# third reading frame
		for found in re.finditer(r"(\w\w\w)",seq_dict[sequence]["seq"].upper()[2:]):
			seq_dict[sequence]["codons-f3"].append(found.group(1)) # save codons
	# write to output file
		codons_out.write(f'{sequence}-frame-1-codons\n')
		codons_out.write(" ".join(seq_dict[sequence]["codons-f1"]))
		codons_out.write("\n")
		codons_out.write(f'{sequence}-frame-2-codons\n')
		codons_out.write(" ".join(seq_dict[sequence]["codons-f2"]))
		codons_out.write("\n")		
		codons_out.write(f'{sequence}-frame-3-codons\n')
		codons_out.write(" ".join(seq_dict[sequence]["codons-f3"]))
		codons_out.write("\n")
