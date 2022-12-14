#!/usr/bin/env python3

# Iterate through list,
# print out each element
# print the length of the sequence, separated by a tab

seqlist = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

pos = 1
for seq in seqlist:
	print(f'{pos}	{len(seq)}	{seq}')
	pos += 1


print('\n\n') # whitespace


# Generate a list of tuples containing sequences and lengths from seqlist
seqlist_tup = []
for seq in seqlist:
	seqlen = len(seq)
	temp = (seqlen, seq)
	seqlist_tup.append(temp)
print(seqlist_tup)

