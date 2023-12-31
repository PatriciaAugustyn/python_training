#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:33:51 2023

@author: patricia
"""

jeu = {}
lettre = ["a", "b", "c", "d", "e", "f", "g", "h"]
for i in range(1,9):
    for b in lettre :
        jeu[(i, b)]=""

print(jeu)

for j in range(1,2):
    n = input("valeur numérique :")
    n = int(n)
    o = input("valeur alphabétique:")
    echec = input("la pièce d'échec: ")
    jeu[(n,o)]= echec

print(jeu)

#2
