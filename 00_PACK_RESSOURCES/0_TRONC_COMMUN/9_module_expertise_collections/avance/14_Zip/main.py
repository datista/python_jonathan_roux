pizzas_nom = ("4 fromage", "Calzone", "Hawai")
pizzas_prix = (10.5, 11, 8)

nom_et_prix = zip(pizzas_nom, pizzas_prix) #-> Crée une liste de tuple composé des éléments de chaque liste. Ex: ("4 fromage", 10.5)
# Par contre on ne peut parcourir un objet zip, on ne pas pas l'afficher ...
#pour l'afficher il faut le mettre dans une liste

nom_et_prix2 = list(nom_et_prix)

for(nom, prix) in nom_et_prix2:
    print(f"{nom} - {prix}€")


for(nom, prix) in zip(pizzas_nom, pizzas_prix):
    print(f"{nom} - {prix}€")

# Pour deziper 
unziped = list(zip(*nom_et_prix2))

pn, pp = list(zip(*nom_et_prix2))