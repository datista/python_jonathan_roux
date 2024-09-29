def multiplication(nombre):
    for i in range(10):
        print(f"{nombre} * {i+1} = {(i+1)*nombre}")



# Menu : choix du numero de la table
print("Ce programme propose la table de multiplication du numéro que vous rentrez")
while True:
    numero = input("Entrez le numéro de la table de multiplication : ")
    if numero == "q":
        break
    multiplication(int(numero))
    