import time
import beepy

# for i in range(5):
#     time.sleep(1)
#     print(".", end="", flush=True)
    

# beepy.beep(sound="ping")

# d = 100
# min = d//100
# sec = d-min
# print(f"{min:02d}")

def afficher_minuteur(option_cuisson: str):
    duree_seconde = int(option_cuisson) * 60
    duree_en_dizaine_seconde = int(duree_seconde / 10)

    for i in range(duree_en_dizaine_seconde):
        duree_restante_seconde = duree_seconde - 10*i
        min = duree_restante_seconde//60
        sec = duree_restante_seconde - min*60
        print(f"Durée restante : {min:02d}:{sec:02d}", end="", flush=True)
        for i in range(10):
            time.sleep(1)
            print(".", end="", flush=True)
        print()
        duree_restante_seconde -= 10
    print("Fin")
    

choix = ""
while True:
    # Menu : choix du programme de cuisson
    print("Ce programme vous permet de choisir votre option de cuisson")
    print("1 - Oeufs à la coque : 3 minutes")
    print("2 - Oeufs mollets : 6 minutes")
    print("3 - Oeufs durs : 9 minutes")
    choix = input("Votre choix (1, 2 ou 3): ")
    if choix in ["1", "2", "3"]:
        break
    print("ERREUR : Vous devez choisir 1, 2 ou 3")

afficher_minuteur (choix)

beepy.beep(sound="ping")
