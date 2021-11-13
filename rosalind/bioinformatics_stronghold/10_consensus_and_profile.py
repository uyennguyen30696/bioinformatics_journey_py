# A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns. Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.
# Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).
# A consensus string c is a string of length n formed from our collection by taking the most common symbol at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

#                 A T C C A G C T
#                 G G G C A A C T
#                 A T G G A T C T
# DNA Strings	  A A G C A A C C
#                 T T G G A A C T
#                 A T G C C A T T
#                 A T G G C A C T

#             A   5 1 0 0 5 5 0 0
# Profile	  C   0 0 1 4 2 0 6 1
#             G   1 1 6 3 0 1 0 0
#             T   1 5 0 0 0 1 1 6

# Consensus	      A T G C A A C T

# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

# Convert FASTA file into an array of dna strings, no name, each line is a fragment of one string it belongs to
f = open('txt_files/10_rosalind_cons.txt', 'r')
g = open('output', 'w')
dna_strings = []
fragments = []
for line in f:
    if line.startswith('>'):
        if fragments:
            dna_strings.append(''.join(fragments))
            fragments = []
    else:
        fragments.append(line.rstrip())
if fragments:
    dna_strings.append(''.join(fragments))

# Create the profile with A, C, G, T frequencies in each dna string
profile = []
for i in range(len(dna_strings)):
    profile.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
# Iterate through each dna string, then iterate through each nucleotide in each string
for i in range(len(dna_strings)):
    for j in range(len(dna_strings[i])):
        # Count the frequency of each nucleotide in each dna string
        profile[i][dna_strings[i][j]] += 1

concensusArr = []
# Treat each of the profile[i] as a dictionary
for i in range(len(profile)):
    common_symbol = max(profile[i], key=profile[i].get)
    concensusArr.append(common_symbol)
    concensus = ''.join(concensusArr)
print (concensus)

# Format the profile table to print
profileA_Arr = []
profileC_Arr = []
profileG_Arr = []
profileT_Arr = []
for i in range(len(profile)):
    profileA_Arr.append(profile[i]['A'])
    profileA = 'A: ' + ''.join(str(profileA_Arr)).strip('[]').replace(',', '')

    profileC_Arr.append(profile[i]['C'])
    profileC = 'C: ' + ''.join(str(profileC_Arr)).strip('[]').replace(',', '')

    profileG_Arr.append(profile[i]['G'])
    profileG = 'G: ' + ''.join(str(profileG_Arr)).strip('[]').replace(',', '')

    profileT_Arr.append(profile[i]['T'])
    profileT = 'T: ' + ''.join(str(profileT_Arr)).strip('[]').replace(',', '')

print (profileA + '\n' + profileC + '\n' + profileG + '\n' + profileT)

g.write(concensus)
g.write(concensus + '\n' + profileA + '\n' + profileC + '\n' + profileG + '\n' + profileT)
