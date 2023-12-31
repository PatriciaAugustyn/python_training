#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 14:52:32 2023

@author: patricia
"""
########Correction##############
prefixes = "JKLMOPQ"
suffixe = "ack"
for i in prefixes : 
    #print(i) = chaque lettre de prefixes liste : J, K, L...
    print(i+suffixe)
    
#####################################################
jour = ["lundi", "mardi", "mercredi", "jeudi"]
jour[3] = "Juillet"
print(jour)
#ajouter

jour.sort()
print(jour)

jour.reverse()
print(jour)

jour.index("lundi")
print(jour)

jour.remove("lundi")
print(jour)

############################################
liste1=[1,2,3]
liste2=[6,7,8]
liste1.extend(liste2)	 #on insère liste2 à la fin de la liste1
print (liste1)

###########################################

liste=[1,2,3]
liste.append(7) 	
liste.insert(2, "c") #ajoute c à la position c	
print (liste)

###########
del liste[2]
print(liste) #supprimer le 2 avec son index

##################
fable = ["la", "cigale", "et", "la"]
for i in range(len(fable)) : 
    print(i, fable[i])
##résultat 0 La
#1 cigale
#2 et .....

######################
a = list(range(10))
print(a)

for i in sorted(a): 
    print(i)
print(a)
#trier

###################
li = [4, 5, 3, -6, 7, 9]
for i in range(0, len(li)): 
    print(i, li[i])
                                #deux colonnes une avec les indice
                                #et la deuxième les éléments
for i, v in enumerate(li):
    print(i, v)

#0 4
#1 5
#2 3
#3 -6
#4 7
#5 9

#############################################
liste=[1,2,3]
for nb in liste:
    print(nb * nb) #le résultat n’est pas une liste
#Résultat : 1,4,9

#ou bien comme ça 
liste=[1,2,3]
print([nb * nb for nb in liste])
#ici le résultat est une liste [1,4,9]

####################
liste=[1,2,3]
print([nb for nb in liste if nb %2 ==0])

###########
l = [3,6,2,7,0]
x = 7 

for i,v: 
print(position)






