import gensim
import gensim.downloader as gensim_api

def similar(clean):
    nlp = gensim_api.load("glove-wiki-gigaword-50")

    word = clean

    labels = []
    for t in nlp.most_similar(word, topn=20):
        labels.append(t[0])
    
    return labels