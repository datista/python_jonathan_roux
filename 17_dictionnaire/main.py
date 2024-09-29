########################### partie 1 ##################
# personne = {"nom":"Mélanie", "age":25, "taille" : 1.60}

# print(personne)
# print(personne["nom"])

# personne["nom"] = "Claire"

# print(personne)

# personne["poste"] = "Développeur"

# print(personne)

# achat = ("chocolat", "beurre", "fromage")

# personne["achat"] = achat

# print(personne)

# for k in personne:
#     print(k)
#     print(personne[k])
#     print(f"Clé: {k} - Valeur: {personne[k]}")

########################### partie 2 ##################

personnes = [
    ("Melanie", 25, 1.6),
    ("Paul", 29, 1.8),
    ("Jacque", 35, 1.75),
    ("Martin", 16, 1.65),
]

def obtenir_informations(nom, liste):
    for i in liste:
        if i[0] == nom:
            return i
    return None

# Jacques
infos = obtenir_informations("Jacques", personnes)
# print(infos)

personne_dict = {
    "Melanie": (25, 1.6),
    "Paul": (29, 1.8),
    "Jacque": (35, 1.75),
    "Martin": (16, 1.65)   
}

infos = personne_dict["Jacque"] # Génère une erreur quand il ne trouve pas
infos = personne_dict.get("Jacques") # A privilégier, car il retourne None, s'il ne trouve rien 

print(infos)

# Penser au dictionnaire quand on a un très grand nombre de données sur lesquelles bouclées