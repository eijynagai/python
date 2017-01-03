#Lists and loops

#classifying the elements of the list
ranks = ["kingdom", "phylum", "class", "order", "family"]
print(ranks)
ranks.reverse()
print(ranks)
#print(ranks.reverse()) -> this command doesn't work 
ranks.sort()
print(ranks)

apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
for i in apes:
    print(i + " is an ape")
print("Everybody in the group are ape")    

#creating list from a string
names = "melanogaster, simulans, yakuba, ananassae"
species = names.split(",")
for i in species:
    print(i)


###############################
# when working with a file and for, each line is an element.
file = open("some_input.txt")
for line in file:
    # do something with the line

# Chapter 4 - Working with loops with ranges (pag. 85)


