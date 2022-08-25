# A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC.

# Given: A DNA string of length at most 1 kbp in FASTA format.
# Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

# Note: numpy error in python vs code environment, run `pip install --upgrade --force-reinstall numpy`

# Brainstorm
# Dynamic programming? Break down into smaller problems
# A function to open file, reformat, and store data in a string
# A function for reverse palindrome, reverse the DNA, then find the compliment strand of the reversed
# A function to find the starting position (starting from 1, not 0) of the reverse palindrome, length ranging from 4 to 12
# A function to print position and length in pairs (use dictionary)

# Reformat FASTA file and store sequence data in an array, using Biopython library
from Bio import SeqIO 

def open_file():
    seq = ''
    file = open('txt_files/21_rosalind_revp.txt', 'r')
    for seq_record in SeqIO.parse(file, 'fasta'):
        for nt in seq_record:
            seq += nt
    return seq

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Reverse complement dna
def reverse_complement_dna(dna):
    complement = { 'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G' }
    reverse_complement = ''.join(complement.get(base, base) for base in reversed(dna))
    return reverse_complement

# Check if reverse compliment
def is_reverse_complement(dna):
    return dna == reverse_complement_dna(dna)

# Find restriction sites (the starting position of the reverse palindrome)
def restriction_sites(dna):
    # Note: do NOT use dictionary here because the key will be unique, 
    # which will overshadow the shorter length version starting at the same position
    # Ex: seq starting at 64, len = 4 will not be counted because seq starting at 64, len = 10 will be counted instead (same key = 64 in dict)
    result = []             
    for length in range(4, 13):
        for position in range((len(dna) - length) + 1):
            if is_reverse_complement(dna[position : position + length]):
                # The returned position starts with 1 instead of 0
                result.append(str(position + 1) + ' ' + str(length))
    return result

if __name__ == "__main__":
    dna = open_file()
    reverse_complement = reverse_complement_dna(dna)
    reverse_panlindrome = restriction_sites(dna)
    
    for dna in reverse_panlindrome:
        print (dna)
