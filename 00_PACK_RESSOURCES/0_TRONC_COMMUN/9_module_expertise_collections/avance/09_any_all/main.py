# LES COLLECTIONS : LISTES / TUPLES
# Any et All -> ne fonctionnent qu'avec des bouleen (True ou False)
# Any : Quelconque / n'importe quel => Retourne True, si au moins un des éléments est True
# All : Tous ==> retourne True, si et seulement si tous les éléments sont à True

#          0        1        2           3           4      5
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe", "Martin"]

'''a = [True, True, True, True]
print(any(a))
print(all(a))'''


'''found = False
for nom in noms:
    if "z" in nom.lower():
        found = True
        break

if found:
    print("Trouvé")
else:
    print("Non trouvé")'''

nom_avec_un_z_existe = any([True if "z" in nom.lower() else False for nom in noms])
tous_nom_avec_un_e = all([True if "e" in nom.lower() else False for nom in noms])
if nom_avec_un_z_existe:
    print("Trouvé")
else:
    print("Non trouvé")
