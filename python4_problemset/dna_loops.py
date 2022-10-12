#!/usr/bin/env python3

# Iterate through list,
# print out each element
# print the length of the sequence, separated by a tab

seqlist = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for seq in seqlist:
	print(f'{len(seq)}	{seq}')
