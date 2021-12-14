# A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".
# Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

# Problem breakdown
# Common substring not to be confused with common subsequence. Common substring is continuous while common subsequence is not necessary continuous, but the order of each element is maintained
# Sort the array of all dna sequences to get the shortest string, and store the rest in the remain_strs array
# The longest common substring can not be longer than the shortest string, that's why we only need to test the shortest string and its substrings compared to all other strings
# To find the collection of substrings from the shortest string, we first test the substring with length l, then the 2 substrings length l - 1, and so forth
# Since the collection of substrings we found this way ranges from longest to shorest length, the first common substring we find will automatically be the answer, the longest common substring

# Reformat FASTA file and store sequence data in an array, using Biopython library
from Bio import SeqIO 

seqArr = []
file = open('txt_files/14_rosalind_lcsm.txt', 'r')
for seq_record in SeqIO.parse(file, 'fasta'):
    seq = ''
    for nt in seq_record:
        seq += nt
    seqArr.append(seq)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Find all substrings possible derived from the shortest string and store in an array
# Iterate over the shortest string by increasing i on the left side and decreasing l from the right side
def substrings(shortest_str):
    subArr = []
    l = len(shortest_str)

    while l > 0:
        for i in range(len(shortest_str) - l + 1):
            sub_str = shortest_str[i:i+l]
            subArr.append(sub_str)
        l -= 1

    return subArr

# Check if a substring is a common substring
def is_common_sub(sub, remain_strs):
    for each in remain_strs:
        if sub not in each:
            return False
        return True

# Find the longest common substring (lcsm)
def is_lcsm(seqArr):
    # Sort and get the shortest substring
    sort_seq = sorted(seqArr, key=len)
    shortest_str = sort_seq[0]
    remain_strs = sort_seq[1:]

    sub_strs = substrings(shortest_str)

    for sub in sub_strs:
        if is_common_sub(sub, remain_strs):
            return sub
    return ''

print (is_lcsm(seqArr))
