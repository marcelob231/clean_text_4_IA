# encoding: utf-8
import pandas as pd
from pymongo import MongoClient
import nltk
from nltk.stem import RSLPStemmer
from gensim.utils import simple_preprocess

#nltk.download()

conn = MongoClient('mongodb://localhost:27017')
print(conn)
db = conn.tcc
twitter_clean = db.twitter_clean

to_pandas = twitter_clean.find({})  # Get data from MongoDB

df = pd.DataFrame(list(to_pandas))  # Convert data to Pandas DataFrame

del df['_id']       # Delete column _id

                # Tokenize words in sentences and keep in a new column
df['tokenized_text'] = [simple_preprocess(line, deacc=True) for line in df['tweet_text']] 
# print(df['tokenized_text'].head(10))

                # Stemm sentences
for idx, sentence in enumerate(df['tokenized_text']):
    df['tokenized_text'][idx] = Stemming(sentence)

# print(df['tokenized_text'].head(10))

def Stemming(sentence):         # Function to Stemm words in sentences 
    stemmer = RSLPStemmer()     # to their root form
    phrase = []
    for word in sentence:
        phrase.append(stemmer.stem(word.lower()))
    return phrase