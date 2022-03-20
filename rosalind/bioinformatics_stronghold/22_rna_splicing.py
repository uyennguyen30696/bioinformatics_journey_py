# Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.
# Return: A protein string resulting from transcribing and translating the exons of s.

# Reformat FASTA file and store sequence data in an array, using Biopython library
from Bio import SeqIO 

dnaList = []
dataFile = open('txt_files/22_rosalind_splc.txt', 'r')
for seq_record in SeqIO.parse(dataFile, 'fasta'):
    seq = ''
    for nt in seq_record:
        seq += nt
    dnaList.append(seq)
dataFile.close()

# Codon table
rnaCodons = {
    "UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
    "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UAA":"Stop", "UAG":"Stop",
    "UGU":"C", "UGC":"C", "UGA":"Stop", "UGG":"W",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
    "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
    "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G" }

# DNA string is the first string in the list
dna = dnaList[0]
# The rest in the list are introns (substrings)
introns = []
for i in range(1, len(dnaList)):
    introns.append(dnaList[i])

# Remove introns
def remove_introns(dna):
    for intron in introns:
        dna = ''.join(dna.split(intron))
    return dna

# Translate dna to rna (replace Ts with Us)
def dna_to_rna(dna_no_intron):
    dna_no_intron = remove_introns(dna)
    rna = dna_no_intron.replace('T', 'U')
    return rna

# Transcribe rna to protein
def rna_to_protein():
    rna = dna_to_rna(dna)
    protein = ''
    for i in range(0, len(rna), 3):
        codon = rnaCodons[rna[i:i+3]]
        if codon == 'Stop':
            break
        protein += codon
    return protein

print ('Protein =', rna_to_protein())
