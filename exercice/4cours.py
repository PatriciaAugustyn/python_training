a = (3,4,5)
print(type(a))
#tuples
#<class 'tuple'>

b = (3,)
print(type(b))
#tuples avec un seul élement --> il faut ,
#<class 'tuple'>

##############################
#Les ensembles : 
a = ["a", "b", "a", 9, 8, 0, 9]
b = set(a)
print(b)
#enlève doublons mais dans le désordre
#################
ensemble1 = {"fraise","groseille","pomme","poire"}
ensemble2 = {"fraise","mûre","myrtille","groseille"}
print(ensemble1&ensemble2) 
#mot commun

print(ensemble1|ensemble2)
#Union tout mais sans doublon

print(ensemble1-ensemble2)
#pomme poire, mot présent dans l'ensemble 1 mais pas ensemble 2

print(ensemble2-ensemble1)
#mure myrtille

print(len(ensemble1))
# 4

for element in ensemble1:
    print(element)
#groseille pomme fraise poire

for e in sorted(ensemble1, reverse=True):
    print(e)

for e in sorted(ensemble1, reverse=True):
	print(e)

#########
ch = "la maison de ma maman"
print(set(ch))
#a e s 

liste=["poire","poire","poire","pomme","pomme","cidre","abricot"]
print(set(liste))

#################
dico = {}
dico["com"] = "ordi"
dico["mouse"] = "souris"
print(dico)
print(dico['mouse'])
print(type(dico))
######################
invent = {'com': 'ordi', 'mouse': 'souris'}
print(invent)

del invent ["com"]
print(len(invent))
# 1 car il y a plus que mouse : souris
print(invent)

#############
print(invent.keys()) #mouse
print(invent.values()) #souris

for cle, valeur in invent.items():
    print ("la clé {} contient la valeur {}. ".format(cle,valeur))
    #la clé mouse contient la valeur souris. 


stock = invent
print(stock)
magasin = stock.copy()
magasin['mouse'] = 561
print(magasin) #{'mouse': 561}
print(stock) #{'mouse': 'souris'}
print(invent) #{'mouse': 'souris'}

for clef in invent :
    print(clef)
#parcourir les clef donc seulement mouse ici
#ici par défaut il parcour clé

for clef, valeur in invent.items():
    print(clef, valeur)
#ici mouse souris
#imprime les 2

for cle in dico: #un dico se parcourt par ses clés
    print(cle,dico[cle])
#ici ordi dans dico
#dans invent mouse souris
#dico ici


for valeur in dico.values():
    print(valeur)
#ici souris ds dico et invent
#valeur

########################

#Parcourir un dictionnaire trié sur les clés
for cle in sorted(dico):
    print(cle,dico[cle])
#com ordi
#mouse souris



