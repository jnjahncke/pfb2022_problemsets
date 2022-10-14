#!/usr/bin/env python3

# -------------------------------------------------
# Import FASTA file,
# 	Find codons for all 6 reading frames
#		Export to `Python_08.codons-6frames.nt`
#
#	Translate all reading frames
#		Export to `Python_08.translated.aa`
#
#	Find the longest peptide sequence (up to stop)
#	of all 6 reading frames for a single sequence
#		Export the SINGLE longest peptide
#			to `Python_08.translated-longest.aa`
#
#	Determine which set of codons produced the 
#		largest peptide
#		Export to `Python_08.orf-longest.nt`
# -------------------------------------------------

# Take fasta from user input
fasta_file = input("FASTA file: ")

import re

seq_dict = {}
with open(fasta_file,"r") as fasta_in:
	# Iterate through lines, extract sequence name and sequences
	isseq = 0
	for line in fasta_in:
		line = line.rstrip()
		if len(re.findall(">",line)) > 0: # This is true if it is a header line
			for found in re.finditer(r"^>(.+?)\s",line):
				seqname = found.group(1)
				# If it is a header line, build out the empty dictionary
				seq_dict[seqname] = {"seq" : "",
									"seq-rev-comp" : "",
									"codons" : {
										"codons-f1" : [],
										"codons-f2" : [],
										"codons-f3" : [],
										"codons-f4": [],
										"codons-f5" : [],
										"codons-f6" : []},
									"translations" : {
										"trans-f1" : [],
										"trans-f2" : [],
										"trans-f3" : [],
										"trans-f4" : [],
										"trans-f5" : [],
										"trans-f6" : []}}
			isseq = 0
		else: # It is a sequence line
			isseq += 1
			if isseq > 0:
				# Get sequence
				seq_dict[seqname]["seq"] = seq_dict[seqname]["seq"] + line
				# Get reverse complement
				seq_dict[seqname]["seq-rev-comp"] = seq_dict[seqname]["seq-rev-comp"] + line[::-1].lower()
				seq_dict[seqname]["seq-rev-comp"] = seq_dict[seqname]["seq-rev-comp"].replace("a","T")
				seq_dict[seqname]["seq-rev-comp"] = seq_dict[seqname]["seq-rev-comp"].replace("g","C")
				seq_dict[seqname]["seq-rev-comp"] = seq_dict[seqname]["seq-rev-comp"].replace("t","A")
				seq_dict[seqname]["seq-rev-comp"] = seq_dict[seqname]["seq-rev-comp"].replace("c","G")

# Iterate through sequences and extract codons
# 	Write to "Python_08.codons-6frames.nt"
with open("Python_08.codons-6frames.nt","w") as codons_out:
	for sequencename in seq_dict: # iterate through sequences (called by name = sequence):
		# find matches for three letters
		# Iterate through frames of first 3 sequences - forward sequences
		for framenum in range(1,4,1):
			frame = seq_dict[sequencename]["codons"]["codons-f"+str(framenum)]
			# Separate into codons
			for found in re.finditer(r"(\w\w\w)",seq_dict[sequencename]["seq"].upper()):
				# Append to codon dictionary
				frame.append(found.group(1))
			# Write to file
			codons_out.write(f">{sequencename}-frame-{framenum}-codons\n")
			codons_out.write(" ".join(seq_dict[sequencename]["codons"]["codons-f"+str(framenum)]))
			codons_out.write("\n")

		# Iterate through reverse sequences
		for framenum in range(4,7,1):
			frame = seq_dict[sequencename]["codons"]["codons-f"+str(framenum)]
			# Separate into codons
			for found in re.finditer(r"(\w\w\w)",seq_dict[sequencename]["seq-rev-comp"].upper()):
				# Append to codon dictionary
				frame.append(found.group(1))
			# Write to file
			codons_out.write(f">{sequencename}-frame-{framenum}-codons\n")
			codons_out.write(" ".join(seq_dict[sequencename]["codons"]["codons-f"+str(framenum)]))
			codons_out.write("\n")
 
# Translate all 6 reading frames
translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

with open("Python_08.translated.aa","w") as trans_out:
	# Iterate through sequences
	for sequencename in seq_dict:
		framenum = 0
		# Iterate through frames, individual codons in each frame
		for frame in seq_dict[sequencename]["codons"]:
			framenum += 1
			for codon in seq_dict[sequencename]["codons"]["codons-f"+str(framenum)]:
				# Iterate through translation table
				#	IF the codon matches the DNA fragment in the table
				#	replace the codon DNA with the associated AA
				# Append translation to dictionary
				for dna,AA in translation_table.items():
					if dna == codon:
						seq_dict[sequencename]["translations"]["trans-f"+str(framenum)].append(re.sub(dna,AA,codon))
			seq_dict[sequencename]["translations"]["trans-f"+str(framenum)] = "".join(seq_dict[sequencename]["translations"]["trans-f"+str(framenum)])
			# Write to output file
			trans_out.write(f'>{sequencename}-frame-{framenum}-translation\n')
			trans_out.write(seq_dict[sequencename]["translations"]["trans-f"+str(framenum)])
			trans_out.write("\n")

# Find the longest peptide sequence of all 6 translations
#	M = STOP
trans_dict = {}
with open("Python_08.translated-longest.aa","w") as long_out, open("Python_08.orf-longest.nt","w") as longest_NT:
	# Iterate throgh sequences, get actual translations, save to trans_dict
	for sequencename in seq_dict:
		# Build dictionary
		trans_dict[sequencename] = {"trans-f1" : {"translation" : "", "length" : 0},
									"trans-f2" : {"translation":"","length":0},
									"trans-f3" : {"translation":"","length":0},
									"trans-f4" : {"translation":"","length":0},
									"trans-f5" : {"translation":"","length":0},
									"trans-f6" : {"translation":"","length":0}}
		framenum = 0
		# Iterate through all 6 translations
		for translation in seq_dict[sequencename]["translations"]:
			framenum += 1
			seq_dict[sequencename]["translations"]["trans-f"+str(framenum)] = seq_dict[sequencename]["translations"]["trans-f"+str(framenum)].split("M")[0] # Note that this overwrites the translation
			translen = len(seq_dict[sequencename]["translations"]["trans-f"+str(framenum)])
			trans_dict[sequencename]["trans-f"+str(framenum)] = {"translation" : seq_dict[sequencename]["translations"]["trans-f"+str(framenum)],
																	"length" : translen}

	# New for loop: iterate through trans_dict
	# For each sequence, find the longest translation
	# Print in fasta format to Python_08.translated-longest.aa
	for sequencename in trans_dict:
		longest_transname = "trans-f1"
		longest_len = 0
		framenum = 0
		for translation in trans_dict[sequencename]:
			framenum += 1
			if trans_dict[sequencename][translation]["length"] > longest_len:
				longest_transname = "trans-f"+str(framenum) 
				longest_len = trans_dict[sequencename][translation]["length"]
				frame = int(longest_transname[-1]) # frame = the frame containing the longest translation
		long_out.write(f'>{sequencename}-frame-{framenum}-longest-translation\n')
		long_out.write(trans_dict[sequencename][longest_transname]["translation"])
		long_out.write("\n")
		
		# Now that we know which frame is longest
		# Print codons in fasta format to Python_08.orf-longest.nt	
		longest_NT.write(f'>{sequencename}-frame-{frame}-codons-longest translation\n')
		longest_NT.write(" ".join(seq_dict[sequencename]["codons"]["codons-f"+str(frame)]))
		longest_NT.write("\n")
