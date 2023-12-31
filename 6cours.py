
def table7():
    n=1
    while n <11:
        print(n*7, end=" ")
        n=n+1

table7()

def table(base):
    n=1
    while n <11:
        print(n*base, end=" ")
        n=n+1

print("Voici la table de 13")
table(13)

def tableMulti(base, debut, fin):
    print("La table de multiplication par", base)
    n=debut
    while n <=fin:
        print(n, "x", base, "=", n*base)
        n=n+1
tableMulti(8, 13, 17)


def test(base):
    resultat=[]
    n=1
    while n < 11:
        b = n*base
        resultat.append(b)
        n=n+1
    return resultat
test(7)

#tuples
def test():
    return 3,4  #retourne par 3 et 4
a = test()

# exo on utilise ça
#réutilise fonctions de façon jolie comme dans le dico : 
#flux d'execution
#materiau = input("Choix: ")
#dico = {"fer": FonctionA,
        #bois": FonctionC}
#dico[materiau]()

import math
print(math.sqrt(16))
   
from turtle import * 
forward(120)
left(90)
color("red")
forward(80)

reset()
a=0
while a <12:
    a=a+1
    forward(300)
    left(150)
    color("blue")

    
