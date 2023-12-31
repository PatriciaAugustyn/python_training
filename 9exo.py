#Recopier un fichier texte dans un autre fichier, 
#en omettant toutes les lignes qui commencent par 
#un caractère #
#• Comparer les contenus de deux fichiers et 
#signaler la première différence rencontrée.
#• A partir de deux fichiers préexistants, 
#construire le troisième qui contienne 
#alternativement un élément de 1er, 
#un élément du 2ème, un élément de 1er, 
#un élément du 2ème... et ainsi de suite 
#jusqu’a atteindre la fin de l’un des deux 
#fichiers originaux.
#Compléter le troisième fichier avec les éléments
#restant sur l’autre.
#Reprendre l’ex. où il fallait écrire un script 
#qui crée et consulte le dictionnaire avec les 
#informations sur les noms, l’âge et la taille 
#des gens. Complétez cet ex. en lui ajoutant 
#deux fonctions : l’une pour enregistrer le 
#dictionnaire résultant dans un fichier texte,
# et l’autre pour reconstituer ce dictionnaire 
#à partir du fichier correspondant.

#création du fichier
a = open("entree.txt", "w")
a.write("# Ceci est un fichier d'exemple\nBonjour, ceci est une ligne de texte.\nCeci est une autre ligne de texte.\n")
a.write("# Les lignes suivantes sont commentées\n#Cette ligne ne sera pas copiée.\nEncore une ligne de texte.")
a.close()

#copier fichier dans un autre sans les ligne commençant #

def cp_sans_commentaire(fichier1, fichier2):
    entree = open(fichier1, "r")
    sortie = open(fichier2, "w")
    for ligne in entree:
        if ligne[0] != "#":
            sortie.write(ligne)
print(cp_sans_commentaire("entree.txt", "sortie.txt"))

#Reprendre l’ex. où il fallait écrire un script 
#qui crée et consulte le dictionnaire avec les 
#informations sur les noms, l’âge et la taille 
#des gens. Complétez cet ex. en lui ajoutant 
#deux fonctions : l’une pour enregistrer le 
#dictionnaire résultant dans un fichier texte,
# et l’autre pour reconstituer ce dictionnaire 
#à partir du fichier correspondant.

def remplir_dico(dico):
    while True:
        choix = input("Voullez-vous remplir le dico (O/N) :")
        if choix == "N":
            break
        else :
            nom = input("Veuillez mettre un nom : ")
            age = int(input("Veuillez mettre son âge : "))
            taille = float(input("Veuiller mettre sa taille en .m : "))
        dico[nom]= age, taille
def consulte_dico(dico):
    recherche = input("Quel nom cherchez-vous : ")
    age, taille = dico[recherche]
    if recherche in dico:
        print(f"Nom : {recherche} - Âge : {age} ans - Taille : {taille} m.")
    else:
       print(f"La personne avec le nom {recherche} n'est pas dans le dictionnaire.")

#l’une pour enregistrer le dictionnaire 
#résultant dans un fichier texte,
def enregistrement(fichier, dico):
    a = open(fichier, "w")
        for nom, infos in dico.items():
            age = infos['age']
            taille = infos['taille']
            ligne = f"{nom},{age},{taille}\n"
            fichier.write(ligne)
    print(f"Le dictionnaire a été enregistré dans le fichier {fichier}.")
    
# et l’autre pour reconstituer ce dictionnaire 
#à partir du fichier correspondant.

abc={}
print(remplir_dico(abc))
print(consulte_dico(abc))
# Supposons que 'informations_personnes.txt' est le nom de votre fichier
print(enregistrement('info_personnes.txt', abc))



#• Créer et de relire un fichier texte. 
#Le programme demandera d’abord à l’utilisateur 
#d’entrer le nom du fichier. Ensuite il lui 
#proposera le choix, soit d’enregistrer de 
#nouvelles lignes de texte, soit d’afficher le 
#contenu du fichier.
#L’utilisateur devra pouvoir entrer ses 
#lignes de texte successives en utilisant 
#simplement la touche <Enter> pour les séparer 
#les unes des autres.
#Pour terminer les entrées, il lui suffira 
#d’entrer une ligne vide (utiliser la touche 
#<Enter> seule). L’affichage du contenu devra 
#montrer les lignes du fichier séparées les 
#unes des autres de la manière la plus naturelle
#(les codes de fin de ligne ne doivent pas 
#apparaître).

