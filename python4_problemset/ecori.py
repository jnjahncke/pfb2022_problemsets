#!/usr/bin/env python3

import sys
seq_raw = sys.argv[1].upper()

ecorI = 'GAATC'
ecorI_cut = 'G^AATC'

if ecorI in seq_raw:
	seq = seq_raw.split(ecorI)
	seq.insert(1, ecorI_cut)
	seq = "".join(seq)
	seq_cut = seq.split("^")
	
	# Sort fragments from large to small
	seq_cut = sorted(seq_cut, key = len, reverse = True)
	
	for frag in seq_cut:
		start = seq_raw.find(frag) #INDEX of start pos
		fraglen = len(frag) # length of fragment
		end = start + fraglen - 1 #INDEX of end pos
		print(f'''Fragment: {frag}
Start position: {start+1}
End position: {end+1}
Fragment length: {fraglen}\n''')

else:
	print("There is no EcoRI cut site in this sequence.")
