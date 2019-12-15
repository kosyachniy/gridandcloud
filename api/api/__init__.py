import time


from mongodb import db
import api.tasks as tasks
import api.account as account
import api._error as Error



class API():
	def __init__(self, server, socketio, token=None):
		self.timestamp = time.time()
		self.server = server
		self.socketio = socketio
		self.token = token

		# Определение пользователя

		self.user = {
			'id': 0,
			'admin': 2,
		}

		if token:
			db_filter = {'id': True, '_id': False}
			user_id = db['tokens'].find_one({'token': token}, db_filter)
			if user_id and user_id['id']:
				self.user = db['users'].find_one({'id': user_id['id']})

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