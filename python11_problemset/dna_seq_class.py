#!/usr/bin/env python3

import re

class DNAseq(object):

	# Define attributes
	def __init__(self, seq_name, sequence, species):
		self.seq_name = seq_name
		self.sequence = sequence
		self.species = species

	# Define methods

	# Get sequence length
	def seq_len(self):
		return len(self.sequence)

	# Report nucleotide composition
	def nt_comp(self):
		nt_dict = {"A" : self.sequence.upper().count("A"),
					"T" : self.sequence.upper().count("T"),
					"G" : self.sequence.upper().count("G"),
					"C" : self.sequence.upper().count("C")}
		return nt_dict
	
	# Get GC content
	def gc_content(self):
		g = self.sequence.upper().count("G")
		c = self.sequence.upper().count("C")
		length = len(self.sequence)
		gc = (g + c)/length
		return gc
	
	# Print sequence in FASTA format
	def to_fasta(self):
		print(f'>{self.seq_name} | {self.species}')
		match = r"(\w{1,60})"
		for found in re.finditer(match, self.sequence):
			print(found.group(1))

# Get sequence info from user
sequence_name = input("Sequence name: ")
sequence = input("Sequence: ")
species = input("Species: ")

# Create sequence object
sequence_obj = DNAseq(sequence_name, sequence, species)

# Return info about sequence to stdout
print(f'Sequence name: {sequence_obj.seq_name}')
print(f'Sequence: {sequence_obj.sequence}')
print(f'Species: {sequence_obj.species}')
print(f'Sequence length: {sequence_obj.seq_len()}')
print(f'Nucleotide composition: {sequence_obj.nt_comp()}')
print(f'GC content: {sequence_obj.gc_content():.2%}')
sequence_obj.to_fasta()
