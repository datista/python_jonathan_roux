# LES COLLECTIONS : LISTES / TUPLES
# index, find et count
# index -> trouve l'index d'une valeur passée en paramètre. Lève une exception si l'élément n'existe pas dans la collection. On peut préciser à partir quel index
# count -> compter le nombre d'occurrence d'un élément 
# find fonctionne comme index, mais uniquement pour les chaines de caractère, pas les collections !
#
#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]


element_cherche = "Martin"
nb_occurences = noms.count(element_cherche)
print("nb_occurences", nb_occurences)
if nb_occurences > 0:
    index_occurence = 0
    for i in range(nb_occurences):
        index_occurence = noms.index(element_cherche, index_occurence)
        print(element_cherche, "trouvé à", index_occurence)
        index_occurence += 1
else:
    print("L'élément n'est pas dans la collection")

