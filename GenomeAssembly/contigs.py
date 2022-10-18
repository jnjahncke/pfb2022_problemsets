#!/usr/bin/env python3

import re

contig_file = "ecoli_0.25.contigs.fasta"

total_num_contig = 0
contig_dict = {}
with open(contig_file,"r") as contigs:
	isseq = 0
	for line in contigs:
		line = line.rstrip()
		if len(re.findall(">",line)) != 0:
			total_num_contig += 1
			for found in re.finditer(r">([!-~]+)\s",line):
				seqname = found.group(1)
				contig_dict[seqname] = {"seq":"", "len":0}
		else:
			isseq += 1
			if isseq > 0:
				contig_dict[seqname]["seq"] += line
				contig_dict[seqname]["len"] += len(line)

print(f'Total number of contigs: {total_num_contig}')
genome = 0
# What is the shortest/longest contig?
shortest = {"seqname":"","seq":"","len":10000000}
longest = {"seqname":"","seq":"","len":0}
for contig in contig_dict:
	# genome size
	genome += contig_dict[contig]["len"]
	# longest
	if contig_dict[contig]["len"] > longest["len"]:
		longest["seqname"] = contig
		longest["seq"] = contig_dict[contig]["seq"]
		longest["len"] = contig_dict[contig]["len"]
	# shortest
	if contig_dict[contig]["len"] < shortest["len"]:
		shortest["seqname"] = contig
		shortest["seq"] = contig_dict[contig]["seq"]
		shortest["len"] = contig_dict[contig]["len"]
print(f'Shortest contig: {shortest["seqname"]}, {shortest["len"]}')
print(f'Longest contig: {longest["seqname"]}, {longest["len"]}')

# What is N50 & L50?
#	Sort largest to smallest
#	N50: 50% of contigs are as long or longer than N50 (length in bp)
#	L50: Number of contigs that are as long or longer than N50
genome50 = genome/2
lengths = []
for contig in contig_dict:
	lengths.append(contig_dict[contig]["len"])
lengths = sorted(lengths)[::-1] # sort largest to smallest
len_sum = 0
upper50 = []
# Iterate through lengths, large to small.
# If the rolling sum is less that 50% of the genome:
#	Add current length to new list upper50
for i in lengths:
	if len_sum <= genome50:
		len_sum += i
		upper50.append(i)
N50 = upper50[-1] # N50 is the smallest item in the list (last item)
L50 = len(upper50) # L50 is the length of the list
print(f'N50: {N50/1000:.1f} kbp\nL50: {L50} contigs')
