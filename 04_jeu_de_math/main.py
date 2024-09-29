import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10

def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    str_ab = input(f"Calculer {a} + {b} : ")
    int_ab = int(str_ab)

    if int_ab == (a+b): 
        print("Réponse correcte")
    else:
        print("Réponse incorrete")

poser_question()