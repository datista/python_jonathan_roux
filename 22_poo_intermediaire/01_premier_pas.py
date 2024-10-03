# personne (entity -> class)
# Données : nom, âge (attributs)
# Actions : (méthode)
#   - sePresenter()
#   - demanderNom() / input

#------------ Definition ------------
class Personne:
    def __init__(self, nom) -> None:
        print("Constructeur Personne " + nom)
        self.nom = nom  # -> Variable d'instance: nom
    
    def SePresenter(self):                # -> avec "self" : Methode d'instance
        print(f"Je m'appelle {self.nom}")

    def AutreFonction():                 # -> sans "self" : Methode statique ou méthode de class
        print("Autre fonction")
        
#------------ Utilisation ------------
personne1 = Personne("Jean") # Je crée une personne
personne1.SePresenter()
#personne2 = Personne("Paul") # Je crée une personne