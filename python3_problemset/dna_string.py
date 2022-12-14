#!/usr/bin/env python3

import sys
# Get DNA sequence from user
dna_temp = sys.argv[1]
dna = dna_temp.upper() # Change all to uppercase

# Count ATCGs
A = dna.count("A")
T = dna.count("T")
C = dna.count("C")
G = dna.count("G")

print(f'\n\nThis sequence has {A} As, {T} Ts, {C} Cs, and {G} Gs.')

# Convert DNA to RNA
rna = dna.replace("T","U")
print(f'\n\nSequence converted to RNA: {rna}')


# Calculate AT content
AorT = A + T
AT_content = AorT/len(dna)
print(f'\n\nThe AT content of the DNA sequnce is {AT_content:.3f}.')


# Substring from nucleotide number 100 to 200
dna_100to200 = dna[99:200]
print(f'\n\nBases 100 to 200: {dna_100to200}')

# Print reverse complement of substring
dna_100to200_comp = dna_100to200.replace("C","g")
dna_100to200_comp = dna_100to200_comp.replace("G","c")
dna_100to200_comp = dna_100to200_comp.replace("T","a")
dna_100to200_comp = dna_100to200_comp.replace("A","t")
dna_100to200_comp = dna_100to200_comp.upper()[::-1]
print(f'\n\nThe DNA reverse complement of this substring is: {dna_100to200_comp}')







