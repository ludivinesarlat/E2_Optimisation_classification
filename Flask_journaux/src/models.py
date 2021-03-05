import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import FrenchStemmer

def trouve_journal(x):
    if x==1:
        val= 'Le monde'
    elif x==2 :
        val = 'Libération'
    elif x==3:
        val = 'Le Parisien'
    elif x == 4 :
        val = "L'EXPRESS"
    elif x == 5:
        val = "Closer"
    
    return val

def nettoyage(text):
    stop_words = stopwords.words('french')
    stop_words.extend(["c'est","j'ai","a","plus","contre","après", "d'un","d'une","entre","ans","deux","veut","comme", "va","trois","sous","faut","n'est","cinq","leurs","doit","qu'il","peut","n'a","mis","six","cette","j'ai","-","2","5","l'","s'est","dit","dont","3","8"])
    stemmer = FrenchStemmer()
    text = str(text).lower() # mettre les mots en minuscule
    text = re.sub(r"[.,\!\?\%\(\)\/\"]", "", text)  # Retrait les caractères spéciaux :
    text = re.sub(r"\&\S*\s", "", text)
    text = re.sub(r"\d", "", text) 
    text = re.sub(r"\-", "", text) 
    text = re.sub(r"\:", "", text)
    text = re.sub(r"\»", "", text) 
    text = re.sub(r"\«", "", text)
    text = re.sub(r"\’", " ", text)
    text = text.split()
    les_mots = ""
    for mot in text:
        a_ajouter = stemmer.stem(mot)
        if a_ajouter not in stop_words:
            les_mots = les_mots + " "+ a_ajouter
    return les_mots