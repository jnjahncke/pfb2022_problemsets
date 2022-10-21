# Similarity Searching Exercies

Use the FASTA search page to compare Honey bee glutathione transferase D1 NP_001171499/ H9KLY5_APIME (gi|295842263) to the PIR1 Annotated protein sequence database.

1. Take a look at the output:
	a. How long is the query sequence? 217 AA
	b. How many sequences are int he PIR1 databse? 13144 sequences
	c. What scoring matrix was used? BL50 matrix
	d. What were the gap penalties? A -10 penalty for opening a gap, a -2 penalty for each AA. (1 reside = 12, 2 residue = 14, etc.) (open/ext: -10/-2)
	e. What are each of the nubers after the description of the library sequence? Which one is best for inferring homology? E-value
	f. How similar is the highest scoring sequence? E = 3.9e-59, %id = 0.578, %sim = 0.811. There is no 100% match because it is not in the database.
	g. Looking at the alignment, where are the boundaries of the alignment (the best local region)? How many gaps are in the best alignment? The second best? 1 gap in the best alignment. 19 (?) gaps in the second best alignment.

2. Homologs, non-homologs, and the statistical control.
	a. What is the highest (worst) E-value shown? What should the ghighest value calculated in the search be, approximately? The highest value is 5. Theoretically, the highest value should be 13,144 (the number of sequences).
	b. Which alignment has the worst statistically significant E-score? Do you think this sequence is likely to be homologous? sp|P0ACA5|SSPA_ECO57 Stringent starvation protein A has an E-value of 0.00029. Based on the pfam domains, it is possibly that the sequence is homologous.
	c. What is the highest scoring non-homolog? Why do you think it is not homologous? sp|Q9SI20|EF1D2_ARATH Elongation factor 1-delta 2; Shor has an E-value of 0.11 and no homologous domains.
	d. If the statistical estimates are accurate, what should the E-value for the highest non-homology be? 0.0011
	e.What is the E-value of the most distant homolog shown? Could there be more distant homologs in the database? sp|P00785|ACTN_ACTCH Actinidain; Short=Actinidin; AltNa has an E-value of 4.3.
i	f. How would you confirm that your candidate non-homology was truly unrelated?  Look at the domains.

3. Domains and alignment regions:
	a. There are three parts to the domain display, the domain structure of the query (top) sequence (if available), the domain structure of the library (bottom) sequence, and the domain alignment boundaries in the middle (inside the alignment box). The boundaries and color of the alignment domain coloring match the Region: sub-alignment scores.
	b. Note that the alignment of Honey bee GSTD1 and SSPA_ECO57 includes portions of both the N-terminal and C-terminal domains, but neither domain is completely aligned. Why do you think the alignments do not include the complete domains? The e. coli sequecnce is just too evolutionarily distant at the ends; but the full domain is likely there. Moral: if it's not shown, that doesn't mean it's not there.
	c. Is your explanation for the partial domain alignment consistent the the argument that domains have a characteristic length? How might you test whether a complete domain is present?

4. Repeat the GSTD1 search using the BLASTP62/-11/-1 scoring matrix  that BLAST uses. Re-examine the honey bee/SSPA_ECO57 alignment.
	a. Are both Glutathione transferase domains present in the honey bee protein? No. Only the C. Thioredoxin domain is present.
	b. Look at the alignments to the homologs above and below SSPA_ECO57. Based on those. aligments, do you think the Glutathione-S-Trfase C-like domain is really missing from the honey bee protein? No
	c. Why did the alignment become shorter? 
	d. Why would a domain appear to be present in the first (BLOSUM50) search, but not in the second (BLOSUM62)?

5. Do the same Honey bee GSTD1 search (295842263) using the Course BLAST WWW page.
	a. Take a look at the output. 
		- How long is the query sequence? 217 AA
		- How many sequences are in the PIR1 database? 13,143 sequences
		- What scoring matrix was used?
		- What were the gap penalties?
		- what are then numbers after the description of the library sequence? Which one is best for inferring homology?
		- Looking at an alignment, where are the boundaries of the alignment (the best local region)?
	b. What is the highest scoring non-homolog? 0.34
	c. How do the BLASTP E-values compare with the FASTA (BLASTP62) E-values for the distantly related mammalian and plant sequences?
