# Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.
# An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

# Given: A DNA string s of length at most 1 kbp in FASTA format.
# Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be retTrned in any order.


# FASTA format to string of dna

# Replace all the U in the rna codon by T to reverse the table from rna to dna
# Loop throTgh dna string to look for start codon (AUG -> ATG -> M)
# If ATG, start translating until stop codon
# Continue
# Reverse dna string, find complement string of it, and apply the loop over again

from Bio import SeqIO

file = open('txt_files/18_rosalind_orf.txt', 'r')
dna = ''
for seq_record in SeqIO.parse(file, 'fasta'):
    for nt in seq_record:
        dna += nt
file.close()

dnaCodons = {
    'TTT':'F',  'TTC':'F',   'TTA':'L',    'TTG':'L',
    'TCT':'S',  'TCC':'S',   'TCA':'S',    'TCG':'S',
    'TAT':'Y',  'TAC':'Y',   'TAA':'Stop', 'TAG':'Stop',
    'TGT':'C',  'TGC':'C',   'TGA':'Stop', 'TGG':'W',
    'CTT':'L',  'CTC':'L',   'CTA':'L',    'CTG':'L',
    'CCT':'P',  'CCC':'P',   'CCA':'P',    'CCG':'P',
    'CAT':'H',  'CAC':'H',   'CAA':'Q',    'CAG':'Q',
    'CGT':'R',  'CGC':'R',   'CGA':'R',    'CGG':'R',
    'ATT':'I',  'ATC':'I',   'ATA':'I',    'ATG':'M',
    'ACT':'T',  'ACC':'T',   'ACA':'T',    'ACG':'T',
    'AAT':'N',  'AAC':'N',   'AAA':'K',    'AAG':'K',
    'AGT':'S',  'AGC':'S',   'AGA':'R',    'AGG':'R',
    'GTT':'V',  'GTC':'V',   'GTA':'V',    'GTG':'V',
    'GCT':'A',  'GCC':'A',   'GCA':'A',    'GCG':'A',
    'GAT':'D',  'GAC':'D',   'GAA':'E',    'GAG':'E',
    'GGT':'G',  'GGC':'G',   'GGA':'G',    'GGG':'G'
}

# Reverse complement dna
def reverse_complement_dna(dna):
    complement = { 'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G' }
    reverse_complement = ''.join(complement.get(base, base) for base in reversed(dna))
    return reverse_complement

# Start codon = ATG encoding M amino acid
# This function is applied to the dna and then the reverse complement dna
def translated_protein(seq):
    start_positions = []
    proteins_list = []
    CODON_LEN = 3
    
    for i in range(0, len(seq)):
        if seq[i:i+3] == 'ATG':
            start_positions.append(i)

    for i in range(0, len(start_positions)):
        detect_stop = False
        protein = ''
        for j in range(start_positions[i], len(seq[:len(seq) // 3 * 3]) - 3, CODON_LEN):   # len(seq[:len(seq) // 3 * 3]) in case len(seq) is not divisable by 3 (CODON_LEN)
            codon = dnaCodons[seq[j:j+3]]
            if codon == 'Stop':
                detect_stop = True
                break
            protein += codon

        # The possible protein must start with start codon and end with stop codon
        if detect_stop == True:
            proteins_list.append(protein)
    
    return proteins_list

if __name__ == "__main__":
    forward_translate = translated_protein(dna)
    reverse_translate = translated_protein(reverse_complement_dna(dna))

    print ('\n'.join(set(forward_translate + reverse_translate)))  # Return no duplicate
