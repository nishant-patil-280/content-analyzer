# # nltk.download('stopwords')
# # nltk.download('wordnet')
# # nltk.download('omw-1.4')
# # spacy.cli.download("en_core_web_lg")
# # ner = en_core_web_lg.load()

import tkinter as tk
from tkinter import ttk
from degree import textNER
from degree import language
from degree import textDegree

root = tk.Tk() 
root.geometry("1000x600")
root.title("Text Analyzer")

Font = ("Fixedsys", 15)

top_frame = tk.Frame(root,width=2000,height=60,bg='#EA5C2B')
top_frame.pack(side="top")

title = tk.Label(top_frame, text="Content Analyzer Using NLP",width=500,height=2,font=30,bg='#F76E11',fg="#F4FCD9")
title.pack()

frame_1 = tk.Frame(root, bg='#FFBC80', width=500, height=600)
frame_1.pack(side="left",fill=tk.BOTH,expand=0)

frame_2 = tk.Frame(root, width=500, height=600)
frame_2.pack(side="right",fill=tk.BOTH,expand=0)

label_1 = tk.Label(frame_1, text="Enter first text to analyze: ",font=Font,bg='#FFBC80',fg="#1B1A17")
label_1.place(x=50, y=20)

entry_1 = tk.Entry(frame_1,font=Font, width = 40, bg="#E8FFC2")
entry_1.place(x=50, y=60,height=40)

label_2 = tk.Label(frame_1, text="Enter second text to analyze: ",font=Font,bg='#FFBC80',fg="#1B1A17")
label_2.place(x=50, y=120)

entry_2 = tk.Entry(frame_1,font=Font, width = 40, bg="#E8FFC2")
entry_2.place(x=50, y=160,height=40)

def clicked():
    txt_1 = entry_1.get()
    txt_2 = entry_2.get()
    entry_1.delete(0, tk.END)
    entry_2.delete(0, tk.END) 

    degree = textDegree(txt_1,txt_2)

    langLabel_1 = tk.Label(frame_2, text="Analysis of text 1: \n" + txt_1,font=Font, justify='left')
    langLabel_1.place(x=50, y=20)

    lang_1 = tk.Label(frame_2,font=5, text = 'Language: ' + str(language(txt_1)), justify='left')
    lang_1.place(x=50, y=60)

    NER_1 = tk.Label(frame_2,font=5, text = 'Entities: ' + str(textNER(txt_1)))
    NER_1.place(x=50, y=100)
    # "Similar bag of Words: " + str(degree[0])       
    # similarTxt_1 = tk.Label(frame_2, text=degree[0],font=Font)
    # similarTxt_1.place(x=100, y=20,width=50)

    langLabel_2 = tk.Label(frame_2, text="Analysis of text 2: \n" + txt_2,font=Font, justify='left')
    langLabel_2.place(x=50, y=160)

    lang_2 = tk.Label(frame_2,font=5, text = 'Language: ' + str(language(txt_2)), justify='left')
    lang_2.place(x=50, y=200)

    NER_2 = tk.Label(frame_2,font=5, text = 'Entities: ' + str(textNER(txt_2)))
    NER_2.place(x=50, y=240)    

    degree = tk.Label(frame_2,font=Font, text = 'Degree of Similarity: ' + str(degree))
    degree.place(x=50, y=300) 

myButton = tk.Button(frame_1,font = Font, padx=50, pady=20, activebackground='#FFBC80', bg='#E8FFC2' , text = 'Analyze', command=clicked)
myButton.place(x=150, y=250)

root.mainloop()
