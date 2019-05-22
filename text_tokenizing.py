# -*- coding: utf-8 -*-
"""
Created on Wed May 15 01:50:32 2019

@author: SPI
"""

import nltk
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
text="""flying making  you i To provide a proper answer to this question, however, I did a little research, and found something named Worst Sort. The notion of worst sort is similar to that of the bogobogosort: start with a terribly algorithm, then use recursion to make it arbitrarily worse. Worst sort, however, is more of a generalized meta-algorithm though, so it doesn’t specify all the parameters to be used. In particular, it specifies use of a function to determine the recursion depth, but doesn’t specify the exact function to be used. One common suggestion is apparently the Ackerman function (known for extremely fast growth itself)."""
text=text.lower()
sentence_tokenize=sent_tokenize(text)
w_tokenize=word_tokenize(text)
print(sentence_tokenize)
print("\n")
print(w_tokenize)
#finding freq of each word
from nltk.probability import FreqDist
fdis=FreqDist(w_tokenize)
print(fdis)
a=fdis.most_common(2)
print(a)
#plotting each word and its frequency
import matplotlib.pyplot as plt
fdis.plot(30,cumulative=True)
plt.show()
#listing all stopwords
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
print(stop_words)
#removing stopwords
refined_sent=[]
for w in w_tokenize:
    if w not in stop_words:
            refined_sent.append(w)
print(refined_sent)
#Converting ino stem words
from nltk.stem import PorterStemmer
ps=PorterStemmer()
stemmed_words=[]
for w in refined_sent:
    stemmed_words.append(ps.stem(w))
print("\n")
print(stemmed_words)  
#converting into lemmatized words
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('wordnet')
lw=WordNetLemmatizer()
lemmatized_words=[]
for w in refined_sent:
    lemmatized_words.append(lw.lemmatize(w,"v"))
print(lemmatized_words)