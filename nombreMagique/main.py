import random
def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:

        try :
            nombre_str = input(f"Quel est le nombre magique (entre {nb_min} et {nb_max})")
            nombre_int = int(nombre_str)
        except:
            print("veuillez entrer un nombre valide")
        else :
            if nombre_int > nb_max or nombre_int < nb_min :
                print(f"Veuillez indiquer un nombre entre {nb_min} et {nb_max}")
                nombre_int=0
    return nombre_int


NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN,NOMBRE_MAX)
nombre=0
NB_VIES = 4
vies = NB_VIES
while nombre != NOMBRE_MAGIQUE and vies != 0:
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo vous avez gagné !")
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit")
        vies -=1
    else:
        print("le nombre est plus grand")
        vies -=1

if vies == 0:
    print(f"Vous avez perdu le nombre magique était {NOMBRE_MAGIQUE}")