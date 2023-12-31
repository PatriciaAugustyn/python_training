#Travail à faire
#Définissez une fonction qui renvoie 
#le nom du n-ième mois de l’année. 
#Exemple, l’exécution de l’instruction :
#print(fonction(4)) doit donner le résultat : 
#Avril.
def mois(nombre):
    moi={1:"janvier", 2:"février", 3:"mars", 4:"avril", 5:"mai", 6:"juin"}
    return moi.get(nombre, "Nope")
print(mois(4))

#Faire une fonction qui affiche la table de 
#multiplication par nombre (nb) en indiquant 
#que le nombre maximum d’affichage doit être 
#10 par défaut
def table_de_multiplication(nb, affichage=10):
    print(f"Table de multiplication pour {nb} jusqu'à {affichage} :")
    for i in range(affichage + 1):
        resultat = nb * i
        print(f"{nb} x {i} = {resultat}")

#table de 5
table_de_multiplication(5)

#Travail à faire
#Définissez une fonction changeCar(ch,ca1,ca2,
#debut,fin) qui remplace tous les caractères 
#ca1 par des caractères ca2 dans la chaine de 
#car. ch, à partir de l’indice debut et jusqu’à 
#l’indice fin, ces deux derniers arguments pouvant
#être omis (et dans ce cas la chaine est traitée 
#d’une extrémité à l’autre) :
#phrase = 'Ceci est une toute petite phrase.'
#print(changeCar(phrase, ' ', '*'))
#Ceci*est*une*toute*petite*phrase.
#print(changeCar(phrase, ' ', '*', 8, 12))
#Ceci est*une*toute petite phrase.
#print(changeCar(phrase, ' ', '*', 12))
#Ceci est une*toute*petite*phrase.
#print(changeCar(phrase, ' ', '*', fin = 12))
#Ceci*est*une*toute petite phrase.

########################################### pas fait

#Définir une fonction qui renvoie l’index de 
#l’élément ayant la valeur la plus élevée dans 
#la liste transmise en argument :
#serie = [5, 8, 2, 1, 9, 3, 6, 7]
#print(fonction(serie))
#4

def fonction(liste):
    maxi = max(liste)
    indexer = liste.index(maxi)
    print(f"Le plus grand nombre dans la liste {liste} est {maxi} donc il se trouve à l'index {indexer} : ")
    return indexer

serie = [5, 8, 2, 1, 9, 3, 6, 7]

print(fonction(serie))
  
#Définir une fonction qui renvoie l’élément 
#ayant la plus grande valeur dans la liste 
#transmise. Les deux arguments debut et fin 
#indiqueront les indices entre lesquels doit 
#s’exercer la recherche, et chacun d’eux pourra 
#être omis.

#Exemples de la fonctionnalité attendue :
#serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
#print(fonction(serie))
#9
#print(fonction(serie, 2, 5))
#7
#print(fonction(serie, 2))
#8
#print(fonction(serie, fin =3, debut =1))
#6



#Faire une fonction qui construit un 
#dictionnaire inversé pour lequel les valeurs 
#seront les clés et réciproquement.
def inverse(dico):
    dico_inverse = {}
    for cle, valeur in dico.items():
        dico_inverse[valeur]= cle
    return dico_inverse

serie = {"dog":"chien", "mouse":"souris"}
print(inverse(serie))


#option raccourci
def inverse(dico):
    dico_inver = {cle:valeur for valeur, cle in dico.items()}
    return dico_inver

serie2 = {"dog":"chien", "mouse":"souris"}
print(inverse(serie2))

#Ecrire un script qui crée et consulte le 
#dictionnaire avec les informations sur les 
#noms, l’âge et la taille des gens.

#Astuces :
#Le script devra comporter deux fonctions : 
#le remplissage du dictionnaire, et sa 
#consultation.
#Remplir le dico en utilisant une 
#boucle pour accepter les données entrées par 
#l’utilisateur.
#Dans le dictionnaire, le nom 
#servira de clé d’accès, et 
#les valeurs seront constituées de tuples 
#(âge, taille)
#L’âge (une année) est une donnée de type entier,
#et la taille est une donnée de type réel.
#Consulter le dico en utilisant aussi une boucle,
#dans laquelle l’utilisateur pourra fournir un 
#nom quelconque pour obtenir en retour le 
#couple « âge, taille » correspondant.
#Le résultat de la requête devra avoir une 
#forme suivante : 
#Nom : Iris Taravella - âge : 18 ans - 
#taille : 1.55 m ».
def remplirDico(dico): 
    for i in range(1):
        nom= input("Entrer un nom : ")
        age = int(input("Entrer l'age : "))
        taille = float(input("Entrer taille : ")) 
        dico[nom]= (age , taille) 
    return dico

def consulterDico(dico):
    recherche = input("Quel nom : ")
    age, taille = dico[recherche]
    print(f"Nom : {recherche} - âge : {age} ans - taille : {taille} m.")

#nom = {}
#print(remplirDico(nom))
#print(consulterDico(nom))

#correction : 
def changeCar(ch, ca1, ca2, debut=0, fin=10):
    if fin > len(ch) : 
        fin = len(ch)
    start = ch[0:debut]
    end = ch[fin:]
    ch = start + ch[debut:fin].replace(ca1, ca2) + end
    return ch

print(changeCar("suis", "i", "o")) 


def tri_valeur(serie, debut=0, fin=None): #none parce que le dernier élement n'est pas forcément à la fin
    if fin is None : 
        fin = max(serie)
    
    biggest = 0
    
    for i in serie : 
        if debut <= i <= fin and i>biggest : 
            biggest = i
    return(biggest)

a=[0,6,9,56, 7, 4, 1, 79]
print(tri_valeur(a, 1,5))
