#!/usr/bin/env python3

# Input two sequences (name, sequence, species)
# Return True if all THREE are the same for both sequences

import re

class DNAseq(object):

	# Define attributes
	def __init__(self, seq_name, sequence, species):
		self.seq_name = seq_name,
		self.sequence = sequence,
		self.species = species

class DNAcomp(object):
	def __init__(self, sequence1_obj, sequence2_obj):
		self.sequence1 = sequence1_obj
		self.sequence2 = sequence2_obj

	def seq_compare(self):
		# Compare two sequence objects
		if self.sequence1.seq_name == self.sequence2.seq_name:
			name_same = True
		else:
			name_same = False
		if self.sequence1.sequence == self.sequence2.sequence:
			seq_same = True
		else:
			seq_same = False
		if self.sequence1.species == self.sequence2.species:
			species_same = True
		else:
			species_same = False

		# Print True only if all three are the same
		if name_same == True & seq_same == True & species_same == True:
			return(True)
		else:
			return(False)

# Get the two sequences
#	for practice: sequence1.txt == sequence2.txt != sequence3.txt
seq1_file = input("File for first sequence: ")
seq2_file = input("File for second sequence: ")

# Get two sequences from files input by user
# Assuming files are in the following format:
# >SequenceName Species
# Sequence
with open(seq1_file, "r") as seq1_read, open(seq2_file, "r") as seq2_read:
	for line in seq1_read:
		if line[0] == ">":
			for found in re.finditer(">(\w+?)\s(.+)", line):
				seq_name1 = found.group(1)
				species1 = found.group(2)
		else:
			sequence1 = line

	for line in seq2_read:
		if line[0] == ">":
			for found in re.finditer(">(\w+?)\s(.+)", line):
				seq_name2 = found.group(1)
				species2 = found.group(2)
		else:
			sequence2 = line

# Compare the two sequences
seq1_obj = DNAseq(seq_name1, sequence1, species1)
seq2_obj = DNAseq(seq_name2, sequence2, species2)

comp_obj = DNAcomp(seq1_obj, seq2_obj)
print(comp_obj.seq_compare())
