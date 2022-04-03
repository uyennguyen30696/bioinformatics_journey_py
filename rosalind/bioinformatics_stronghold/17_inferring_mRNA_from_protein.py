# Given: A protein string of length at most 1000 aa.
# Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)

rnaCodons = {
    'UUU':'F',  'UUC':'F',   'UUA':'L',    'UUG':'L',
    'UCU':'S',  'UCC':'S',   'UCA':'S',    'UCG':'S',
    'UAU':'Y',  'UAC':'Y',   'UAA':'Stop', 'UAG':'Stop',
    'UGU':'C',  'UGC':'C',   'UGA':'Stop', 'UGG':'W',
    'CUU':'L',  'CUC':'L',   'CUA':'L',    'CUG':'L',
    'CCU':'P',  'CCC':'P',   'CCA':'P',    'CCG':'P',
    'CAU':'H',  'CAC':'H',   'CAA':'Q',    'CAG':'Q',
    'CGU':'R',  'CGC':'R',   'CGA':'R',    'CGG':'R',
    'AUU':'I',  'AUC':'I',   'AUA':'I',    'AUG':'M',
    'ACU':'T',  'ACC':'T',   'ACA':'T',    'ACG':'T',
    'AAU':'N',  'AAC':'N',   'AAA':'K',    'AAG':'K',
    'AGU':'S',  'AGC':'S',   'AGA':'R',    'AGG':'R',
    'GUU':'V',  'GUC':'V',   'GUA':'V',    'GUG':'V',
    'GCU':'A',  'GCC':'A',   'GCA':'A',    'GCG':'A',
    'GAU':'D',  'GAC':'D',   'GAA':'E',    'GAG':'E',
    'GGU':'G',  'GGC':'G',   'GGA':'G',    'GGG':'G'
}

def codon_frequency():
    f = {}
    for key, value in rnaCodons.items():
        if value not in f:
            f[value] = 0
        f[value] += 1
    
    return f

def possible_rna(protein_seq):
    f = codon_frequency()
    stop_codon_f = f['Stop']
    possible_seq = stop_codon_f

    for seq in protein_seq:
        possible_seq *= f[seq]

    return possible_seq % 1000000

protein_seq = open('txt_files/17_rosalind_mrna.txt', 'r').read().strip()
print (possible_rna(protein_seq))
