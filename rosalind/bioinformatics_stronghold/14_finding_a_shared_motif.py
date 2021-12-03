# A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".
# Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

# This lenghty FASTA reformat needs improvement
# Read data from FASTA formatted file, return a list of line
def readFile(fastaFile):
    with open(fastaFile, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Store FASTA formatted data in the data varialbe for easy access
data = readFile('txt_files/14_rosalind_lcsm.txt')

# Reformat data and store in an dictionary
seqDict = {}
seq_id = ''
for str in data:
    if str.startswith('>'):
        seq_id = ''.join(str.split('>')) 
        seqDict[seq_id] = ''
    else:
        seqDict[seq_id] += str

# Store value in an array
seqArr = []
for key in seqDict:
    seqArr.append(seqDict[key])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Sort and get the shortest sequence
sort_seq = sorted(seqArr, key=len)
shortest_seq = sort_seq[0]
seqs = sort_seq[1:]
motif = ''

# Compare each substring in the shortest seq to each of the remaining seq
for i in range(len(shortest_seq)):
    for j in range(i, len(shortest_seq)):
        substring = shortest_seq[i:j+1]
        present = True
        for each in seqs:
            if substring not in each:
                present = False
                break
            else:
                present = True
        if present and len(substring) > len(motif):
            motif = substring
        j += 1

print (motif)
