#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 16:17:16 2023

@author: patricia
"""

#obFichier = open("Monfichier.txt", "a")
#obFichier.write("Bonjour, fichier !")
#obFichier.write("Quel beau temps, aujourd’hui !")
#ofi = open("Monfichier.txt", "a")
#t = ofi.read()
#print(t)
#ofi.close()
f = open("MonFichier.txt", "w") #write
f.write("Ceci est la ligne un\nVoici la ligne deux\n")
f.write("Ceci est la ligne trois\nVoici la ligne quatre\n")
f.close()

f = open("MonFichier.txt", "r") #read
t = f.readline()
print(t)
#Ceci est la ligne un
print(f.readline())
#Voici la ligne deux

t = f.readlines()
print(t)
#['Ceci est la ligne trois\n', 'Voici la ligne quatre\n']
f.close

####################on prend ce qu'on a écrit dans le Monfichier --> TonFichier
def copieFichier(source, destination): 
    fs = open(source, "r")
    fd = open(destination, "w")
    while 1:
        txt = fs.read(10)
        if txt == "": #si il arrive à la fin alors on sort
            break
        fd.write(txt)
    fs.close()
    fd.close()
    return
copieFichier("MonFichier.txt", "TonFichier.txt")

#############"
filename = input("Veuiller entrer un nom de fichier : ")
try : 
    f = open(filename, "r")
except:
    print("Le fichier", filename, "est introuvable")

##################### pour ouvrir fichier on peut
with open("MonFichier.txt", "r") as mon_fichier:
    texte=mon_fichier.read()











    




