#!/usr/bin/env python3

import sys
seq = sys.argv[1]


ecorI_seq = "GAATTC"


ecorI_start = seq.find(ecorI_seq)
ecorI_end = seq.find(ecorI_seq) + len(ecorI_seq) - 1

# Print the start and end positions containing the first EcoRI site
# Note that the variables are the python index numbers,
# for "human" numbers, I will add 1
print(f'EcoRI startPos: {ecorI_start+1} endPos: {ecorI_end+1}')
