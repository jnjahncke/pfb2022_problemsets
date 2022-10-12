#!/usr/bin/env python3

import random
import sys
seq = sys.argv[1]
seqlist = list(seq)

for i in range(0,len(seq)+1,1):
	posA = random.randrange(0,len(seq))
	posB = random.randrange(0,len(seq))
	while posA == posB:
		posB = random.randrange(0,len(seq))
	ntA = seq[posA]
	ntB = seq[posB]
	seqlist[posA] = ntB
	seqlist[posB] = ntA
	newseq = "".join(seqlist)
print(newseq)
	
		
