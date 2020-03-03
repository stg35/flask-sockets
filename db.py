from pymongo import MongoClient
import constants

client = MongoClient(constants.db_connect)
db = client['sample_analytics']
collection = db['customers']

print(collection.count_documents({"_id":"1"}))