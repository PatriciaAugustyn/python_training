#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:57:57 2023

@author: patricia
"""

def remplir_dico(dico):
    while True:
        choix = input("Voulez-vous remplir le dico (O/N) : ")
        if choix.upper() == "N":
            break
        else:
            nom = input("Veuillez mettre un nom : ")
            age = int(input("Veuillez mettre son âge : "))
            taille = float(input("Veuillez mettre sa taille en m : "))
            dico[nom] = {'age': age, 'taille': taille}

def consulte_dico(dico):
    recherche = input("Quel nom cherchez-vous : ")
    if recherche in dico:
        personne = dico[recherche]
        print(f"Nom : {recherche} - Âge : {personne['age']} ans - Taille : {personne['taille']} m.")
    else:
        print(f"La personne avec le nom {recherche} n'est pas dans le dictionnaire.")

# Fonction pour enregistrer le dictionnaire dans un fichier texte
def enregistrement(fichier, dico):
    with open(fichier, "w") as fichier_texte:
        for nom, infos in dico.items():
            age = infos['age']
            taille = infos['taille']
            ligne = f"{nom},{age},{taille}\n"
            fichier_texte.write(ligne)
    print(f"Le dictionnaire a été enregistré dans le fichier {fichier}.")


# Exemple d'utilisation
abc = {}
remplir_dico(abc)
consulte_dico(abc)

# Enregistrement du dictionnaire dans un fichier texte
enregistrement('info_personnes.txt', abc)


