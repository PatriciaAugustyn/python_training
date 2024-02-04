'''
Nous allons créer un programme qui vérifie si un nombre est pair ou impair. 
'''

while True : 
    choice = input("Voulez-vous continuer [Y/N] ? ")
    if choice == "N":
        break
    else : 
        number = int(input("Veuillez entrer un nombre : "))
        if number % 2 == 0:
            print(f"Le nombre {number} est un nombre pair")
        else :
            print(f"Le nombre {number} est impair")