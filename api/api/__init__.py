import time


from mongodb import db
import api.tasks as tasks
import api._error as Error



class API():
	def __init__(self, server, socketio, token=None):
		self.timestamp = time.time()
		self.server = server
		self.socketio = socketio
		# self.token = token

		# # Определение пользователя

		# self.user = {
		# 	'token': None,
		# 	'admin': 2,
		# }

		# if token:
		# 	self.user = db['users'].find_one({'token': token})

		# 	if not self.user:
		# 		self.user = {
		# 			'token': token,
		# 			'stories': [],
		# 			'admin': 3,
		# 			'online': True,
		# 			'last': self.timestamp,
		# 		}

		# 		db['users'].insert_one(self.user)


	def method(self, name, params={}):
		# Убираем лишние отступы

		for i in params:
			if type(params[i]) == str:
				params[i] = params[i].strip()

		# Метод API

		try:
			module, method = name.split('.')
			func = getattr(globals()[module], method)
		except:
			raise Error.ErrorWrong('method')
		
		# Запрос

		return func(self, **params)