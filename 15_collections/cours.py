# Collections : (Tableau : Array), Listes, Tuples ...
# Tuple (): immutable -> non modifiable
# Liste []: mutable -> modifiable -> rajouter/supprimer des éléments ou les modifier
# Le dernier élément d'une liste ou d'un tuple -> [-1]
# Range fonctionne comme un tuple
# Pourquoi utiliser un tuple et non une liste : le tuple utilise moins de mémoire -> plus performance, dans certains cas les accès sont plus rapide

########################## Tuple ##############################
# personnes = ("Mélanie", "Jean", "Martin", "Alice") # Un tuple

# for i in range(len(personnes)):
#     print(personnes[i]) 

# print()

# for personne in personnes:
#     print(personne)
#     print(len(personne))
#     print(personne[i])

########################## Listes ##############################
personnes = ["Mélanie", "Jean", "Martin", "Alice"] # Un tuple

for i in range(len(personnes)):
    print(personnes[i]) 

print()

for personne in personnes:
    print(personne)
    print(len(personne))
    print(personne[i])


########################## Fonctions et tuples ##############################

def obtenir_informations():
    return "Melanie", 37, 1.60 # -> retourne un tuple

def afficher_informations(nom, age, taille):
    print(f"Nom: {nom}, age: {age}, taille: {taille}") 

infos = obtenir_informations()
print(f"Nom: {infos[0]}") # - > Mélanie

nom, age, taille = obtenir_informations() # - > la façon la plus recommandées

afficher_informations(nom, age, taille)
afficher_informations( *infos )

print(infos) # -> on a bien un tuple avec les parenthèses
print(*infos) # -> se comporte comme un print avec les paramètre séparés. On dit qu'on unpack le tuple


########################## slices tuple/liste ##############################
personnes = ["Mélanie", "Jean", "Martin", "Alice", "Pierre", "Paul"] # Un tuple

#[start:stop:step] -> slice
#[:] -> l'ensemble
#[::2] -> l'ensemble en sautant de 2 en 2
#[::-1] -> il affiche tout mais dans le sens opposé

for i in personnes[0:2]:
    print(i)