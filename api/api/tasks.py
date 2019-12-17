import time

from mongodb import db
from api._error import ErrorAccess
from sets import CLIENT


# Получение

def get(this, **x):
	# Нет прав

	if this.user['admin'] < 3:
		raise ErrorAccess('get')

	# Получение списка

	db_filter = {
		'_id': False,
		'user': False,
	}

	tasks = []

	for task in db['tasks'].find({'user': this.user['id']}, db_filter).sort('time', -1):
		task['image'] = '{}load/{}'.format(CLIENT['link'], task['image'])
		tasks.append(task)

	# Ответ

	res = {
		'tasks': tasks,
	}

	return res