# Collections : Le Set
# Collection sans doublon
# On peut l'ennumérer, mais pas l'indexer : -> on peut bouclé dans un for, mais on ne peut pas y aller avec des crochets
# Pas de notion d'ordre
#

'''noms = ["Marie", "Paul", "Jean", "Marc", "Emilie", "Marie"]
noms_sans_doublons = list(set(noms))
print(noms_sans_doublons)
print(noms_sans_doublons[0])'''

set_noms = { "Marie", "Paul", "Jean", "Marc", "Emilie", "Marie" }
print(set_noms)

# for s in set_noms:
#     print(s)