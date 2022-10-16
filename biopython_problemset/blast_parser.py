#!/usr/bin/env python3

from Bio import SeqIO
import re

fasta_file = "uniprot_sprot.fasta"

# Extract sequences from uniprot fasta
seqnum_total = 0
seq_dict = {}

for record in SeqIO.parse(fasta_file, "fasta"):
	seqnum_total += 1
	seq_dict[record.name] = {"desc" : record.description, "genus":"", "species":"", "seq":""}
	seq_dict[record.name]["seq"] = record.seq
	for found in re.finditer(r"OS=(\w+) (\w+ \w+)\s", seq_dict[record.name]["desc"]):
		seq_dict[record.name]["genus"] = found.group(1)
		seq_dict[record.name]["species"] = found.group(2)

# Create a dictionary with genus-species pairs and their counts
species_dict = {}
for record in seq_dict:
	genus = seq_dict[record]["genus"]
	species = seq_dict[record]["species"]
	genus_species = genus + " " + species
	if genus_species in species_dict:
		species_dict[genus_species] += 1
	else:
		species_dict[genus_species] = 1

# Print all salmonella paratyphi b entries to a fasta file
with open("salmonella.fasta","w") as salmonella_out:
	sal_num = 0
	for record in seq_dict:
		if seq_dict[record]["genus"] == "Salmonella" and seq_dict[record]["species"] == "paratyphi B":
			sal_num += 1
			salmonella_out.write(f">{record} | {seq_dict[record]['desc']}\n{seq_dict[record]['seq']}\n")
		
# Print sequence counts to stdout
print(f'Total number of sequences: {seqnum_total}')
print(f'Total number of Salmonella paratyphi B sequnces: {sal_num}')
