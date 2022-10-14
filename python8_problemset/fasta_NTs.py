#!/usr/bin/env python3

# Take fasta file, calculate nucleotide composition for each sequence
# dictionary:  {seqname : {seq : sequence, NT : {ACTG : count} }  }

import re

seq_dict = {}
with open("Python_08.fasta","r") as fasta_in:
	isseq = 0
	for line in fasta_in:
		line = line.rstrip()
		if len(re.findall(">",line)) > 0: 
			for found in re.finditer(r"^>(.+?)\s",line):
				seqname = found.group(1)
				seq_dict[seqname] = {"seq" : "",
									 "NTs" : {"A":0,"T":0,"G":0,"C":0}}
			isseq = 0
		else:		
			isseq += 1
			if isseq > 0:
				seq_dict[seqname]["seq"] = seq_dict[seqname]["seq"] + line
				seq_dict[seqname]["NTs"]["A"] += line.upper().count("A")
				seq_dict[seqname]["NTs"]["T"] += line.upper().count("T")
				seq_dict[seqname]["NTs"]["G"] += line.upper().count("G")
				seq_dict[seqname]["NTs"]["C"] += line.upper().count("C")


print(seq_dict["c0_g1_i1"])
				
		
