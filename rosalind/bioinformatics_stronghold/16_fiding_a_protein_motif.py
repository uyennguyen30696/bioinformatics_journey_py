# Given: At most 15 UniProt Protein Database access IDs.
# Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

from Bio import SeqIO
import requests         # To install requests, run 'pip install requests'
import re               # To use regex

# Open the given file and store data in the id_data_list
dataFile = open('txt_files/16_rosalind_mprt.txt')
id_data_list = dataFile.read().splitlines()
dataFile.close()

# Download data from uniprot to a new file in fasta format
uniprotFile = open('id_uniprot.txt', 'w')
for id in range(0, len(id_data_list)):
    url = 'http://www.uniprot.org/uniprot/' + id_data_list[id] + '.fasta'
    r = requests.get(url).text
    uniprotFile.write(r)

# Helper function to convert data from fasta format and store in a dictionary
# Replace id from uniprot by id in the provided data file because they are in different format
uniprotFile = open('id_uniprot.txt', 'r')
def parse_fasta(uniprotFile):
    dnaList = []
    for seq_record in SeqIO.parse(uniprotFile, 'fasta'):
        seq = ''
        for nt in seq_record:
            seq += nt
        dnaList.append(seq)

    seq_dict = {}
    seq_id = ''
    for i in range(0, len(id_data_list)):
        seq_id = id_data_list[i]
        seq_dict[seq_id] = dnaList[i]

    return seq_dict

# Search for matched motif in each sequence
def search_motif():
    seq_dict = parse_fasta(uniprotFile)
    motif = r'(?=N[^P][ST][^P])'

    for id, value in seq_dict.items():
        locations = [m.start() + 1 for m in re.finditer(motif, value)]   # Refer to python regex docs for more info
        if len(locations) != 0:
            print (id)
            print (' '.join(map(str, locations)))

search_motif()
uniprotFile.close()
