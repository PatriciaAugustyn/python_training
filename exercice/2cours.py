#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:53:04 2023

@author: patricia
"""

#for i in range (50) :
	#print (i, ":", type(i))
    
#range(3)

#ch ="Christina"
#print(ch[0], ch[3], ch[5])


car = "e"
voyelle = "aeiouy"

if car in voyelle : 
    print(car, "est une voyelle")
    
salut = "bonjour à tous"
salut = "b" + salut[1:]
print(salut )


print("bonjour", "a", "tous", sep="*")

#nom = input("Entrer votre prénom : ")
#print("Bonjours", nom)

#----- Le type
a = 1
print(type(a))


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 10:08:25 2023

@author: patricia
"""
#Exemple séance 2

c = "1"
d = int(c) #on ne peut pas calculer un str + un int
#il faut le convertir en int
#print(d + 45)
#46

k = float("12.36")
print(k+5)
#17.36

#------------------ Formatage
a = "a"
b = "c"

c = "alpha : {} , b, {}, d"
print(c.format(a,b)) # a,b,c,d

#-------------------index
z = "Le sort"
print(z.index("s")) #place 3
#------------Exo liste

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février ', 'Mars', 'Avril', 'Mai', 'Juin',
'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

t3 = []
for i in range(len(t1)):
    t3.append(t1[i])
    t3.append(t2[i])

print(t3)







   
    
    

