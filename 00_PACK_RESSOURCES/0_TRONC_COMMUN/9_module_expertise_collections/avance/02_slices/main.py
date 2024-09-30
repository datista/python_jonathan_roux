# LES COLLECTIONS : LISTES / TUPLES
# Slices

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

# slices_noms = noms -> copie la référence
# slices_nomes = [:] -> copie les valeurs de noms dans slices_noms. En mémoire c'est donc 2 objets différents
# A chaque slice -> une nouvelle liste
slices_noms = noms[-2:] 

#noms[0] = "Toto"

print(slices_noms)
#print(noms)




