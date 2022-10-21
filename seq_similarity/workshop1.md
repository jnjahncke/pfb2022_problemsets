# Similarity Searching Exercies

Use the FASTA search page to compare Honey bee glutathione transferase D1 NP_001171499/ H9KLY5_APIME (gi|295842263) to the PIR1 Annotated protein sequence database.

1. Take a look at the output:  
 
	1. How long is the query sequence? 217 AA
	2. How many sequences are int he PIR1 databse? 13144 sequences
	3. What scoring matrix was used? BL50 matrix
	4. What were the gap penalties? A -10 penalty for opening a gap, a -2 penalty for each AA. (1 reside = 12, 2 residue = 14, etc.) (open/ext: -10/-2)
	5. What are each of the nubers after the description of the library sequence? Which one is best for inferring homology? E-value
	6. How similar is the highest scoring sequence? E = 3.9e-59, %id = 0.578, %sim = 0.811. There is no 100% match because it is not in the database.
	7. Looking at the alignment, where are the boundaries of the alignment (the best local region)? How many gaps are in the best alignment? The second best? 1 gap in the best alignment. 19 (?) gaps in the second best alignment.

2. Homologs, non-homologs, and the statistical control.  

	1. What is the highest (worst) E-value shown? What should the ghighest value calculated in the search be, approximately? The highest value is 5. Theoretically, the highest value should be 13,144 (the number of sequences).
	2. Which alignment has the worst statistically significant E-score? Do you think this sequence is likely to be homologous? sp|P0ACA5|SSPA_ECO57 Stringent starvation protein A has an E-value of 0.00029. Based on the pfam domains, it is possibly that the sequence is homologous.
	3. What is the highest scoring non-homolog? Why do you think it is not homologous? sp|Q9SI20|EF1D2_ARATH Elongation factor 1-delta 2; Shor has an E-value of 0.11 and no homologous domains.
	4. If the statistical estimates are accurate, what should the E-value for the highest non-homology be? 0.0011
	5.What is the E-value of the most distant homolog shown? Could there be more distant homologs in the database? sp|P00785|ACTN_ACTCH Actinidain; Short=Actinidin; AltNa has an E-value of 4.3.
i	6. How would you confirm that your candidate non-homology was truly unrelated?  Look at the domains.

3. Domains and alignment regions:  

	1. There are three parts to the domain display, the domain structure of the query (top) sequence (if available), the domain structure of the library (bottom) sequence, and the domain alignment boundaries in the middle (inside the alignment box). The boundaries and color of the alignment domain coloring match the Region: sub-alignment scores.
	2. Note that the alignment of Honey bee GSTD1 and SSPA_ECO57 includes portions of both the N-terminal and C-terminal domains, but neither domain is completely aligned. Why do you think the alignments do not include the complete domains? The e. coli sequecnce is just too evolutionarily distant at the ends; but the full domain is likely there. Moral: if it's not shown, that doesn't mean it's not there.
	3. Is your explanation for the partial domain alignment consistent the the argument that domains have a characteristic length? How might you test whether a complete domain is present?

4. Repeat the GSTD1 search using the BLASTP62/-11/-1 scoring matrix  that BLAST uses. Re-examine the honey bee/SSPA_ECO57 alignment.  
	
	1. Are both Glutathione transferase domains present in the honey bee protein? No. Only the C. Thioredoxin domain is present.
	2. Look at the alignments to the homologs above and below SSPA_ECO57. Based on those. aligments, do you think the Glutathione-S-Trfase C-like domain is really missing from the honey bee protein? No
	3. Why did the alignment become shorter? 
	4. Why would a domain appear to be present in the first (BLOSUM50) search, but not in the second (BLOSUM62)?

5. Do the same Honey bee GSTD1 search (295842263) using the Course BLAST WWW page.  
	
	1. Take a look at the output. 
		- How long is the query sequence? 217 AA
		- How many sequences are in the PIR1 database? 13,143 sequences
		- What scoring matrix was used?
		- What were the gap penalties?
		- what are then numbers after the description of the library sequence? Which one is best for inferring homology?
		- Looking at an alignment, where are the boundaries of the alignment (the best local region)?
	2. What is the highest scoring non-homolog? 0.34
	3. How do the BLASTP E-values compare with the FASTA (BLASTP62) E-values for the distantly related mammalian and plant sequences?
