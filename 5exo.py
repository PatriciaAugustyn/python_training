
jeu = {}
jeu["1D"] = "Reine blanche"
jeu["1F"] = "Cavalier blanc"
jeu["1g"] = "Cheval blanc"
jeu["8d"] = "Reine noire"
jeu["1e"] = "Roi blanc"
jeu["8e"] = "Roi noir"

print(jeu)
#print(sorted(jeu))
for clef, valeur in jeu.items() :
    print(sorted(clef),valeur)
#Non hypothèse éliminé
#donc non le 2
   
jeu_reverse= {}
jeu_reverse["Reine blanche"] = "1D"
jeu_reverse["Reine noire"] = "8D"
jeu_reverse["Roi blanc"] = "1E"
jeu_reverse["Roi noir"] = "8E"
jeu["Cavalier blanc"] = "1F"
jeu["Cheval blanc"] = "1g"
print(jeu_reverse)

for clef, valeur in jeu.items():
    print(clef, valeur)
for clef, valeur in jeu_reverse.items():
    print(clef, valeur)