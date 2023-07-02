# Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
# Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.

# Refer to matching in graph theory https://en.wikipedia.org/wiki/Matching_(graph_theory)
# and bipartite graph https://en.wikipedia.org/wiki/Bipartite_graph

from math import factorial

with open('txt_files/24_rosalind_pmch.txt') as f:
    line = f.read().split()[1:]
    str = ''
    for i in line:
        str += i
    print(str)

num_AU = str.count('A')
num_GC = str.count('G')

matching = factorial(num_AU) * factorial(num_GC)
print(matching)
