# Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.
# Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.

# Reformat FASTA file and store sequence data in an array, using Biopython library
from Bio import SeqIO 

dnaList = []
dataFile = open('txt_files/26_rosalind_sseq.txt', 'r')
for seq_record in SeqIO.parse(dataFile, 'fasta'):
    seq = ''
    for nt in seq_record:
        seq += nt
    dnaList.append(seq)
dataFile.close()

# s = given DNA string, t = a subsequence of s
s = dnaList[0]
t = dnaList[1]

# Make t (shorter string) the outer loop to avoid as many unnecessry iterations as possible
output = []
current = 0
for i in range(0, len(t)):
    for j in range(current, len(s)):
        # current must be here instead of before the second loop
        # Every time j increments, current increments as well
        # If not clear, print i, j, and current in the if statement to verify
        current += 1   
        if s[j] == t[i]:
            output.append(j + 1)
            break

# end=' ' doesn't work in VS Code
print (*output, sep=' ')
