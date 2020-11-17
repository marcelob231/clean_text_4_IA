from pymongo import MongoClient
import nltk

conn = MongoClient('mongodb://localhost:27017')
print(conn)
db = conn.tcc
twitter = db.twitter
twitter_clean = db.twitter_clean

list_twitters = twitter.find({})

#nltk.download()
stop_words = nltk.corpus.stopwords.words("portuguese")

def cleaning(text):
    stop_words = nltk.corpus.stopwords.words("portuguese")
    
    stopchars = ['!', '.', ';', ':', ',', '>', '<', '?', '/', '"', '%', '*', '#',
    '=', '+', '(', ')', '|' ]

    startchar = ['@', '.@', '#', '.#', 'http', '.http']


    ltext = text.lower()    #Convert sentence to lowcaps
    ntext = ltext.split()
    _ntext = []
    for word in ntext:
        check = True
        for i in startchar:             # Checks if words starts with 
            if word.startswith(i):      # characters from list startchar
                check = False
        if check:
            check2 = True
            for j in stop_words:         # Checks if word is from list stopwords 
                if word == j:           
                    check2 = False    
            if check2:
                for w in stopchars:             # Removes special characters if it's
                    word = word.replace(w, '')  # in the list stopchars 
                _ntext.append(word)                     # Puts word in new text list 

    jtext = " ".join(_ntext)
        
    return jtext

for idx, i in enumerate(list_twitters):
    tweet_clean = cleaning(i['tweet_text'])
    i['tweet_text'] = tweet_clean
    #print(tweet_clean + " " + str(idx))
    twitter_clean.insert_one(i)
    # if idx >= 1000:
    #     break


