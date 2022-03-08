from threading import local
from pymongo import MongoClient

mongo_url = 'mongodb://mongo:iPAnHlBPYNyPlsoIltgc@containers-us-west-15.railway.app:7323'
mongo_localhost = 'mongodb://localhost'

conn = MongoClient(mongo_url)