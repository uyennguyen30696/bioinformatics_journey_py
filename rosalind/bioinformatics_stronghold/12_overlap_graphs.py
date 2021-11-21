# A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.
# A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).
# For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

# Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.
# Return: The adjacency list corresponding to O3. You may return edges in any order.

# Problem breakdown
# The task is to print out the adjacent list of the overlap graph of the sequences with the overlap length of k = 3 bp
# We need to compare the suffixes of each sequence to prefixes of all other sequences
# If there is a match, print the id of the sequence containing the matched suffix to the left, and the id of the sequence with the matched prefix on the right

# k is the number of overlap bp
k = 3
g = open('output.txt', 'w')

# Read data from FASTA formatted file, return a list of line
def readFile(fastaFile):
    with open(fastaFile, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Store FASTA formatted data in the data varialbe for easy access
data = readFile('txt_files/12_rosalind_grph.txt')

# Reformat data and store in seqDict dictionary
seqDict = {}
seq_id = ""
for str in data:
    if str.startswith('>'):
        seq_id = ''.join(str.split('>')) 
        seqDict[seq_id] = ''
    else:
        seqDict[seq_id] += str

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def is_overlap(u, v, k):
    return u[-k:] == v[:k]

adjacency_list = []
def overlap_graph():
    for seq1 in seqDict:
        for seq2 in seqDict:
            if seq1 != seq2:
                if is_overlap(seqDict[seq1], seqDict[seq2], k):
                    adjacency_list.append((seq1, seq2))
    return adjacency_list
overlap_graph()

for edge in adjacency_list:
    print (edge[0], edge[1])

for edge in adjacency_list:
    g.write((' '.join(edge)) + '\n')
