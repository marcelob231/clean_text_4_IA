from pymongo import MongoClient
conn = MongoClient('mongodb://localhost:27017')
print(conn)
db = conn.tcc
twitter_new = db.twitter_new


replic = db.twitter_new.aggregate([
    {'$group': {
        '_id': {'tweet_text': '$tweet_text'},
        'idsUnicos': {'$addToSet': '$_id'},
        'total': {'$sum': 1}
        }
    },
    {'$match': { 
        'total': {'$gt': 1}
        }
    }
])

for i in replic:
    for idx, j in enumerate(i['idsUnicos']):
        if idx != 0:
            twitter_new.delete_one({'_id': j})



