my_file = open("out.txt", "w")
my_file.write("Hello world\n")
# write "abcdef"
my_file.write("abc" + "def\n")
# write "8"
my_file.write(str(len('AGTGCTAG\n')))
# write "TTGC"
my_file.write("ATGC".replace('A', 'T'))
# write "atgc"
my_file.write("ATGC".lower())
# write contents of my_variable
my_data = open("gene.fa")
my_variable = my_data.read()
my_file.write(my_variable)
my_data.close()
my_file.close()


# Exercises

# 1-Splitting genomic DNA
seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGA\
TCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

exon1 = seq[:62] #consider that python start counting from 0

exon2 = seq[90:]

# Creating variable for coding and non coding sequences
coding_seq = exon1 + exon2

noncoding_seq = seq[62:90]

# Creating files for variables
coding_seq_file = open("coding.fa","w")

noncoding_seq_file = open("noncoding.fa", "w")

# Writing the variables in different files
coding_seq_file.write(coding_seq)

noncoding_seq_file.write(noncoding_seq)

# Closing the files
coding_seq_file.close()
noncoding_seq_file.close()

# 2-Writing a FASTA file
"""
Write a program that will create a FASTA file for the following three \
sequences – make sure that all sequences are in upper case and only contain\
the bases A, T, G and C.
"""
my_fasta = open("my_fasta.fa","w")

header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG"

# inserindo informaçoes da primeira sequencia
my_fasta.write(">" + header_1 + "\n" + seq_1 + "\n")

# inserindo informaçoes da segunda sequencia
my_fasta.write(">" + header_2 + "\n" + seq_2.upper() + "\n")

# inserindo informaçoes da terceira sequencia
my_fasta.write(">" + header_3 + "\n" + seq_3.replace("-","") + "\n")

my_fasta.close()


# 3-Writing multiple FASTA files

# set the values of all the header variables
header_1 = "ABC123"
header_2 = "DEF456"
header_3 = "HIJ789"

# set the values of all the sequence variables
seq_1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
seq_2 = "actgatcgacgatcgatcgatcacgact"
seq_3 = "ACTGAC-ACTGT—ACTGTA----CATGTG"

# make three files to hold the output
output_1 = open(header_1 + ".fasta", "w")
output_2 = open(header_2 + ".fasta", "w")
output_3 = open(header_3 + ".fasta", "w")

# write one sequence to each output file
output_1.write('>' + header_1 + '\n' + seq_1 + '\n')
output_2.write('>' + header_2 + '\n' + seq_2.upper() + '\n')
output_3.write('>' + header_3 + '\n' + seq_3.replace('-', '') + '\n')


