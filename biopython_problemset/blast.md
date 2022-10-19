```
conda install -c bioconda blast
```

Input file = `salmonella.fasta'

Format FASTA file so that BLAST+ can use it as a database:

```
makeblastdb -in salmonella.fasta -dbtype prot -out salmonella.db.fasta -parse_seqids
```

Returns multiple salmonella.db.fasta.* files but the db name is `salmonella.db.fasta`

Run `blastp`:

```
blastp -query salmonella.fasta -db salmonella.db.fasta -out query_out -evalue 1e-5 -outfmt 5 
```

- Common evalue is 1e-2 to 1e-5 (1e-5 is more conservative)
- `-outfmt 5` makes an xml file as the output file
