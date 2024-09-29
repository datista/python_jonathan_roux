""" Premier programme
Formation python
apprendre la programmation """

nom = input("Quel est votre nom ? ")
age = input("Quel est votre age ? ")

try:
    age_prochain = int(age) + 1
except:
    print("ERREUR :  Vous devez un nombre pour l'âge")
else:
    print("Vous vous appelez " + nom + ", vous avez " + age + " ans")
    print("L'an prochain vous aurez "+ str(age_prochain) + " ans")