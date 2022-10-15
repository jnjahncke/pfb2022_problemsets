#!/usr/bin/env python3

import re

def reverse_complement(seq):
	seq = re.sub("\s","",seq).lower()
	newseq = seq[::-1]
	newseq = re.sub("a","T",newseq)
	newseq = re.sub("c","G",newseq)
	newseq = re.sub("g","C",newseq)
	newseq = re.sub("t","A",newseq)
	return(newseq)

dna = input("DNA sequence: ")
print(reverse_complement(dna))
