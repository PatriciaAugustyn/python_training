#Ok je veux une fonction qui prend en argument une chaine de caractere et qui 
#affiche le plus grand et le plus petit nombre de la chaine
#par exemple : high_and_low("5 2 9 3 4") affiche "2 est le plus petit et 9 est 
#le plus grand"

def high_and_low(chaine):
    chaine = chaine.split()
    maxi = max(chaine)
    mini = min(chaine)
    print(f"La chaine {chaine} a comme plus grand nombre {maxi} et pour plus petit nombre {mini}.")
          

print(high_and_low("15 7 96 1"))  

dico = {}
while True : 
    choix = input("Voulez-vous remplir le dico (O/N): ")
    if choix == "N":
        break
    else : 
        nom = input("Entrer le nom : ")
        age = int(input("Entrer l'âge : "))
    dico[nom]=age

print(dico)