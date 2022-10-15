#!/usr/bin/env python3

import re

def sequence_format(sequence = "", length = 60):
	seq = re.sub(r"\s","",sequence)
	length = int(length)
	newseq = ""
	match = r"(\w{1," + str(length) + r"})"
	for found in re.finditer(match, sequence):
		if len(found.group(1)) == length:
			newseq = newseq + found.group(1) + "\n"
		else:
			newseq = newseq + found.group(1)
	return(newseq)


# Take fasta from user input
fasta_file = input("FASTA file: ")
length = input("Desired sequence length: ")

# Parse FASTA
seq_dict = {}
with open(fasta_file,"r") as fasta_in:
	# Iterate through lines, extract sequence name and sequences
	isseq = 0
	for line in fasta_in:
		line = line.rstrip()
		if len(re.findall(">",line)) > 0: # This is true if it is a header line
			for found in re.finditer(r"^>(.+?)\s",line):
				seqname = found.group(1)
				# If it is a header line, build out the empty dictionary
				seq_dict[seqname] = {"sequence" : "","formatted_seq" : ""}
			isseq = 0
		else: # It is a sequence line
			isseq += 1
			if isseq > 0:
				# Get sequence
				seq_dict[seqname]["sequence"] = seq_dict[seqname]["sequence"] + line

# Loop through sequences, format them as you go
# Write to output FASTA
with open(re.sub("\.fasta",".formatted.fasta",fasta_file),"w") as fasta_out:
	for sequence in seq_dict:
		seq_dict[sequence]["formatted_seq"] = sequence_format(seq_dict[sequence]["sequence"],length)
		fasta_out.write(f'>{sequence}\n')
		fasta_out.write(seq_dict[sequence]["formatted_seq"])
		fasta_out.write("\n")
