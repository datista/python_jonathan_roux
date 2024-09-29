
def message_erreur(nb_tentatives):
    print("ERROR: Vous devez rentrer 1 pour pouces vers cm et 2 pour cm vers pouce ")
    print(f"Il vous reste {nb_tentatives - 1} tentatives")

def convertion (sens, a_convertir):
    valeur = 0;
    if(sens == 1):
        valeur = a_convertir/2.54
    else:
        valeur = a_convertir * 2.54
    return valeur


def convertisseur ():
    nb_error = 3
    sens_int = 0
    unite = ""
    while sens_int == 0 and nb_error > 0:
        sens_str = input("Entrez: 1 pour pouces vers cm et 2 pour cm vers pouce ")
        try:
            sens_int = int(sens_str)
        except:
            message_erreur(nb_error)
            nb_error -= 1 
        else:
            if sens_int == 1:
                unite = "cm"
            elif sens_int == 2:
                unite = "pouces"
            else:
                message_erreur(nb_error)
                sens_int = 0
                nb_error -= 1 

    if nb_error == 0:
        return
    else :
        nb_error = 3
        while nb_error > 0:
            entree_str = input("Entrez: le nombre de " + unite + " à convertir ou @ pour sortir du convertisseur " )
            entree_int = 0
            try:
                entree_int = int(entree_str)
            except:
                print("Vous devez rentrer un nombre ")
                if entree_str == "@":
                    nb_error = 0
                else:
                    nb_error -= 1 
                    print(f"Il vous reste {nb_error - 1} tentative ")
            else:
                nb_error = 3
                valeur = convertion(sens_int, entree_int)
                if sens_int == 1:
                   print(f"{valeur} pouces ")
                elif sens_int == 2:
                   print(f"{valeur} cm")


convertisseur()