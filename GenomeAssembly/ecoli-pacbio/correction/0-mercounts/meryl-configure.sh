#!/bin/sh


#  Path to Canu.

bin="/Users/student/pfb2022_problemsets/GenomeAssembly/canu-2.2/bin"

#  Report paths.

echo ""
echo "Found perl:"
echo "  " `which perl`
echo "  " `perl --version | grep version`
echo ""
echo "Found java:"
echo "  " `which /Users/student/miniconda/bin/java`
echo "  " `/Users/student/miniconda/bin/java -showversion 2>&1 | head -n 1`
echo ""
echo "Found canu:"
echo "  " $bin/canu
echo "  " `$bin/canu -version`
echo ""


#  Environment for any object storage.

export CANU_OBJECT_STORE_CLIENT=
export CANU_OBJECT_STORE_CLIENT_UA=
export CANU_OBJECT_STORE_CLIENT_DA=
export CANU_OBJECT_STORE_NAMESPACE=
export CANU_OBJECT_STORE_PROJECT=




/Users/student/pfb2022_problemsets/GenomeAssembly/canu-2.2/bin/meryl -C k=16 threads=4 memory=8 \
  count segment=1/01 ../../ecoli.seqStore \
> ecoli.ms16.config.01.out 2>&1
exit 0
