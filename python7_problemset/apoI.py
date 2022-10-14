#!/usr/bin/env python3

# ApoI cut site: R^AATTY
# 	R = A/G
# 	Y = C/T


# Extract sequence from fasta
import re
seq = ""
with open("Python_07_ApoI.fasta","r") as raw:
	for line in raw:
		line = line.rstrip()
		if len(re.findall(">",line)) == 0:
			seq += line

# Determine physical cut sites
sites = 0
locations = []
for found in re.finditer(r"([AG]AATT[CT])", seq):
	sites += 1
	site = found.start(1)+1
	locations.append(site)
print(f'The cut sites are located at positions: {locations}')

# Print out sequence with "^" at the cut site
cutseq = re.sub(r"([AG])AATT([CT])",r"\1^AATT\2", seq)
print(cutseq)

# Determine the length of the digested fragments
#	Cut fragment at cut site
fragments = cutseq.split("^")
# 	Sort large to small
fragments = sorted(fragments,key = len, reverse = True)
# Print fragment length and fragment
for frag in fragments:
	print(f'{len(frag):<6}	{frag:<}')
