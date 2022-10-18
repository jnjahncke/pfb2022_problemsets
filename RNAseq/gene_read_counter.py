#!/usr/bin/env python3

import sys
import re

## Read bowtie2.sam and generate a table containing the number of reads mapped to each gene

# Get file name
sam_file = sys.argv[1]

# Iterate through lines
#	Get gene name
#	Count number of reads for that gene
gene_counts = {}
with open(sam_file, "r") as mapped:
	for line in mapped:
		line = line.rstrip()
		for found in re.finditer(r"\s([!-~]+?)\^", line):
			gene_name = found.group(1)
		if gene_name not in gene_counts:
			gene_counts[gene_name] = 1
		else:
			gene_counts[gene_name] += 1

for k,v in gene_counts.items():
	print(f'{k:<8} {v:>6}')
