#!/usr/bin/env python3

from Bio.Seq import Seq
from Bio import SeqIO
import re

# Create sequence object
seqobj = Seq("ATGCGATCGAGC")

# Print the sequence
print(seqobj)

# Translate the sequence
protein = seqobj.translate()
print(protein)

# Print out codons
for codon in re.findall(r"(\w{3})", str(seqobj)):
	print(codon)


# Read a FASTA file
for seq_record in SeqIO.parse("./single_seq.fasta", "fasta"):
	print("ID",seq_record.id)
	print("Sequence",seq_record.seq)
	print("Length",len(seq_record))
