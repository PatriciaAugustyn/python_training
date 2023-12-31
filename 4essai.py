#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 18:37:23 2023

@author: patricia
"""
#tuples
tuples = ("a","c","d", 1, 2)
b=(1,)
print(type(b))

#ensemble

ensemble1 = {"a", "b",}
ensemble2={"a","c", "d"}
print(ensemble1)
print(type(ensemble1))
print(ensemble1 | ensemble2)


#dico
mot = {"mouse": "souris", "shark": "requin", "snake": "serpent"}
print(type(mot))
print(set(mot))
print(mot.keys())
print(mot.values())
print(mot.items())

del mot ["mouse"]
print(mot)
  
for clef in mot : 
    print(clef)
    
for values in mot.values() :
    print(values)

for clef, valeur in mot.items():
    print(clef, valeur)


