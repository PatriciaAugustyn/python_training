 
#re.compile() : pour compiler et enregistrer un motif
#re.match() = recherche au début de la chaîne
#re.search() = chercher la première correspondance
#re.finditer() : itérateur qui cherche toutes les correspondances
#re.sub() = pour remplacer
#re.split() = pour découper
#match.group() = appeler les séquences mémorisées

import re

#Pour la semaine prochaine : trouver tous les adverbes dans un texte
#français et anglais
def adv_angl(text):
    adv = re.compile(r'\b(\w+ly|\w+able|\w+ible)\b')
    extract = adv.findall(text)
    return extract

print(adv_angl("The teacher explained clearly the concept to the class. (ironie humh hum)"))

def adv_fr(text):
    adv = re.compile(r'\b(\w+ment)\b')
    extract = adv.findall(text)
    return extract

print(adv_fr("Il marche rapidement"))

#Ecrire une fonction qui supprime tout ce qui ressemble à un suffixe : 
#trouver tout les suffixes d’un  mot
def supp_suffixe(text):
    suffixe = re.sub(r'(ade|age|able|tion|ment|ique|té|al|isme|âtre|eur|euse)', "", text) 
    return suffixe
print(supp_suffixe("Le bandage est blanchâtre."))



     



