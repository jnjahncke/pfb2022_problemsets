#!/usr/bin/env python3

import re

def gc_content(seq):
	seq = re.sub("\s","",seq).upper()
	g = seq.count("G")
	c = seq.count("C")
	length = len(re.findall(r"[ACTGN]",seq))
	gc = (g + c)/length
#	return(gc)
	return(f'{gc:.2%}')

dna = input("DNA sequence: ")

print(gc_content(dna))
