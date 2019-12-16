from pymongo import MongoClient

from keys import DB


link = 'mongodb://{}:{}@ds018839.mlab.com:18839/user'.format(DB['login'], DB['password'])

db = MongoClient(link)['user']