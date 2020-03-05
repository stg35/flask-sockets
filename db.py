from pymongo import MongoClient
import constants

client = MongoClient(constants.db_connect)
db = client['chats']

def insertUser(username, password):
    db['users'].insert_one({'username': username, 'password': password})

