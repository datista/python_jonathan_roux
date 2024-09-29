import turtle

t = turtle.Turtle()
# Un escalier de 5 marches de 30 pixels
def escalier (taille, nb):
    t.forward(taille)
    for i in range(0, nb-1):
        t.left(90)
        t.forward(taille)
        t.right(90)
        t.forward(taille)
        taille -= 10

#carre
def carre(taille):
    for i in range(0, 3):
        t.forward(taille)
        t.left(90)
    t.forward(taille)

#escalier(60,5)
carre(50)
carre(100)
turtle.done()