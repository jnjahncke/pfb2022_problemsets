#!/usr/bin/env python3

taxa = "sapiens, erectus, neanderthalensis"
print(taxa)
print(taxa[1])
print(type(taxa))


# split into list of individual words
species = taxa.split(', ')
print(species)
print(species[1])
print(type(species))

# sort the list alphabetically
print(sorted(species))

# sort the list by the length of each string
print(sorted(species, key=len, reverse=False))
