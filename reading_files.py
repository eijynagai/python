# In this section I am studying reading and writing files using python.
# I downloaded the first gene from E. coli and saved it as gene.fa

# reading files
my_file = open("gene.fa")

# It is not the same interaction of strings.
print(my_file)
# <open file 'gene.fa', mode 'r' at 0x10a7ac660>

# So working with files need different commands like:
file_contents = my_file.read()
print(file_contents)

# working with fasta or fastq files will bring an issue. How to deal with newlines?
my_file = open("gene.fa")
my_file_contents = my_file.read()
# then remove the newline from the end of the file contents
my_dna = my_file_contents.rstrip("\n")
dna_lentgh = len(my_dna)
print("sequence is " + my_dna + " and lentgh is " + str(dna_lentgh))

# or you can do it in only one line:
# my_dna = my_file.read().rstrip("\n")


