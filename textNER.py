import spacy
import nltk
import re

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
        return (tag.text, " ---> ", tag.label_)

    # return all_entities