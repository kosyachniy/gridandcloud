import os
import re
import time
import base64

import requests

from mongodb import db
from api._error import ErrorSpecified, ErrorInvalid, ErrorType

from sets import CLIENT


# Проверить наличие файла по имени

def get_file(url, name):
	url = '/static/' + url + '/'

	return name in os.listdir('app' + url)

# Проверка параметров

def check_params(x, filters): # ! Удалять другие поля (которых нет в списке)
	for i in filters:
		if i[0] in x:
			# Неправильный тип данных
			if type(i[2]) not in (list, tuple):
				el_type = (i[2],)
			else:
				el_type = i[2]

			cond_type = type(x[i[0]]) not in el_type
			cond_iter = type(x[i[0]]) in (tuple, list)

			try:
				cond_iter_el = cond_iter and any(type(j) != i[3] for j in x[i[0]])
			except:
				raise ErrorType(i[0])

			if cond_type or cond_iter_el:
				raise ErrorType(i[0])
				# return dumps({'error': 4, 'message': ERROR[3].format(i[0], str(i[2]))})

			cond_null = type(i[-1]) == bool and i[-1] and cond_iter and not len(x[i[0]])
			
			if cond_null:
				raise ErrorInvalid(i[0])

		# Не все поля заполнены
		elif i[1]:
			raise ErrorSpecified(i[0])
			# return dumps({'error': 3, 'message': ERROR[2].format(i[0])})

# Следующий ID БД

def next_id(name):
	try:
		db_filter = {'id': True, '_id': False}
		id = db[name].find({}, db_filter).sort('id', -1)[0]['id'] + 1
	except:
		id = 1
	
	return id