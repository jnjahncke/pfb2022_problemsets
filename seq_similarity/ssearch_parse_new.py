#!/usr/bin/env python3

# random seq BLASTP results from fasta.bioch.virginia.edu/mol_evol/data
# 800 AA random protein sequence against the QFO78 library of 78 Uniprot Reference Proteomes

randseq = input("Specify sequence - <rand5-200> or <rand5-800>: ")

matrices = ["BL50","BP62","VT10","VT160","VT20","VT40","VT80"] 

# Extract info from file:
result_dict = {}
for matrix in matrices:
	filename = "ss_" + randseq + "_v_qfo_" + matrix + ".txt"
	with open(filename,"r") as results:
		for line in results:
			line = line.rstrip()
			if line[0] != "#":
				line = line.split("\t")
				result_dict[matrix] = {"sseqid":line[1], "percid":float(line[2]), "alen":int(line[3]), "mismat":line[4], "gaps":line[5], "q_start":line[6], "q_end":line[7], "s_start":line[8], "s_end":line[9], "evalue":line[10], "bits":line[11]}
				break

# Print results: matrix, seq id, percent id, alignment length, e-value for the TOP HIT from each search (smallest e-value)
print(f'{"Matrix":<8}\tPctID\tLen\tE-Value')
for matrix in result_dict:
	print(f'{matrix:<8}\t{result_dict[matrix]["percid"]:.2f}\t{result_dict[matrix]["alen"]}\t{result_dict[matrix]["evalue"]}')
