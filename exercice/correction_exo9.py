#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 13:36:14 2023

@author: patricia
"""
with open("text.txt", "r") as fichierInitial:
    with open("nouveauTexte.txt", "w") as nouveauFichier:
        for ligne in fichierInitial:
            if ligne[0] == "#":
                continue
            else:
                nouveauFichier.write(ligne)

def alterneFichier(source1, source2, sortie):
    fichierAlterne = open("sortie", "w")
    file1 = open(source1, "r")
    file2 = open(source2, "r")
    file1_lecture = file1.readlines()
    file2_l
    
    while 1:
        file1_ligne = file1.readline()
        file2_ligne = file1.readline()
        if file1_ligne = "" and file2_ligne = "":
            break 
        if file1_ligne != ""
#####
