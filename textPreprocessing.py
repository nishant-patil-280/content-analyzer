import spacy
import nltk
import re
import langdetect

def language(txt):
    clean_txt_0 = txt
    lang = langdetect.detect(clean_txt_0)
    return lang

def textPreprocessing(txt):

    clean_txt_0 = txt

    clean_txt_1 = re.sub(r'[^\w\s]', '', str(clean_txt_0).lower().strip())
    clean_txt_2 = clean_txt_1.split()

    lst_stopwords = nltk.corpus.stopwords.words("english")
    clean_txt_3 = [word for word in clean_txt_2 if word not in lst_stopwords]

    lem = nltk.stem.wordnet.WordNetLemmatizer()
    clean_txt_4 = [lem.lemmatize(word) for word in clean_txt_3]

    words = len(clean_txt_4)
    char = 0
    for word in clean_txt_4: 
        for w in word: 
            char += 1

    print(clean_txt_4, "\nWord Count ---> ", words, "\nCharacter Count ---> ", char)

    return clean_txt_4

