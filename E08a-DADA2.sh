#!/bin/bash
source activate qiime2-2018.8

qiime dada2 denoise-single \
  --i-demultiplexed-seqs 18s-concat.qza \
  --p-trim-left 0 \
  --p-trunc-len 0 \
  --output-dir 08a-DADA2d \
  --p-n-threads 10 \
  --verbose

source deactivate
