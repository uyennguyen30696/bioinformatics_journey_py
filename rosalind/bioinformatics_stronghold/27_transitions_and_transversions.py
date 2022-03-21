# For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the total number of transitions to the total number of transversions, 
# where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

# Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).
# Return: The transition/transversion ratio R(s1,s2).

# Transitions
# A <--> G
# C <--> T

# Transversions
# A <--> C
# A <--> T
# G <--> C
# G <--> T

# Reformat FASTA file and store sequence data in an array, using Biopython library
from Bio import SeqIO 

dnaList = []
dataFile = open('txt_files/27_rosalind_tran.txt', 'r')
for seq_record in SeqIO.parse(dataFile, 'fasta'):
    seq = ''
    for nt in seq_record:
        seq += nt
    dnaList.append(seq)
dataFile.close()

s1 = dnaList[0]
s2 = dnaList[1]

numTransition = 0
numTransversion = 0

# s1 and s2 have the same length
for i in range(0, len(s1)):
    if (s1[i] == 'A' and s2[i] == 'G') or (s1[i] == 'G' and s2[i] == 'A'):
        numTransition += 1
    elif (s1[i] == 'C' and s2[i] == 'T') or (s1[i] == 'T' and s2[i] == 'C'):
        numTransition += 1
    elif (s1[i] == 'A' and s2[i] == 'C') or (s1[i] == 'C' and s2[i] == 'A'):
        numTransversion += 1
    elif (s1[i] == 'A' and s2[i] == 'T') or (s1[i] == 'T' and s2[i] == 'A'):
        numTransversion += 1
    elif (s1[i] == 'G' and s2[i] == 'C') or (s1[i] == 'C' and s2[i] == 'G'):
        numTransversion += 1
    elif (s1[i] == 'G' and s2[i] == 'T') or (s1[i] == 'T' and s2[i] == 'G'):
        numTransversion += 1

r = numTransition / numTransversion

print ('R(s1,s2) = %.11f' %r)
