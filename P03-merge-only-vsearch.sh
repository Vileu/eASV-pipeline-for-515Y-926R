#!/bin/bash
mkdir logs
mkdir logs/03-VSEARCH-merging

source activate qiime2-2018.8

qiime vsearch join-pairs \
  --output-dir 03-merged \
  --i-demultiplexed-seqs 16s.qza \
  --verbose 2>&1 | tee -a logs/03-VSEARCH-merging/log.txt