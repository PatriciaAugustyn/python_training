import re
re.search(r"expr_reg", "string")

a = re.search(r"abc", "abcdef") #non
b = re.search(r"abc", "abccadaef") #non
c = re.search(r"abc*", "ab") #non
d = re.search(r"abc", "abccc") #oui
e = re.search(r"chat*", "chateau") #oui

print(a)
print(b)
print(c)
print(d)
print(e)

ab = re.match("c", "abcdef") #NONE
print(ab)
ac = re.search("c", "abcdef") #OUI
print(ac)

aa = re.match("^a", "abcdef") #match
print(aa)

x = re.match("X", "A\nB\nX", re.MULTILINE) #non
print(x)
i = re.search("^X", "A\nB\nX", re.MULTILINE) #oui
print(i)

######################
texte = "Pierre 123 %*$"
m = re.search("\d+", texte) #search cherche partout

print(m,"\n") 
print(m.group(0)) #123
print(m.start(0)) #7 #index du premier caractère
print(m.end(0)) #10 #index du dernier caractère
print(m.span(0)) #(7, 10) #index de l'intervalle

#avec match
texte = "Pierre 123 %*$"
m = re.match("\d+", texte) #ne marche pas

#print(m,"\n") 
#print(m.group(0)) 
#print(m.start(0)) 
#print(m.end(0))
#print(m.span(0))

try:
    print(m.group(0))
except AttributeError:
    print("Aucune correspondance, désolée") #ici du coup

####findall()

un = re.findall("([0-9]+)", "Bonjour 111 Aurevoir 222")
print(un)
#["111", "222"]


#compile()
pattern = re.compile("d")
a = pattern.search("dog") #match à index 0
print(a)
b = pattern.search("dog", 1) #no match
print(b)
#######avec match()
pattern = re.compile("o")
a = pattern.match("dog") #no match
print(a)
b = pattern.match("dog", 1) #match
print(b)

##########trouver tous les suffixe d'un mot

suff = re.findall(r"^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$", "processing")
print(suff) #["processing"]

autre = re.findall(r"^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$", "processing")
print(autre) #[("process", "ing")]

##########re.finditer
texte = "M. Dupont et Mme. Durand ne sont pas venus hier. Mlle. Perrin était là."
regex= re.compile("(Mm?l?l?e?)\. ([A-Z])")
for m in re.finditer(regex, texte):
    print(m.group(1), "***", m.group(2))
    
#M *** D Mme **** D et Mlle *** P

second = "Le 14 avril 1995 et le 10 mai 1992."
red = re.compile("(\d+) (avril|mai) (\d+)")

for m in re.finditer(red, second):
    print(m.group(1), m.group(2), m.group(3))
#14 avril 1995 et 10 mai 1992


###################SEGMENTER
phrase = "When I'm a Duchess, she said blablbla"
rf = re.split(r' ', phrase)
print(rf)
#['When', "I'm", 'a', 'Duchess,', 'she', 'said', 'blablbla']
rg = re.split(r'[\t\n]+', phrase)
print(rg)
#["When I'm a Duchess, she said blablbla"]

fr = re.split(r'\W+', phrase)
print(fr)
#['When', 'I', 'm', 'a', 'Duchess', 'she', 'said', 'blablbla']


#####################re.sub()
jr = re.sub(r"ab", r"ab", "abcdef")
print(jr)

lm = re.sub(r'(ab)', r'\1', 'abcdef')
print(lm)


fleur = "La petite fleur aime le soleil"
new = re.sub("a", "***", fleur)
print(new)
#L*** petite fleur ***ime le soleil

new1 = re.sub("[aeiou]", "V", fleur)
print(new1)
#LV pVtVtV flVVr VVmV lV sVlVVl

new2 = re.sub("[aeiou]{2}", "V", fleur)
print(new2)
#La petite flVr Vme le solVl



###################FONCTION
def remplace_civilite(m):
    #Permet de remplacer les abréviations de civilités par leur nom complet.
    civilite = str()
    if m.group(1) == "M":
        civilite = "Monsieur"
    elif m.group(1) == "Mme":
        civilite = "Madame"
    elif m.group(1) == "Mlle":
        civilite = "Mademoiselle"
    return civilite+" "+m.group(2)
ex = "M. Dupont et Mme. Durand ne sont pas venus hier. Mlle. Perrin était là. Signé M."
regexx = re.compile("(Mm?l?l?e?)\. ([A-Z])")
for m in re.finditer(regexx,ex):
    print(m.group(1), m.group(2))
nouv_txt = re.sub(regexx, remplace_civilite,ex)
print(nouv_txt)

###
#M D
#Mme D
#Mlle P
#Monsieur Dupont et Madame Durand ne sont pas venus hier. 
#Mademoiselle Perrin était là. Signé M.

#################################
def tokenize(text):
    tokens = clean_text(text) #nettoyer texte : enlever maj
    tokens = tokens.split() #découpe chaque mot à l'espace
    return tokens
    
def clean_text(text: str) -> str: #-> : typing elle prend un str et donne un str après être nettoyé
    #mais pour les dic
    PUNCTUATION = "?!():;,.*"
    APOSTROPHE = "'"
    cleaned = ""
    for char in text:
        if char not in PUNCTUATION:
            cleaned += char
        if char == APOSTROPHE:
            cleaned += " "
        return cleaned.replace("\n", " ").lower()

def main():
    texte = input("Veullez entrer un texte : ")
    words = tokenize(texte)
    print(words)
main()


#2ème partie
#from tokenisation import tokenize
from sys import argv

def main():
    path = input("Quel est le chemin du texte : ")
    text = load_file(path)
    tokens = tokenize(text)
    occ_dict = create_occ_dict(tokens)
    print(occ_dict)

def load_file(path: str) -> str:
    with open(path, "r") as file:
        return file.read()

    
def create_occ_dict(tokens):
    occ_dict={}
    for token in tokens:
        if token in occ_dict:
            occ_dict[token] += 1
        else:
            occ_dict[token] = 1
        return occ_dict

if __name__ == "__main__":
    main()
       
    
    
    
    
    
    
    
    
    
    












