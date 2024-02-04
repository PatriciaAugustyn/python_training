'''
L'objectif est de créer un programme qui demande à l'utilisateur de saisir 
deux nombres, puis d'afficher la somme de ces deux nombres.
'''
while True : 
    choice = input("Voulez-vous continuer [Y/N] ? ")
    if choice == "N":
        break
    else : 
        first = int(input("Veuillez entrer un premier nombre : "))
        second = int(input("Veuillez entrer un deuxième nombre : "))
        results = first + second
        print(f"L'addition de {first} et de {second} est {results}")