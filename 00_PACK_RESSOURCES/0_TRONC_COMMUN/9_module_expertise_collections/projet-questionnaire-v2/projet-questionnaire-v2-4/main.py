# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions
#
# Class Question
#   - données : 
#       - titre -> str
#       - choix -> (str)
#       - bonne_reponse -> str
#   - action : 
#       - poser() -> bool
# Class questionnaire
#   - données : 
#       - questions : (Question)
#   - Action :  
#       - lancer_questionnaire ()poser question, 
#

class Question:
    def __init__(self, titre: str, choix: str, reponse: str ) -> None:
        self.titre = titre
        self.choix = choix
        self.reponse = reponse

    def poser(self):
        print("QUESTION")
        print("  " + self.titre)
        for i in range(len(self.choix)):
            print("  ", i+1, "-", self.choix[i])

        print()
        resultat_correct = False
        reponse_int = Question.demander_reponse_numerique_utlisateur(1, len(self.choix))
        if self.choix[reponse_int-1].lower() == self.reponse.lower():
            print("Bonne réponse")
            resultat_correct = True
        else:
            print("Mauvaise réponse")
            
        print()
        return resultat_correct

    def demander_reponse_numerique_utlisateur(min, max):
        reponse_str = input("Votre réponse (entre " + str(min) + " et " + str(max) + ") :")
        try:
            reponse_int = int(reponse_str)
            if min <= reponse_int <= max:
                return reponse_int

            print("ERREUR : Vous devez rentrer un nombre entre", min, "et", max)
        except:
            print("ERREUR : Veuillez rentrer uniquement des chiffres")
        return Question.demander_reponse_numerique_utlisateur(min, max)
    
class Questionnaire:
    def __init__(self, questions) -> None:
        self.questions = questions

    def lancer_questionnaire(self):
        score = 0
        for q in self.questions:
            if(q.poser()):
                score += 1
        print(f"Score final : {score} / {len(self.questions)}")



Questionnaire((
    Question("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes", "Lille"), "Paris"),
    Question("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome"),
    Question("Quelle est la capitale de la Belgique ?", ("Rome", "Bruge", "Pise", "Bruxelles"), "Bruxelles")
)).lancer_questionnaire()
