#!/usr/bin/env python3

# random seq BLASTP results from fasta.bioch.virginia.edu/mol_evol/data
# 800 AA random protein sequence against the QFO78 library of 78 Uniprot Reference Proteomes

randseq = input("Specify sequence - <rand5-200> or <rand5-800>: ")
print("Comparinng matrices: BLOSUM62, BLOSUM80, PAM30, PAM70...")

matrices = ["BLOSUM62", "BLOSUM80", "PAM30", "PAM70"]

# Extract info from file:
result_dict = {}
for matrix in matrices:
	resultnum = 0
	matrix_dict = {}
	filename = "blast_" + randseq + "_v_qfo_" + matrix + ".txt"
	with open(filename,"r") as results:
		for line in results:
			line = line.rstrip()
			if line[0] != "#":
				resultnum += 1
				line = line.split("\t")
				matrix_dict["hit"+str(resultnum)] = {"sseqid":line[1], "percid":line[2], "alen":line[3], "mismat":line[4], "gaps":line[5], "q_start":line[6], "q_end":line[7], "s_start":line[8], "s_end":line[9], "evalue":line[10], "bits":line[11]}
	result_dict[matrix] = matrix_dict

# Extract top hits
top_dict = {}
for matrix in result_dict:
	minE = 1000000000
	sseqid = ""
	percid = 0
	alen = 0
	for hit in result_dict[matrix]:
		if float(result_dict[matrix][hit]["evalue"]) < minE:
			minE = float(result_dict[matrix][hit]["evalue"])
			sseqid = result_dict[matrix][hit]["sseqid"]
			percid = float(result_dict[matrix][hit]["percid"])
			alen = int(result_dict[matrix][hit]["alen"])
	top_dict[matrix] = {"sseqid":sseqid, "percid":percid, "alen":alen, "evalue":minE}

# Print results: matrix, seq id, percent id, alignment length, e-value for the TOP HIT from each search (smallest e-value)
print(f'{"Matrix":<8}\tPctID\tLen\tE-Value')
for matrix in top_dict:
	print(f'{matrix:<8}\t{top_dict[matrix]["percid"]:.2f}\t{top_dict[matrix]["alen"]}\t{top_dict[matrix]["evalue"]}')
