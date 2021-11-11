# Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

s = open('txt_files/6_rosalind_hamm.txt', 'r').readlines()[0]
t = open('txt_files/6_rosalind_hamm.txt', 'r').readlines()[1]

count = 0
for i in range(len(s)):
    if s[i] != t[i]:
        count += 1
        
print (count)
