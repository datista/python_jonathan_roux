# LES COLLECTIONS : LISTES / TUPLES
# join et split

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

# Join : Rejoindre -> coller avec un séparateur (ex: csv)

noms_join = ", ".join(noms)
print(noms_join)

# Split : Séparer, extrait une chaine avec séparateur (ex: un csv)
# a = "Paul-Marc-Emilie"
#a_split = a.split("-")
#print(a_split)

noms_resconstruits = noms_join.split(", ")
print(noms_resconstruits)
