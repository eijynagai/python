# Manipulating texts
# Using the book "Python for biologists" as a guide

# Concatenation
my_dna = "ATTC" + "GCTA"
print(my_dna)

upstream = "AAA"
my_dna = upstream + "CCGTACGAATT"
print(my_dna)

# len and str
print("The length of my dna is " + str(len(my_dna)))

# lower and upper functions
word = "AaaTTcCGaGC"
print("You can choose use lower case, as " + str(word.lower()) + " or upper \
case, as in " + word.upper())

# Replacement
protein = "vlspadktnv"
# replace valine with tyrosine
print(protein.replace("v", "y"))
# we can replace more than one character
print(protein.replace("vls", "ymt"))
# the original variable is not affected
print(protein)

# Extracting part of the string
protein = "pasldvpldsvpdsvlpsdlvsplvpdslvpsldvllvlvlavpsdds"
print(protein[2:10])

# Counting and finding substrings
count_v = protein.count("v")
print(protein)
print("Number of valine in protein: " + str(count_v))

print("Positions of valine in the sequence: " + str(protein.find("v")))

# Exercises

# Calculating AT content in a DNA sequence
dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
dna_test = "ATCG"
a_sum = dna.count("A")
t_sum = dna.count("T")
at_content = (a_sum+t_sum)*1.0/len(dna)
print("AT content in the DNA sequence is " + str(at_content) + ".")

# Complementing DNA
dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print(dna)
comp = dna.replace("A","t")
comp = comp.replace("T","a")
comp = comp.replace("G","c")
comp = comp.replace("C","g")
print(comp.upper())

# Restriction fragment lengths
dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
motif = "GAATTC"
motif_pos = dna.find(motif) + 1
print("First part of the sequence: " + str(len(dna[:motif_pos])))
print("Second part of the sequence: " + str(len(dna[motif_pos:])))

# Splicing out introns, part one
seq = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGA\
TCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = seq[:62] #consider that python start counting from 0
exon2 = seq[90:]
print(exon1+exon2)

# Splicing out introns, part two
coding_seq = exon1 + exon2
exon_len = len(coding_seq)
intron_len = len(seq) - exon_len
print("Coding part is " + str(exon_len*100/(intron_len+exon_len)) + "%.")

# Splicing out introns, part three
seq_final = exon1 + seq[62:90].lower()  + exon2
print(seq_final)
