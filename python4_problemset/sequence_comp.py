#!/usr/bin/env python3

# Sequences, alignments
seqA_fasta = '''>gi|170746|gb|M12277.1|WHTH4091 Wheat histone H4 TH091 gene, complete cds
AGCACCCTCCCACCTCATCCCACCCTTCTGATCTCAATCCAACGTCGCATCTCCACCGTCTCGCGGATCG
ACCCAGCGAAGTCCCTCCCGCCCCCAAAGTCCCCCAAATCTTGCAGTTCCCTCCTAAATCCTCCCCATAT
AAACCAACCCCCCGCCCTCAGATCCCTAATCCCATCGCAAGCATCAGACTCCCTCCAAAGCAGGCAGCAG
CTCCTCTTCTTCCTAATCACACTATCTCGGAGAGGAGCGGCCATGTCTGGGCGCGACAAGGGCGGCAAGG
GGCTGGGCAAGGGCGGCGCCAAGCGGCACCGGAAGGTCCTCCGCGACAACATCCAGGGCATCACCAAGCC
GGCGATCCGGAGGCTGGCCAGGAGGGGCGGCGTGAAGCGCATCTCCGGCCTCATCTACGAGGAGACCCGC
GGCGTCCTCAAGATCTTCCTCGAGAACGTCATCCGCGACGCCGTCACCTACACCGAGCACGCCCGCCGCA
AAACCGTCACCGCCATGGACGTCGTCTACGCGCTCAAGCGCCAGGGCCGCACCCTCTACGGCTTCGGAGG
CTAGATTTGTGTGGTGAAGCAACTTCCTCGTTTGCTCTGTGATCTGTGCTGTCGTAGATGAGATTTACTG
ATTTGGCGTGCGCCGGTTGTATTCTGTCATGGGGTTCAGTGGGCTGTGTAATACCTTGCTCTGTACTTCT
GTTCAATGCAATCACTTCTATTCTGAA'''

seqB_fasta = '''>gi|603555|emb|X83548.1| H.sapiens gene for histone H4
TCTAGAGATGGCGCCATTTGATTCCAGCAGCCACAAAGCACTAGAACAATCGATGCTAAGAGGTGACAGG
AAAAACAGGCTGCAAAGACCCAGACAATGGAATGCAGCGGTGGTCAGCCTAAAACACTGTAGAAGGGCAA
GATGAGCTGAGTAATTTTTAACTGGGCATCATTTTTAGAAACTGGAGTTTAAGTACCCCCTTTTCCATTT
TTTCCTGAAGTCGTGGGCAGGGCGCAAGGTCTGTGAATCGGCCGACCGGATGCAGCTGGTGTGGAGAGTT
CCCAATCAGGTCCGATTTATTACTATATAAAGTACTGCTGCGAGGCTTGCCGTGTTGCATTTTGTTTAGT
ACAAGACATGTCTGGGCGCGGCAAAGGCGGGAAGGGTCTGGGCAAAGGAGGCGCTAAGCGCCACCGCAAA
GTTCTGCGCGACAACATTCAGGGCATCACCAAGCCCGCCATCCGACGCCTGGCACGGCGTGGAGGCGTTA
AGCGCATCTCAGGCCTTATATACGAGGAGACACGCGGAGTTCTTAAAGTGTTTTTGGAGAATGTAATCCG
CGATGCAGTTACCTACACGGAGCACGCCAAACGCAAGACAGTCACAGCCATGGACGTGGTTTACGCGCTC
AAGCGCCAGGGCCGCACCCTGTATGGCTTTGGCGGCTGAGTGTTTTACTTACTTACACGGTTCCTCAAAG
GCCCTTCTCAGGGCCACCCATGAAGTCTGTGAAAGAGCTGTAGACTAAAGATAGTTAATTTCTTAAGAAC
ACTTAAACGTATGGCAGTTTTGGCAAATTAGCGATTCCACATAAGCAGTCGCTGAAGTTTGAGGTTCGGT
GCCCCTTTCAGCATTACTTAGTGGTTAAAA'''

