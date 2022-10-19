#!/usr/bin/env python3

from Bio import SearchIO

blast_file = "query_out.xml"

# print hit sequence id if better than 1e-5 as well as descriptions in tab separated columns.

for query in SearchIO.parse(blast_file,"blast-xml"):
	for hit in query:
		print(f'{hit.id}\t{hit.description}')
