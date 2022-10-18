# Counting k-mers

We're going to write a python program that counts kmers from reads in a fastq file.  To do this, we'll first break the task up into smaller parts involving:

* A. retrieving the sequences from the fastq file
* B. extracting kmers from a sequence
* C. counting the kmers among all sequences

Let's tackle each in the above order, and in the process, be generating a library of reusable python methods.



## Part A: Retrieve sequences from a fastq file

Write a python script that retrieves a list of all read sequences from a fastq file. 

A script [fastq_file_to_sequence_list.py](fastq_file_to_sequence_list.py) is provided as a starting point.  Fill in the missing code.

A fastq file <reads.fq> is provided as input.

The script usage is:

```
    usage: ./fastq_file_to_sequence_list.py filename.fastq num_seqs_show
```

Running it like so:

```
    fastq_file_to_sequence_list.py reads.fq 10
```

Should produce the following output:

['ACTGCATCCTGGAAAGAATCAATGGTGGCCGGAAAGTGTTTTTCAAATACAAGAGTGACAATGTGCCCTGTTGTTT', 'GTAATTTCCGTACCTGCCACAGTGTGGGCTCACCCTGCTTAGAGGACAGGGAAGGACCCTAAAGGTAGGCTGATGC', 'CTGGGCTGCAGCTAAGTTCTCTGCATCCTCCTTCTTGCTTGTGGCTGGGAAGAAGACAATGTTGTCGATGGTCTGG', 'CACGTTTTCTAAGCAGTTTGTACCAGATCGTGCTAACTGCTCATTGTCTTGTTGTACACACCAGTAAAGCTGGGCA', 'TGCTCATTGTCTTGTTGTACACACCAGTAAAGCTGGGCAAAAATATCATCCAAAAGTACATCGCTGAGAACTCCTA', 'CCCACCTGAAAACATTTTCTACATCCACTGTTATATGGAATGCTTGATAAGCTTTTCATTCTAACCATCAGAGCAC', 'TCTGAATAAGTCCTGCCACCAATGTTTTTCATAAGTGTGGCCATATGTTTTCATTATTTCAAACATTACTGTTAAG', 'CTCCGTTTTTTGAGAGTGCAACACATAGATACTGCTTGATAGCATTAATAAACATCTCATTTGTCCTGAAAACAGG', 'GCCTGAGTGTGCAAAAATCTTCAGAGTAAGAATACCATAGTTGCTAAATATCTTTTACCATGAGCAATAATTTTTT', 'TCTGGTGCAGCTAGATGGAATACTGAGAAAATGTTCTTCCATCCTGAACGAATATTTGCAGCCTGAGAATTAACCA']


## Part B: Extracting kmers from a sequence

Write a python script to extract all kmers of a specified length from a nucleotide sequence.

A script [fastq_file_to_sequence_list.py](fastq_file_to_sequence_list.py) is provided as a starting point.  Fill in the missing code.

The script usage is:

```
   usage: ./sequence_to_kmer_list.py sequence kmer_length
```

Running it like so:

```
    sequence_to_kmer_list.py ACTGCATCCTGGAAAGAATCAATGGTGGCCGGAAAGTGTTTTTCAAATACAAGAGTGACAATGTGCCCTGTTGTTT 6
```

Should produce the following output:

['ACTGCA', 'CTGCAT', 'TGCATC', 'GCATCC', 'CATCCT', 'ATCCTG', 'TCCTGG', 'CCTGGA', 'CTGGAA', 'TGGAAA', 'GGAAAG', 'GAAAGA', 'AAAGAA', 'AAGAAT', 'AGAATC', 'GAATCA', 'AATCAA', 'ATCAAT', 'TCAATG', 'CAATGG', 'AATGGT', 'ATGGTG', 'TGGTGG', 'GGTGGC', 'GTGGCC', 'TGGCCG', 'GGCCGG', 'GCCGGA', 'CCGGAA', 'CGGAAA', 'GGAAAG', 'GAAAGT', 'AAAGTG', 'AAGTGT', 'AGTGTT', 'GTGTTT', 'TGTTTT', 'GTTTTT', 'TTTTTC', 'TTTTCA', 'TTTCAA', 'TTCAAA', 'TCAAAT', 'CAAATA', 'AAATAC', 'AATACA', 'ATACAA', 'TACAAG', 'ACAAGA', 'CAAGAG', 'AAGAGT', 'AGAGTG', 'GAGTGA', 'AGTGAC', 'GTGACA', 'TGACAA', 'GACAAT', 'ACAATG', 'CAATGT', 'AATGTG', 'ATGTGC', 'TGTGCC', 'GTGCCC', 'TGCCCT', 'GCCCTG', 'CCCTGT', 'CCTGTT', 'CTGTTG', 'TGTTGT', 'GTTGTT', 'TTGTTT']


## Part C: Counting all kmers from all sequences in a fastq file

Now, let's count all kmers in all sequences.  We can leverage each of the methods implemented above. Because of the way we wrote the above scripts, we can leverage them as a code library and simply import them for use in a new script.

Use the script [count_kmers_from_fastq.py](count_kmers_from_fastq.py) as the starting point.  You'll see at the top of this script:

```
from sequence_to_kmer_list import *
from fastq_file_to_sequence_list import *
```

