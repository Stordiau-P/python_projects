from random import randrange
from math import ceil
money = 500

while True :
    mise = int(input("Combien voulez-vous miser ?"))
    number = int(input("Sur quel numéro voulez-vous miser ?"))
    random_number = randrange(50)
    if random_number == number :
        money = money + mise*3
    elif random_number % 2 == number % 2 :
        money = money + ceil(mise*(1+0.5))
    else :
        money = money - mise
    print("Il vous reste ",money,"$")