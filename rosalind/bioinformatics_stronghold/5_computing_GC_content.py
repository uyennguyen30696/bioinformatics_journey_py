# The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.
# DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

# In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 

# I understand the problem and got the answer based on the solution from here, thank you!: https://www.youtube.com/watch?v=mw4FSbDro0A 

# Read data from FASTA formatted file, return a list of line
def readFile(fastaFile):
    with open(fastaFile, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Store FASTA formatted data in the data varialbe for easy access
data = readFile('txt_files/rosalind_gc.txt')

# Reformat data and store in seqDict dictionary
# seqDict = {
    # seq_id: str
# }
seqDict = {}
seq_id = ""
for str in data:
    if str.startswith('>'):
        seq_id = ''.join(str.split('>')) 
        seqDict[seq_id] = ''
    else:
        seqDict[seq_id] += str

# Calculate GC content in a sequence
def gc(seq):
    gc_percent = round(( (seq.count('G') + seq.count('C')) / len(seq) * 100), 6)
    return gc_percent

# Transform (key, value) from seqDict to percentage in finalDict
# finalDict = {
    # seq_id: percentage
# }
finalDict = {key: gc(value) for (key, value) in seqDict.items()}

# for key, value in finalDict.items():
maxKey = max(finalDict, key = finalDict.get)

print (maxKey)
print (finalDict[maxKey])
