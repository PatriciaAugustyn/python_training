#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 21:06:54 2023

@author: patricia
"""

#1
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février ', 'Mars', 'Avril', 'Mai', 'Juin',
'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

t3 = []
for i in range(len(t2)):
    t3.append(t2[i])
    t3.append(t1[i])
print(t3)

#2. Rechercher le plus grand élément dans une 
#liste de nombres donnée.

a = [13, 79, 1, 30, 456, 16]
plus = a[0]

for i in a :
    if i > plus : 
        plus = i
print("le plus grand élément de la liste : ", plus)
#Output : Le plus grand élément de la liste a la 
#valeur de 456.

#autre façon : 
# liste.sort() #--> trier plus grand plus petit
#print(liste[-1])


#3. A partir d’une liste de nombres donnée, 
#créer deux nouvelles listes : avec les nombres
#divisibles par 4 et les autres.
a = [13, 79, 1, 30, 456, 16]
quatre = []
non_quatre=[]

for i in a : 
    if i % 4 == 0 :
        quatre.append(i)

    else : 
        non_quatre.append(i)
    

print("Divisible par 4 :",quatre)
print("Non divisible par 4 :", non_quatre)
#Output :
#liste des nombres divisibles par 4 : [456, 16]
#liste des nombres non divisible par 4 : [13, 79, 1, 30]













