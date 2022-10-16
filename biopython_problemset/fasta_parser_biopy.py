#!/usr/bin/env python3

from Bio import SeqIO
from Bio.Seq import Seq
import re

# Get FASTA file from input
fasta_file = input("FASTA File: ")

# Extract sequences
seqnum_total = 0
ntnum_total = 0
seq_lengths = []
gc_contents = []

for record in SeqIO.parse(fasta_file, "fasta"):
	seqnum_total += 1
	ntnum_total += len(record.seq)
	seq_lengths.append(len(record.seq))
	g = record.seq.upper().count("G")
	c = record.seq.upper().count("C")
	gc_contents.append((g+c)/len(record.seq))

print(f'''sequence count: {seqnum_total}
total number of nucleotides: {ntnum_total}
avg len: {ntnum_total/seqnum_total:.2f}
shortest len: {min(seq_lengths)}
longest len: {max(seq_lengths)}
avg GC content: {sum(gc_contents)/seqnum_total:.2%}
lowest GC content: {min(gc_contents):.2%}
highest GC conent: {max(gc_contents):.2%}''')
