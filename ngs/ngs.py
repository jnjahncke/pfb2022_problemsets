#!/usr/bin/env python3

from Bio import SeqIO
import re

genome_file = "Ecoli.fasta"
annotation_file = "Ecoli.gff3"

#features = []
#with open(annotation_file,"r") as ann_file:
#	for line in ann_file:
#		if line[0] != "#":
#			features.append(line.split("\t")[0])
#print(set(features))

genome_dict = {}
maxlen = 0
for record in SeqIO.parse(genome_file, "fasta"):
	genome_dict[record.name] = {"length" : len(record.seq)}
	if len(record.seq) > maxlen:
		maxlen = len(record.seq)
		longest_seqname = record.name

print(f'The genome ({longest_seqname}) contains {maxlen} nucleotides.\n')

# Figuring out which Phred quality encoding (ASCII offset) the reads are in
# Every 4th line indicates quality
linenum = 0
qual_raw = ""
with open("SRR21901339.fastq","r") as reads:
	for line in reads:
		linenum += 1
		line = line.rstrip()
		if linenum % 4 == 0:
			qual_raw += line
qual_raw_set = set(qual_raw) # Just extract the characters that are used
qual_to_ASCII = []
# Convert from character to ASCII
for char in qual_raw_set:
	qual_to_ASCII.append(ord(char))
print(f"The phred characters used are: {qual_raw_set}")
print(f"The converted numbers are: {qual_to_ASCII}")
# The minimum ASCII should indicate the offset
print(f"Because the minimum offset is {min(qual_to_ASCII)}, the offset can be assumed to be +33")