Those lines import the methods we implemented earlier so that we can just reuse them without having to rewrite or copy/paste any code in this new script.

The usage of our script is:

```
    usage: ./count_kmers_from_fastq.py filename.fastq kmer_length num_top_kmers_show
```

And when we run it like so:

```
    count_kmers_from_fastq.py reads.fq 6 10
```

It should produce the output:

```
TTTTTT: 3085
CTTCTT: 2550
AAAAAA: 2498
CTGCTG: 2446
AGCTGG: 2400
CAGCAG: 2265
CAGCTG: 2243
TCTTCT: 2208
CTGGAG: 2174
TGCTGT: 2156
```
## Extra credit section:

If you've accomplished the above, here's another challenge!

Note that the top-most kmer is of low complexity.  If we are going to perform downstram operations like assembly and want to start with a seed kmer, we might want to avoid low complexity kmers as they would lack specificity.

Challenge:  include another method that computes the complexity of each kmer using Shannon's Entropy
      (example:  see: https://en.wikipedia.org/wiki/Sequence_logo#Logo_creation ), and picture the kmer as representing one column of the seqlogo for which you would get one entropy calculation.

Add the entropy value as another column in the above printing.


# Estimating Gene Expression Levels

Write a python program that reads in the 'bowtie2.sam' file and generates a table containing the number of reads mapped to each gene.

For example:

    gene_read_counter.py bowtie2.sam

would return:

    CG14995 1654
    S-Lap3  1598
    Eno     1415
    sqd     866
    AdipoR  792
    Est-6   780
    Cnx99A  777
    eff     770
    CG31948 709
    eIF5B   671
    Aldh-III        634
    CG6424  604
    Calx    542
    ...





# About the data:

The alignments are stored in a 'bam' file - the binary equivalent of the 'sam' file format.  The format of the alignments are like so, showing the first few rows:

    25_1_17589_1126_120	83	AdipoR^FBtr0084283	536	1	101M	=	517	-120	GGCGCATTGGCACACAATGCCGCCGAGCAGGCGGAGGAGTTTGTGCGCAAGGTCTGGGAGGCTAGCTGGAAAGTGTGCCACTACAAAAATCTACCCAAGTG	EGJJHHIIHFFFFFHJJJIGIJJJJJJJIGFFFCIHB>@2DDEFFFF@DDBDBCC>@HHHHHHGHFFFFDDDDCDDDDDDFFHG@7FFBCCDDDB<FFD@B	AS:i:-5	XS:i:-5	XN:i:0	XM:i:1	XO:i:0	XG:i:0	NM:i:1	MD:Z:32A68	YS:i:-5	YT:Z:CP
    25_1_17589_1126_120	163	AdipoR^FBtr0084283	517	1	101M	=	536	120	CTCCGATGAAATTGATTTGGGCGCATTGGCACACAATGCCGCCGAGCAGGCAGAGGAGTTTGTGCGCAAGGTCTAGGAGGCTAGCTGGAAAGTGTGCCACT	CA?@@;@FFHHHIHIJJJIIHHHHJJJJJJJJJJJJJJJJC?6.(<92++9ABCHHIJIGIIJJIJJJJJJIIGGIJJJJJJJJJJJJJIJJIIIIJJJJJ	AS:i:-5	XS:i:-5	XN:i:0	XM:i:1	XO:i:0	XG:i:0	NM:i:1	MD:Z:74G26	YS:i:-5	YT:Z:CP
    25_1_17589_1126_120	339	AdipoR^FBtr0308848	649	1	101M	=	630	-120	GGCGCATTGGCACACAATGCCGCCGAGCAGGCGGAGGAGTTTGTGCGCAAGGTCTGGGAGGCTAGCTGGAAAGTGTGCCACTACAAAAATCTACCCAAGTG	EGJJHHIIHFFFFFHJJJIGIJJJJJJJIGFFFCIHB>@2DDEFFFF@DDBDBCC>@HHHHHHGHFFFFDDDDCDDDDDDFFHG@7FFBCCDDDB<FFD@B	AS:i:-5	XS:i:-5	XN:i:0	XM:i:1	XO:i:0	XG:i:0	NM:i:1	MD:Z:32A68	YS:i:-5	YT:Z:CP

The first field is the read name (ex. 25_1_17589_1126_120) and the second field is the name of the transcript sequence that read aligned to (ex. AdipoR^FBtr0084283).

For these data, the transcript identifiers include the gene identifier as a prefix.  So, the transcript AdipoR^FBtr0084283 corresponds to gene AdipoR.

>Note that a read that aligns to a region of shared sequence among multiple splicing isoforms for a gene will end up mapping to each of those isoforms (ie. multiply mapped).  If we are going to count reads mapping to genes, we'll want to count each read-to-gene mapping only once.


# Implementation options:

You'll need to uncompress the gzipped sam file in order to more easily read the data in your program. Youc an do this directly using gunzip:

    gunzip bowtie2.sam.gz

and then parse that tab-delimited text file.

Or, try reading the gzip file directly as per <https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python>


A useful data structure for storing the unique read-to-gene mappings is to use a set() built-in data structure.  
   
   
      ie. a dict[gene] = set(read1, read2, ...)

where each gene is associated with the unique set of reads that mapped to any of its transcript isoform sequences.





