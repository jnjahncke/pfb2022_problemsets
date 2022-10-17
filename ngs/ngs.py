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

print(f'The genome ({longest_seqname}) contains {maxlen} nucleotides.')
