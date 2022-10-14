#!/usr/bin/env python3

# Import enzyme list, parse into dictionary: {enzyme : cut site}
import re
enzymelist = {}
with open("enzymes.txt","r") as raw:
	linenum = 0
	for line in raw:
		linenum += 1
		if linenum > 10:
			for found in re.finditer(r"^(\w+\s?\(?.*\)?)\s\s+(.*)",line):
				enzyme = found.group(1).strip()
				site = found.group(2).strip()
				enzymelist[enzyme] = site
			
# Take two inputs from user: enzyme and FASTA file
enzyme = input("Restriction enzyme: ")
fasta = input("FASTA file name: ")		

# If the enzyme is in your dictionary, print:
#	The sequence, annotated with cut site
#	The number of fragments
#	The fragments, unsorted
# 	The fragments, sorted largest to smallest

if enzyme in enzymelist:
	cutseqraw = enzymelist[enzyme]
	cutseqfrags = cutseqraw.split("^")
	cutseq = "".join(cutseqfrags)
	# Print enzyme annotated with cut site
	#	Get sequence from fasta
	seq = ""
	with open(fasta,"r") as fa_in:
		for line in fa_in:
			line = line.rstrip()
			if len(re.findall(">",line)) == 0:
				seq += line
	annotated_seq = re.sub(cutseq,cutseqraw,seq)
	print(annotated_seq)
	# Print number of fragments
	fragments = annotated_seq.split("^")
	print(f'\nNumber of fragments: {len(fragments)}\n')
	# Print the unsorted fragments:
	print("\nUnsorted fragments:")
	fragnum = 0
	for i in fragments:
		fragnum += 1
		print(f'Fragment {fragnum}: {i}')	
	# Print the sorted fragments, large to small
	print("\nSorted fragments:")
	fragments = sorted(fragments, key = len, reverse = True)
	fragnum = 0
	for i in fragments:
		fragnum += 1
		print(f'Fragment {fragnum}: {i}')

else:
	print("Enzyme not in database.")
