a = (3,4,5, "a")
print(a)
print(type(a)) #class tuple
b = (2,)
print(type(b))

##### ensemble 
t1 = ["a", "b", "c", "a", 3, 6, 1, 8, 5, 1, 1]
print(set(t1)) #enlève doublons
#set(t1) -->puis print(t1)

ensemble1 = {"fraise","groseille","pomme","poire"}
ensemble2 = {"fraise","mûre","myrtille","groseille"}

print(ensemble1&ensemble2) #mot communs fraise groseille
print(ensemble1 | ensemble2) #ensemble sans doublons
print(ensemble1-ensemble2) #ce qu'il n'y a pas ds liste 2 #pomme poire
print(ensemble2-ensemble1) #ce qu'il n'y a pas ds liste 1 #mure myrtille


for e in sorted(ensemble1, reverse=True):
    print(e)

#trier dans l'ordre

######################"

dico = {}
dico["dog"] = "chien"
dico["cat"] = "chat"
dico["shark"] = "requin"
dico["snake"] = "serpent"
print(dico) #{"dog" : "chien", ...}
print(dico["snake"]) #serpent

del dico["dog"] #supprime dog : chien
print(dico)
print(len(dico))

#Test d’appartenance
if  "chat" in dico : 
    print('oui')
else : 
    print("non")

print(dico.keys()) #cat shark snake
print(dico.values()) #chat requin serpent
print(dico.items()) #(cat chat) ; (shark requin)...


stock = dico.copy() #faire une copie de la liste
del stock["shark"]
print(stock) #cat chat et snake sepent
print(dico) #cat chat; shark requin et snake serpent

a = {'cat': 'chat', 'shark': 'requin', 'snake': 'serpent'}

for clef in a : 
    print(clef) #la clé

for clef in a :
    print(clef, a[clef]) #cat chat

for clef in sorted(a):
    print(clef, a[clef])