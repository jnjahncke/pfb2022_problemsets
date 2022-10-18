#!/usr/bin/env python3

import math
import sys

## Shannon's entropy: a measure of sequence complexity
## For a kmer,
## 		For each base,
##		Calculate the relative frequency = f
## 		Calculate f x log2(f)
## Shannon's entropy = -1 * (A_f + G_f + C_f + D_f)
##		Should range from 0 to 2

def shannons_entropy(kmer):
	
	kmer_len = len(kmer)
	
	Afreq = kmer.count("A")/kmer_len
	Gfreq = kmer.count("G")/kmer_len
	Cfreq = kmer.count("C")/kmer_len
	Tfreq = kmer.count("T")/kmer_len
	
	if Afreq != 0:
		A = (Afreq) * math.log(Afreq)/math.log(2)
	else:
		A = 0
	if Gfreq != 0:
		G = (Gfreq) * math.log(Gfreq)/math.log(2)
	else:
		G = 0
	if Cfreq != 0:
		C = (Cfreq) * math.log(Cfreq)/math.log(2)
	else:
		C = 0
	if Tfreq != 0:
		T = (Tfreq) * math.log(Tfreq)/math.log(2)
	else:
		T = 0

	shan_ent = -(A + G + C + T)

	return(shan_ent)


def main():

	progname = sys.argv[0]
	usage = "\n\n\tusage: {progname] <kmer>\n\n\n"
	
	if len(sys.argv) < 2:
		sys.stderr.write(usage)
		sys.exit(1)
	
	kmer = sys.argv[1]
	shann_ent = shannons_entropy(kmer)
	print(shann_ent)

	sys.exit(0)

if __name__ == '__main__':
	main()
