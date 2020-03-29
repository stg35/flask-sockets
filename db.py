from pymongo import MongoClient
import constants

client = MongoClient(constants.db_connect)
db = client['chats']

def insertUser(username, password):
    db['users'].insert_one({'username': username, 'password': password})


def findUser(username):
    if db['users'].find({'username': username}).count() > 0:
        return True
    else:
        return False

def findPassword(username, password):
    if db['users'].find({'username': username, 'password': password}).count() > 0:
        return True
    else:
        return False


def addMessage(message, user, timestamp, id):
    db['messages'].insert_one({'_id': id, 'user': user, 'message': message, 'timestamp': timestamp})

def lastMessages():
    k = 1
    messages = []
    for message in db['messages'].find().sort('_id', -1):
        if k > 10: break
        else: k+=1
        messages.append(message)
    return messages

def getIDLastMessage():
    if db['messages'].count() > 0:
        return db['messages'].find().sort('_id', -1).limit(1)[0]['_id']
    else:
        return 0