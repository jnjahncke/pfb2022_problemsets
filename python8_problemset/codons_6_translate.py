#!/usr/bin/env python3

# -----------------------------------------------
# Import FASTA file,
# 	Find codons for all 6 reading frames
#		Export to `Python_08.codons-6frames.nt`
#	Translate all reading frames
#		Export to `Python_08.translated.aa`
# -----------------------------------------------

# Take fasta from user input
fasta_file = input("FASTA file: ")

import re

seq_dict = {}
with open(fasta_file,"r") as fasta_in:
	# Iterate through lines, extract sequence name and sequences
	isseq = 0
	for line in fasta_in:
		line = line.rstrip()
		if len(re.findall(">",line)) > 0: 
			for found in re.finditer(r"^>(.+?)\s",line):
				seqname = found.group(1)
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
		else:		
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
	for sequence in seq_dict: # iterate through sequences (called by name = sequence):
		# find matches for three letters
		# first reading frame
		for found in re.finditer(r"(\w\w\w)",seq_dict[sequence]["seq"].upper()):
			seq_dict[sequence]["codons"]["codons-f1"].append(found.group(1)) # save codons to dictionary
		# second reading frame
		for found in re.finditer(r"(\w\w\w)",seq_dict[sequence]["seq"].upper()[1:]):
			seq_dict[sequence]["codons"]["codons-f2"].append(found.group(1))
		# third reading frame
		for found in re.finditer(r"(\w\w\w)",seq_dict[sequence]["seq"].upper()[2:]):
			seq_dict[sequence]["codons"]["codons-f3"].append(found.group(1))
		# fourth reading frame
		for found in re.finditer(r"(\w\w\w)",seq_dict[sequence]["seq-rev-comp"].upper()):
			seq_dict[sequence]["codons"]["codons-f4"].append(found.group(1))
		# fifth reading frame
		for found in re.finditer(r"(\w\w\w)",seq_dict[sequence]["seq-rev-comp"].upper()[1:]):
			seq_dict[sequence]["codons"]["codons-f5"].append(found.group(1))
		# sixth reading frame
		for found in re.finditer(r"(\w\w\w)",seq_dict[sequence]["seq-rev-comp"].upper()[2:]):
			seq_dict[sequence]["codons"]["codons-f6"].append(found.group(1))
	# write to output file
		codons_out.write(f'{sequence}-frame-1-codons\n')
		codons_out.write(" ".join(seq_dict[sequence]["codons"]["codons-f1"]))
		codons_out.write("\n")
		codons_out.write(f'{sequence}-frame-2-codons\n')
		codons_out.write(" ".join(seq_dict[sequence]["codons"]["codons-f2"]))
		codons_out.write("\n")		
		codons_out.write(f'{sequence}-frame-3-codons\n')
		codons_out.write(" ".join(seq_dict[sequence]["codons"]["codons-f3"]))
		codons_out.write("\n")
		codons_out.write(f'{sequence}-frame-4-codons\n')
		codons_out.write(" ".join(seq_dict[sequence]["codons"]["codons-f4"]))
		codons_out.write("\n")
		codons_out.write(f'{sequence}-frame-5-codons\n')
		codons_out.write(" ".join(seq_dict[sequence]["codons"]["codons-f5"]))
		codons_out.write("\n")		
		codons_out.write(f'{sequence}-frame-6-codons\n')
		codons_out.write(" ".join(seq_dict[sequence]["codons"]["codons-f6"]))
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
	for sequencename in seq_dict:
		framenum = 0
		for frame in seq_dict[sequencename]["codons"]:
			framenum += 1
			for codon in seq_dict[sequencename]["codons"]["codons-f"+str(framenum)]:
				for dna,AA in translation_table.items():
					if dna == codon:
						seq_dict[sequencename]["translations"]["trans-f"+str(framenum)].append(re.sub(dna,AA,codon))
			seq_dict[sequencename]["translations"]["trans-f"+str(framenum)] = "".join(seq_dict[sequencename]["translations"]["trans-f"+str(framenum)])
			trans_out.write(f'{sequencename}-frame-{framenum}-translation\n')
			trans_out.write(seq_dict[sequencename]["translations"]["trans-f"+str(framenum)])
			trans_out.write("\n")
