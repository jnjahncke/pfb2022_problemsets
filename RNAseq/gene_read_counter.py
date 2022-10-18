#!/usr/bin/env python3

import sys

## Read bowtie2.sam and generate a table containing the number of reads mapped to each gene

# Get file name
sam_file = sys.argv[1]

# Iterate through lines
#	Get gene name
#	Count number of reads for that gene
gene_counts = {}
reads = []
with open(sam_file, "r") as mapped:
	for line in mapped:
		line = line.rstrip()
		gene_name = line.split("\t")[2]
		gene_name = gene_name.split("^")[0]
		readID = line.split("\t")[0]
		if readID not in reads: # Only count each read once per gene
			reads.append(readID)
			if gene_name not in gene_counts:
				gene_counts[gene_name] = 1
			else:
				gene_counts[gene_name] += 1
			
for k,v in gene_counts.items():
	print(f'{k:<11} {v:>6}')
