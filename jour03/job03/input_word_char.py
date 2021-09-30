nb = input("Entrez un nombre\n")
nb = int(nb)
datafile = "data.txt"

lines = open(datafile, "r").readlines()
string = ""
new_string = string.join(lines)
list_words = new_string.split()
nb_word = 0

for word in list_words:
    if int(len(word)) == nb:
        nb_word += 1

print(nb_word)
