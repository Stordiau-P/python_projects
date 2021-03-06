import turtle
t = turtle.Turtle()
# def escalier(taille,nb):
#     for i in range(0,nb):
#         t.forward(taille)
#         t.left(90)
#         t.forward(taille)
#         t.right(90)
#     t.forward(taille)
# escalier(20,7)
def carre(cote):
    for i in range(0,4):
        t.forward(cote)
        t.left(90)
def carres(taille,nb):
    for i in range (0,nb):
        carre((i+1)*taille)


carres(10,4)
turtle.done()