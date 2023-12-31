#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 12:19:59 2023

@author: patricia
"""

print("You can do it !")
print("Love Yourself !")

#Séance 1 

#Exercice cours 
a, b, c, d = 3,4,5,7
print(a)
b, a, c, d = 3,4,5,7
print(a)

#Exercice Maison

#1)
#Faire un test pour savoir si a est compris dans
#l’intervalle allant de 2 à 8

a = 1

if 2 <= a <= 8 :
    print("oui")
else:
    print("non")
    
#2) 
#Afficher les 10 premiers termes de la table de
#multiplication par 5.

for i in range(11):
    print(i, "x 5 =", i*5)

#3) 
#Afficher les 10 premiers termes de la table de
#multiplication par 5, en signalant au passage (à
#l’aide d’un astérisque) ceux qui sont des
#multiples de 3.

for i in range(11):
    print(i*5)
    if i%3==0:
        print("*")
    else : 
        print("")

for i in range(11) :
    a = i*5
    if a %3==0 :
        print(a, "*")
    else:
        print(a)


#4
#Afficher une suite de 10 nombres dont chaque
#terme soit égale au triple du terme précédent

#Suite de Fibonacci : 
#Une suite de nombres dont chaque terme est égal à la
#somme des deux termes qui le précèdent

a, b, c = 1,1,1
while c<11 : 
    print(b, end=" ")
    a,b,c = b, a+b, c+1
# Résultat : 1 2 3 5 8 13 21 34 55 89     

a=1
for i in range (10):
    a = a*3 
    print(a)

a, b, c, d = 1,1,1,1
while d<11 : 
    print(c, end=" ")
    a,b,c,d = b,c, a+b+c, d+1

#1)
#Faire un test pour savoir si a est compris dans
#l’intervalle allant de 2 à 8
a=11
if 2<= a <= 8 :
    print("oui")
else : 
    print("non")

#2) 
#Afficher les 10 premiers termes de la table de
#multiplication par 5.
for i in range(11):
    a=i*5
    print(i,"x 5 =", a)


#3) 
#Afficher les 10 premiers termes de la table de
#multiplication par 5, en signalant au passage (à
#l’aide d’un astérisque) ceux qui sont des
#multiples de 3.
for i in range(11):
    a=i*5
    print(i,"x 5 =", a, end=" ")
    if a%3==0 :
        print("*")
    else:
        print("")

#4
#Afficher une suite de 10 nombres dont chaque
#terme soit égale au triple du terme précédent
a = 1

for i in range(11):
    print(a)
    a = a*3

#feuille 

r , pi = 12, 3.14159
s = pi * r**2
print(s)
print(type(r), type(pi), type(s))
#type = int, float (décimaux), str

####################################
#Écrivez un programme qui affiche les 20 
#premiers termes de la table de multiplication 
#par 7.
for i in range(21):
    a = i*7
    print(i, "x = 7 =", a)
    
#4.3 Écrivez un programme qui affiche une 
#table de conversion de sommes d’argent 
#exprimées en euros, en dollars canadiens. 
#La progression des sommes de la table sera 
#« géométrique »,comme dans l’exemple ci-dessous :
#1 euro(s) = 1.65 dollar(s)
#2 euro(s) = 3.30 dollar(s)
#4 euro(s) = 6.60 dollar(s)
#8 euro(s) = 13.20 dollar(s)
#etc. (S’arrêter à 16384 euros.)

a = 1
while a < 16384:
    print(a, "euro(s) =", a*1.65, "dollar(s)")
    a = a*2

#4.4 Écrivez un programme qui affiche une suite de 12 nombres dont chaque terme soit égal au
#triple du terme précédent.

a = 1
for i in range(13):
    a = a*3
    print(a)

#4.6 ) Écrivez un programme qui convertit 
#un nombre entier de secondes fourni au 
#départ en un nombre d’années, de mois, de jours,
#de minutes et de secondes 
#(utilisez l’opérateur modulo : %).

NbrSeconde = 1234567890

NbrSecondeJ = 3600 * 24
NbrSecondeM = NbrSecondeJ * 30
NbrSecondeA = NbrSecondeM * 365

print("On a :", NbrSeconde, "secondes")
a = NbrSeconde%NbrSecondeJ
print("Dans une journée, on a", a, "secondes")
b = NbrSeconde//NbrSecondeJ
print("Mais, il en reste : ",b)

c = NbrSeconde%NbrSecondeM
print("Dans un moi, on a", c, "secondes")
d = NbrSeconde // NbrSecondeM
print("Mais, il en reste : ",d)

d = NbrSeconde%NbrSecondeA
print("Dans un moi, on a", d, "secondes")
e = NbrSeconde // NbrSecondeA
print("Mais, il en reste : ",e)

#4.9 :
#Écrivez un programme qui affiche la suite de symboles suivante :
#*
#**
#***
#****
#*****
#******
#*******
for i in range(8):
    print("*"*i)

#5.1 : 
#Écrivez un programme qui convertisse en 
#radians un angle fourni au départ en degrés,
#minutes, secondes.
deg, min, sec = 90, 8, 100

#5.3 :
#Écrivez un programme qui convertisse en 
#degrés Celsius une température exprimée au départ
#en degrés Fahrenheit, ou l’inverse.
#La formule de conversion est : 
#T F =T C ×1,832 .
temps = 25
print("Il fait", temps , "°C")
tempsF = temps*1.8+32
print("Il fait",tempsF, "°F")

F = 77
print("Il fait", F, "°F")
C = (F-32)/1.8
print("Il fait :", C, "°C")

#5.5 :
#1 seul sur la première case du jeu qu’il 
#venait d’inventer, deux sur la suivante, 
#quatre sur la troisième, 
#et ainsi de suite jusqu’à la 64 e case.
c = 1
r = 1

for c in range (1,65) :
    print(c, "=", r)
    r = r*2






    




#5.5 :
#1 seul sur la première case du jeu qu’il 
#venait d’inventer, deux sur la suivante, 
#quatre sur la troisième, 
#et ainsi de suite jusqu’à la 64 e case.
a = 1
for i in range (1,11):
    print(i, "=",a)
    a = a*2










