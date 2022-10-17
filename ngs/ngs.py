#!/usr/bin/env python3

from Bio import SeqIO
import re
import sys

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


# Trim poor-quality bases from the ends of the FASTQ sequences and output new FASTQ
file_in = sys.argv[1]
threshold = int(sys.argv[2])

with open(file_in,"r") as reads, open(file_in[:-6]+"_qc.fastq","w") as fastq_out:
	linenum = 0
	for line in reads:
		linenum += 1
		start_1 = ""
		read_2 = ""
		plus_3 = ""
		qual_4 = ""
		qual_trans = ""
		qual_list = []
		line = line.rstrip()
		if line[0] == "@":
			start_1 = line
		if linenum % 2 == 0 and linenum % 4 != 0:
			read_2 = line
		if line[0] == "+":
			plus_3 = line
		else:
			qual_4 = line
			qual_4_temp = list(line)
			for char in qual_4_temp:
				if ord(char)-33 > threshold:
					qual_list.append(ord(char))
			qual_len = len(qual_list)*(-1)
		fastq_out.write(f'''{start_1}
{read_2[:qual_len]}
{plus_3}
{qual_4[:qual_len]}''')
