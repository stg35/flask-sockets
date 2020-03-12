from pymongo import MongoClient
import constants

client = MongoClient(constants.db_connect)
db = client['chats']


def insertUser(username, password):
    db['users'].insert_one({'username': username, 'password': password})


def findUP(username, password):
    if db['users'].find({'username': username, 'password': password}).count() > 0:
        return True
    else:
        return False

def addMessage(message, user):
    db['messages'].insert_one({'user': user, 'message': message})