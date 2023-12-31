#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:03:32 2023

@author: patricia
"""

dico = {}
dico["dog"] = "chien"
dico["cat"] = "chat"
dico["shark"] = "requin"
dico["snake"] = "serpent"
print(dico)

print(dico.get("dog")) #chien
print(dico.get("mouse")) #none
print(dico.get("mouse", "Not Found !")) #Not found

#####

dico = {
"pair":list(),
"impair":list(),
}

for nombre in range(0,100):

    if nombre%2 == 0:
        dico["pair"].append(nombre) # ajoute dans dico si c’est divisible par 2
    else:
            dico["impair"].append(nombre) #dans dico “impair”
print(dico["pair"]) # [0,2,4...98]
print(dico["impair"]) # 1,3... 99

##########
from collections import Counter
texte = "La la la li li li lu lu lu po po po mu mu mu"
compteur_caracteres_freq = Counter(texte)
print(compteur_caracteres_freq)
print(compteur_caracteres_freq["a"])
#Counter({' ': 14, 'l': 8, 'u': 6, 'a': 3, 'i': 3, 'p': 3, 'o': 3, 'm': 3, 'L': 1})
#3

for caractere in sorted(compteur_caracteres_freq,
key=lambda x:compteur_caracteres_freq[x], reverse=True):
    print(caractere, compteur_caracteres_freq[caractere])
###########
from collections import Counter
texte = "La la la li li li lu lu lu po po po mu mu mu"
mots = texte.split(" ")
compteur_mot_freq = Counter(mots)
compteur2 = Counter([m.lower() for m in mots])
print(compteur_mot_freq)
print(compteur_mot_freq["la"])
print(compteur2)

#Counter({'li': 3, 'lu': 3, 'po': 3, 'mu': 3, 'la': 2, 'La': 1})
#2
#Counter({'la': 3, 'li': 3, 'lu': 3, 'po': 3, 'mu': 3})
#######

dico={}
dico["yes"]= "oui"
dico["no"]= "non"
dico["maybe"]= "peut-être"
dico["never"]= "jamais"
dico["always"]= "toujours"
print(dico)

del dico["yes"]
print(dico)

for clef in dico:
    print(clef)
for clef, values in dico.items():
    print(clef, values)
for values in dico.values():
    print(values)

print(dico.get("never"))
print(dico.get("jamais",))





from collections import Counter

texte = "La la la li li li lu lu lu po po po mu mu mu"
mots = texte.split(" ") #segmenter en liste

compteur = Counter([i.lower() for i in mots])
print(compteur)

from collections import Counter
a = "La la le Le li ju na"
b = a.split(" ")
print(b)

compteur = Counter([i.lower() for i in b])
print(compteur)



dico={}
dico["yes"]= "oui"
dico["no"]= "non"
dico["maybe"]= "peut-être"
dico["never"]= "jamais"
dico["always"]= "toujours"
print(dico)

for mot in sorted(dico, key=lambda x: dico[x], reverse=True):
    print(mot, dico[mot])

#trier un dico

print(list(dico.keys()))

mots = {}

for i in range(1,3):
    a = input("enter la clé dico:")
    a = int(a)
    b = input("entrer la valeur: ")
    mots[a]=b

print(mots)


for i in sorted(mots, key=lambda x: mots[x], reverse=True):
    print(i, mots[i])

for cle, valeur in mots.items():
    print(cle, valeur)

for cle in mots:
    print(cle)

for valeur in mots.values():
    print(valeur)

print(mots.get(8, "Non !!!!!"))






