#!/usr/bin/env python3

from Bio import SeqIO
import argparse
import sys

parser = argparse.ArgumentParser(description='This script splits your eASV repseqs into forward and reverse read files.')

parser.add_argument('--repseqs', help='Your eASV sequences as generated by deblur or DADA2. Must match the ASV table!', default='dna-sequences.fasta')

parser.add_argument('--forwardtrim', help='Required for 18s, 1-indexed.')

parser.add_argument('--reversetrim', help='Required for 18s, 1-indexed.')

args = parser.parse_args()

forwardtrim = int(args.forwardtrim)
reversetrim = int(args.reversetrim)

forwardout = str(args.repseqs).rsplit('.',1)[0] + ".R1.fasta"
reverseout = str(args.repseqs).rsplit('.',1)[0] + ".R2.fasta"

fwdhandle = open(forwardout, "w+")
revhandle = open(reverseout, "w+")

for record in SeqIO.parse(args.repseqs, "fasta"):

    forward = record[0:forwardtrim]
    reverse = record[forwardtrim:]

    SeqIO.write(forward, fwdhandle, "fasta")
    SeqIO.write(reverse, revhandle, "fasta")