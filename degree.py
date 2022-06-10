from cProfile import label
import nltk
import re
import langdetect
import spacy
# import pandas as pd
# import numpy as np
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# import spacy.cli
# spacy.cli.download("en_core_web_lg")
# import en_core_web_lg
# ner = en_core_web_lg.load()
# import gensim
import gensim.downloader as gensim_api
# from sklearn import feature_extraction, manifold
# from similar import similar
# from textNER import textNER
# from textPreprocessing import textPreprocessing

# Degree of Similarity
def textDegree(txt_1,txt_2):

    clean_txt_1 = textPreprocessing(txt_1)

    clean_txt_2 = textPreprocessing(txt_2)

    labels_1 = []
    for text in clean_txt_1:
        labels_1.extend(similar(text))

    print('Top 20 similar words each for sentence 1 --->')
    print(labels_1)

    labels_2 = []
    for text in clean_txt_2:
        labels_2.extend(similar(text))

    print('Top 20 similar words each for sentence 2 --->')
    print(labels_2)

    count = 0

    list3 = set(labels_1)&set(labels_2)

    list4 = sorted(list3, key = lambda k : labels_1.index(k))

    # print(len(list4))

    if len(clean_txt_1) + len(clean_txt_2) < 5:
        if len(list4) < 5:
            degree = 0
        elif len(list4) < 15:
            degree = 1
        else: 
            degree = 2

        return degree
    elif len(clean_txt_1) + len(clean_txt_2) < 10:
        if len(list4) < 11:
            degree = 0
        elif len(list4) < 21:
            degree = 1
        else: 
            degree = 2

        return degree
    else:
        if len(list4) < 21:
            degree = 0
        elif len(list4) < 31:
            degree = 1
        else: 
            degree = 2
        
        print(degree)
        return degree


# Text Preprocessing
def language(txt):
    clean_txt_0 = txt
    lang = langdetect.detect(clean_txt_0)
    return lang

def textPreprocessing(txt):

    clean_txt_0 = txt

    print(clean_txt_0, " --- > Language ---> ", langdetect.detect(clean_txt_0))

    person_count = 0

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

# NER model
def textNER(txt):
    ner = spacy.load("en_core_web_lg")
    entities = ner(txt).ents

    clean_txt_0 = txt
    for tag in entities:
        clean_txt_0 = re.sub(tag.text, "_".join(tag.text.split()), 
                            clean_txt_0)
    
    all_entities = []

    persons = []
    norp = []
    org = []
    gpe = []
    loc = []
    date = []
    event = []

    for tag in entities:
        if tag.label_ == "PERSON":
            persons.append(tag.text)
            all_entities.append(persons)
        elif tag.label_ == "NORP":
            norp.append(tag.text)
            all_entities.append(norp)
        elif tag.label_ == "ORG":
            org.append(tag.text)
            all_entities.append(org)
        elif tag.label_ == "GPE":
            gpe.append(tag.text)
            all_entities.append(gpe)
        elif tag.label_ == "LOC":
            loc.append(tag.text)
            all_entities.append(loc)
        elif tag.label_ == "DATE":
            date.append(tag.text)
            all_entities.append(date)
        elif tag.label_ == "EVENT":
            event.append(tag.text)
            all_entities.append(event)
        print(tag.text, " ---> ", tag.label_)
        return (str(tag.text) + ' ' + str(tag.label_))

# Similar function
def similar(clean):
    nlp = gensim_api.load("glove-wiki-gigaword-50")

    word = clean

    labels = []
    for t in nlp.most_similar(word, topn=20):
        labels.append(t[0])
    
    return labels