seqA_align_fasta = '''>gi|170746|gb|M12277.1|WHTH4091 Wheat histone H4 TH091 gene, complete cds
AGCAC----CCTCCCACCTCATCCCACCCTTCTGATCTCAATCCAACG-TCG--------
---CATCTCCACCGTCTCGC-GGATCGACCCAG----CGAAGTCCCTC--CCGCC--CCC
AAAGTCCC--------CCAAATCTTGCAGT-TCCCTCCTAAATCCTCCCCA----TATAA
ACC-------AA---CCCCC-CGCCCTCAGATCCCTAATCCCA--------TCGCAAGC-
ATCAGACTCCCTC---C-AAAGCAG---GCA--------------GCAGCTCCTC-TTCT
TCCTAATCACACTATCTCGGAGAG-------------------------GAGCGGCCATG
TCTGGGCGCGACAAGGGCGGCAAGGGGCTGGGCAAGGGCGGCGCCAAGCGGCACCGGAAG
GTCCTCCGCGACAACATCCAGGGCATCACCAAGCCGGCGATCCGGAGGCTGGCCAGGAGG
GGCGGCGTGAAGCGCATCTCCGGCCTCATCTACGAGGAGACCCGCGGCGTCCTCAAGATC
TTCCTCGAGAACGTCATCCGCGACGCCGTCACCTACACCGAGCACGCCCGCCGCAAAACC
GTCACCGCCATGGACGTCGTCTACGCGCTCAAGCGCCAGGGCCGCACCCTCTACGGCTTC
GGAGGCTAGA---TTTGT--------GTGGTGAAGCAA----CTTCCTCGT---TTGCTC
TGTGATCTGTGC---TGTCGTAGATGAGATTTAC-TGATTT--------------GGCGT
GCGCCGGTTGTATTCTGTCATGGGGTTCA-----GTGGGCTGTGTAATACCTTGCTCTGT
ACTTCTGTTCAATGCAATCACTT-CTATTCTGAA'''

seqB_align_fasta = '''>gi|603555|emb|X83548.1| H.sapiens gene for histone H4
TCTAGAGATGGCGCCATTTGATTCCAGCAGCCACAAAGCACTAGAACAATCGATGCTAAG
AGGTGACAGGAAAAACAGGCTGCAAAGACCCAGACAATGGAATGCAGCGGTGGTCAGCCT
AAAACACTGTAGAAGGGCAAGATGAGCTGAGTAATTTTTAACTGGGCATCATTTTTAGAA
ACTGGAGTTTAAGTACCCCCTTTTCCATTTTTTCCTGAAGTCGTGGGCAGGGCGCAAGGT
CTGTGAATCGGCCGACCGGATGCAGCTGGTGTGGAGAGTTCCCAATCAGGTCCGATTTAT
TACTATATAAAGTACTGCTGCGAGGCTTGCCGTGTTGCATTTTGTTTAGTACAAGACATG
TCTGGGCGCGGCAAAGGCGGGAAGGGTCTGGGCAAAGGAGGCGCTAAGCGCCACCGCAAA
GTTCTGCGCGACAACATTCAGGGCATCACCAAGCCCGCCATCCGACGCCTGGCACGGCGT
GGAGGCGTTAAGCGCATCTCAGGCCTTATATACGAGGAGACACGCGGAGTTCTTAAAGTG
TTTTTGGAGAATGTAATCCGCGATGCAGTTACCTACACGGAGCACGCCAAACGCAAGACA
GTCACAGCCATGGACGTGGTTTACGCGCTCAAGCGCCAGGGCCGCACCCTGTATGGCTTT
GGCGGCTGAGTGTTTTACTTACTTACACGGTTCCTCAAAGGCCCTTCTCAGGGCCACCCA
TGAAGTCTGTGAAAGAGCTGTAGACTAAAGATAGTTAATTTCTTAAGAACACTTAAACGT
ATGGCAGTTTTGGCAAATTAGCGATTCCACATAAGCAGTCGCTGAAGTTTGAGGTTCGGT
GCCCCT-TTCA--GC-ATTACTTAGTGGTTAAAA'''

# Get rid of fasta header; remove newlines - all in one go
seqA_align = seqA_align_fasta.split("\n")
seqA_align = seqA_align[1:]
seqA_align = "".join(seqA_align)

seqB_align = seqB_align_fasta.split("\n")
seqB_align = seqB_align[1:]
seqB_align = "".join(seqB_align)

# Compare the two sequnces
# Report percent identity
same = 0
seqlength = len(seqA_align)
for NT in range(0, seqlength):
	# Find the identity of each sequence at the current position
	A = seqA_align[NT]
	B = seqB_align[NT]
	# IF they are the same, increase `same` by 1
	if A == B:
		same += 1

# The percent identity is the ratio of same to the length of the alignment
pctsame = same*100/seqlength
print(f'The percent identity is {round(pctsame,3)}%')
