# LES COLLECTIONS : LISTES / TUPLES
# Operations sur les éléments : min, max, in, sum

# min, max sur une liste de chaine de caractère, se base sur l'ordre alphabétic
# sum ne s'utilise que sur des valeurs numériques

#          0        1        2           3           4
noms = ["Jean", "Sophie", "Martin", "Christophe", "Zoe"]

ages = [21, 20, 30, 25, 22]

'''if 31 in ages:
    print("Présent")
else:
    print("Abscent")'''

'''found = False
for nom in noms:
    if nom == "Martin":
        found = True
        break
if found:
    print("Présent")
else:
    print("Abscent")'''

print(sum(ages))

