import xml.etree.ElementTree as ET


domainXML = "domains.xml"
tree = ET.parse(domainXML)
root = tree.getroot()

ET.dump(tree)

print("------------------------------------------")

i = 0
elements = []
domains = 0

# Itere sur chaque noeuf columun et récupère le contenur txt pour l'inserer dans un tableau
# 1 element sur 2 étant un domain applique un modulo si le resultat n'est pas multiple de 2 il s'agit d'un domaine

for el in root.findall(".//column"):
    elements.append(el.text)

for item in elements:
    i += 1
    if i % 2:
        ""
    else:
        domains += 1

print("Il y a {} Nom de domaines dans le fichier".format(domains))
