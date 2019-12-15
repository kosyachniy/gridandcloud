from pymongo import MongoClient

from keys import DB


# db = MongoClient()['junction']

# db = MongoClient(
# 	username=DB['login'],
# 	password=DB['password'],
# 	authSource='admin',
# 	authMechanism='SCRAM-SHA-1'
# )['moscow']

link = 'mongodb://{}:{}@ds018839.mlab.com:18839/user'.format(DB['login'], DB['password'])

db = MongoClient(link)['user']