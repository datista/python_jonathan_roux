import random

def demander_nombre (nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"Quel est le nombre magique (entre {nb_min} et {nb_max}) ?")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez.")
        else:
            if nombre_int < nb_min or nombre_int > nb_max :
                print(f"ERREUR: Le nombre doit être compris en {nb_min} et {nb_max}. Réessayez")
                nombre_int = 0

    return nombre_int

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)

nombre = demander_nombre (NOMBRE_MIN, NOMBRE_MAX)

while nombre != NOMBRE_MAGIQUE:
    if nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
    else:
        print("Le nombre magique est plus grand")
    nombre = demander_nombre (NOMBRE_MIN, NOMBRE_MAX)
print("Bravo, vous avez gagné")