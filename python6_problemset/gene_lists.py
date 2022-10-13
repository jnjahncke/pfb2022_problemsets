#!/usr/bin/env python3

allgenes = set()
with open("alpaca_all_genes.tsv", "r") as allgenes_file:
	for line in allgenes_file:
		line = line.rstrip()
		if line[0] == "E":
			allgenes.add(line)

stemcellgenes = set()
with open("alpaca_stemcellproliferation_genes.tsv", "r") as stemcellgenes_file:
	for line in stemcellgenes_file:
		line = line.rstrip()
		if line[0] == "E":
			stemcellgenes.add(line)

pigmentationgenes = set()
with open("alpaca_pigmentation_genes.tsv", "r") as pigmentationgenes_file:
	for line in pigmentationgenes_file:
		line = line.rstrip()
		if line[0] == "E":
			pigmentationgenes.add(line)


transcriptionfactors = set()
with open("alpaca_transcriptionFactors.tsv", "r") as transcriptionfactors_file:
	for line in transcriptionfactors_file:
		line = line.rstrip()
		if line[0] == "E":
			transcriptionfactors.add(line)


# Find all genes that are NOT cell proliferation genes
notproliferation = allgenes - stemcellgenes

# Find all genes that are both stem cell proliferation genes and pigment genes
both = stemcellgenes & pigmentationgenes # there are none!

# Find all genes that are transcription factors for cell proliferation
proliferationTFs = stemcellgenes & transcriptionfactors
