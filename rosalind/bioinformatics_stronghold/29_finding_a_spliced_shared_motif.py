# LCS - longest common subsequence
# Credit to this tutorial that helped me understand this problem: https://www.youtube.com/watch?v=NnD96abizww&t=323s

# A string u is a common subsequence of strings s and t if the symbols of u appear in order as a subsequence of both s and t. 
# For example, "ACTG" is a common subsequence of "AACCTTGG" and "ACACTGTGA".

# Analogously to the definition of longest common substring, u is a longest common subsequence of s and t if there does not exist a longer common subsequence of the two strings. 
# Continuing our above example, "ACCTTG" is a longest common subsequence of "AACCTTGG" and "ACACTGTGA", as is "AACTGG".

# Given: Two DNA strings s and t (each having length at most 1 kbp) in FASTA format.
# Return: A longest common subsequence of s and t. (If more than one solution exists, you may return any one.)

# Dynamic progamming

# Compare to 14_finding_a_shared_motif.py and 26_finding_a_spliced_motif

# Reformat FASTA file and store sequence data in an array, using Biopython library
from Bio import SeqIO 

dnaList = []
dataFile = open('txt_files/29_rosalind_lcsq.txt', 'r')
for seq_record in SeqIO.parse(dataFile, 'fasta'):
    seq = ''
    for nt in seq_record:
        seq += nt
    dnaList.append(seq)
dataFile.close()

# s = given DNA string, t = a subsequence of s
s = dnaList[0]
t = dnaList[1]

# Sample 2D array           # If rows = len(s), cols = len(t)
#     A A C C T T G G               
#   0 0 0 0 0 0 0 0 0 
# A 0 1 1 1 1 1 1 1 1 
# C 0 1 1 2 2 2 2 2 2 
# A 0 1 2 2 2 2 2 2 2  
# C 0 1 2 3 3 3 3 3 3
# T 0 1 2 3 3 4 4 4 4
# G 0 1 2 3 3 4 4 5 5
# T 0 1 2 3 3 4 5 5 5
# G 0 1 2 3 3 4 5 6 6
# A 0 1 2 3 3 4 5 6 6

# Sample 2D array           # If cols = len(s), rows = len(t)
#     A C A C T G T G A
#   0 0 0 0 0 0 0 0 0 0 
# A 0 1 1 1 1 1 1 1 1 1
# A 0 1 1 2 2 2 2 2 2 2
# C 0 1 2 2 3 3 3 3 3 3 
# C 0 1 2 2 3 3 3 3 3 3
# T 0 1 2 2 3 4 4 4 4 4
# T 0 1 2 2 3 4 4 5 5 5
# G 0 1 2 2 3 4 5 5 6 6
# G 0 1 2 2 3 4 5 5 6 6

# Create a 2D array of lengths
rows = len(s) + 1
cols = len(t) + 1
lenArr = [[0 for i in range(rows)] for j in range(cols)]

for i in range(0, cols):
    for j in range(0, rows):
        if i == 0 or j == 0:
            lenArr[i][j] = 0
        elif t[i - 1] == s[j - 1]:
            lenArr[i][j] = lenArr[i - 1][j - 1] + 1
        else:
            lenArr[i][j] = max(lenArr[i - 1][j], lenArr[i][j - 1])

# Visualize the 2D array of lengths
# for i in range(0, len(lenArr)):
#     print (lenArr[i])

# Bottom up
result = ''
x = len(s)
y = len(t)

while x != 0 and y != 0:
    if lenArr[y][x] == lenArr[y][x - 1]:
        x -= 1
    elif lenArr[y][x] == lenArr[y - 1][x]:
        y -= 1
    else:
        result = s[x - 1] + result
        y -= 1
        x -= 1

print (result)
