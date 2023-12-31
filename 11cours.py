import nltk

#afficher stopwords
from nltk.corpus import stopwords
print(set(stopwords.words('english')))
print(stopwords.words("english"))

french_stopwords = set(stopwords.words("french"))
print(french_stopwords)

#pour connaitre 
stopwords.fileids()

#éliminer les stopwords du texte
from nltk.tokenize import word_tokenize
text = "In this tutorial hello I\'m learning NLTK. It is an interesting platform."
stop_words = set(stopwords.words("english"))
words = word_tokenize(text) #forme une liste
#si on fait print(words)

new_sentence = []

for word in words :
    if word not in stop_words:
        new_sentence.append(word)
print(new_sentence)


##### en français
french_stopwords = set(stopwords.words("french"))
tokens = ["elle", "moi", "est", "sortir"]
tokens = [token for token in tokens if token.lower() not in french_stopwords]
#parcours liste et voit si les mots de cette liste sont dans notre phrase
print(tokens) #sortir

##############concordancier
file = open("80jours.txt", "r")
read_file = file.read()
text = nltk.Text(nltk.word_tokenize(read_file))

match = text.concordance("société")

###########gutenberg
gutenberg_files = nltk.corpus.gutenberg.fileids()
print(gutenberg_files)
#projet gutenberg

bryant_words = nltk.corpus.gutenberg.words("bryant-stories.txt")
print(len(bryant_words)) #longueur du txt

#######parcourir les fichier des différents textes et voir la moyenne
nltk.corpus.gutenberg.fileids()
from nltk.corpus import gutenberg
gutenberg.fileids()
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    print(int(num_chars/num_words), int(num_words/num_sents), fileid)
#longueur moyenne de chaque test
from nltk.book import*
text1
text1.concordance("monstrous")
text1.similar("monstrous")
#text2.common_
len(text2)
sorted(set(text3))
###########













