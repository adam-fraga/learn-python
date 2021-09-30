datafile = "data.txt"

lines = open(datafile, "r").readlines()
string = ""
datastring = string.join(lines)
world_list = datastring.split()
count = 0

for word in world_list:
    if word.isalpha():
        count += 1

print("Il y a {} mots sans caractères spéciaux".format(count))
