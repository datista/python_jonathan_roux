import time
import random
import os


def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')
    
sequenceJoueur = ""
laBonneSequence = str(random.randint(1000, 9999))
scoreJoueur = 0
while True:
    print("Retenez la squence:")
    print(laBonneSequence)
    time.sleep(3)
    clear_screen()
    sequenceJoueur = input("Votre séquence : ")
    if sequenceJoueur != laBonneSequence :
        print("Perdu, la bonne séquence est : " + laBonneSequence)
        print(f"Votre score : {scoreJoueur}")
        break
    scoreJoueur += 1
    print("Bonne réponse !")
    print(f"Votre score : {scoreJoueur}")
    laBonneSequence = laBonneSequence + str(random.randint(0,9))
    time.sleep(3)
    clear_screen()

