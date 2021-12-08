# -*- coding: utf-8 -*-
"""Tokenization_NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1THQXJAfUH6WcQTz4nUjHR6fuKr4Fk1_T
"""

#Split by Whitespace
import re
text = 'I\'m with you for the entire life in U.K.!'
words = re.split(r'\W+', text)
print(words[:100])

#Select Words
words = re.split(r'\W+', text)
print(words[:100])

import string
import re
# split into words by white space
words = text.split()
# prepare regex for char filtering
re_punc = re.compile('[%s]' % re.escape(string.punctuation))
# remove punctuation from each word
stripped = [re_punc.sub('', w) for w in words]
print(stripped[:100])

# string.printable inverse of string.punctuation
re_print = re.compile('[^%s]' % re.escape(string.printable))
result = [re_print.sub('', w) for w in words]
print(result)

# Normalizing Case

# split into words by white space
words = text.split()
# convert to lower case
words = [word.lower() for word in words]
print(words[:100])

_____________________________ Working on Spacy _________________________

# Install by https://spacy.io/usage/facts-figures#benchmarks
# conda install -c conda-forge spacy
# or
# pip install -U spacy

# Alternatively you can create a virtual environment:
# conda create -n spacyenv python=3 spacy=2

import spacy
nlp = spacy.load('en_core_web_sm')

string = '"I\'m with you for the entire life in P.K.!"'
print(string)

doc = nlp(string)
for token in doc:
    print(token.text, end=' | ')

doc2 = nlp(u"We're here to help! Send snail-mail, email fahad@gmail.com or visit us at https://fahadhussaincs.blogspot.com/!")
for t in doc2:
    print(t)

doc3 = nlp(u'A 5km NYC cab ride costs $10.30')
for t in doc3:
    print(t)

doc4 = nlp(u"Let's visit St. Louis in the U.S. next year.")
for t in doc4:
    print(t)

len(doc)

len(doc.vocab)

doc5 = nlp(u'It is better to give than to receive.')
# Retrieve the third token:
doc5[2]

# Retrieve three tokens from the middle:
doc5[2:5]

# Retrieve the last four tokens:
doc5[-4:]

doc6 = nlp(u'My dinner was horrible.')
doc7 = nlp(u'Your dinner was delicious.')

# Try to change "My dinner was horrible" to "My dinner was delicious"
doc6[3] = doc7[3]

doc8 = nlp(u'Apple to build a Hong Kong factory for $6 million')

for token in doc8:
    print(token.text, end=' | ')

print('\n----')

for ent in doc8.ents:
    print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))

len(doc8.ents)

doc9 = nlp(u"Autonomous cars shift insurance liability toward manufacturers.")

for chunk in doc9.noun_chunks:
    print(chunk.text)

doc10 = nlp(u"Red cars do not carry higher insurance rates.")

for chunk in doc10.noun_chunks:
    print(chunk.text)

doc11 = nlp(u"He was a one-eyed, one-horned, flying, purple people-eater.")

for chunk in doc11.noun_chunks:
    print(chunk.text)

from spacy import displacy

doc = nlp(u'Apple is going to build a U.K. factory for $6 million.')
displacy.render(doc, style='dep', jupyter=True, options={'distance': 110})

doc = nlp(u'Over the last quarter Apple sold nearly 20 thousand iPods for a profit of $6 million.')
displacy.render(doc, style='ent', jupyter=True)

doc = nlp(u'This is a sentence.')
displacy.serve(doc, style='dep')

