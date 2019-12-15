import time

from mongodb import db
from api._error import ErrorAccess, ErrorBusy, ErrorWrong
from api._func import check_params, next_id, get_file


# Создание

def add(this, **x):
	# Проверка параметров

	check_params(x, (
		('video', True, str),
	))

	# Не авторизован

	if this.user['admin'] < 3:
		raise ErrorAccess('add')

	# Уже добавлено

	if db['stories'].find_one({'video': x['video']}, {'_id': True}):
		raise ErrorBusy('video') # ErrorAlready

	#

	query = {
		'id': next_id('stories'),
		'time': this.timestamp,
		'user': this.user['token'],
		'video': x['video'],
	}

	#

	db['stories'].save(query)

	# Убираем лишние поля

	del query['_id']
	del query['time']

	# Прикрепление задания к пользователю

	this.user['stories'].append(query['id'])
	db['users'].save(this.user)

	# Обновление списка историй

	query['video'] = this.server['link'] + 'static/stories/' + query['video']
	this.socketio.emit('story_add', query, namespace='/main')

	# Ответ

	res = {
		'id': query['id'],
	}

	return res

# Получение

def get(this, **x):
	# Проверка параметров

	check_params(x, (
		('id', False, (int, list, tuple), int),
		('my', False, bool),
		('count', False, int),
	))

	# Мои истории

	if 'my' not in x:
		x['my'] = False

	if x['my'] and this.user['admin'] < 3:
		raise ErrorAccess('token')

	# Условия

	count = x['count'] if 'count' in x else None

	db_condition = dict()

	if 'id' in x:
		if type(x['id']) == int:
			db_condition['id'] = x['id']

		else:
			db_condition['id'] = {'$in': x['id']}

	else:
		if x['my']:
			db_condition['id'] = {'$in': this.user['stories']}

	#

	db_filter = {
		'_id': False,
	}

	stories = [i for i in db['stories'].find(db_condition, db_filter).sort('time', -1) if i]

	# Выборка

	ind = 0
	while ind < len(stories):
		# Только чужие

		if not x['my'] and stories[ind]['user'] == this.user['token']:
			del stories[ind]
			continue

		# Онлайн пользователи

		db_filter = {
			'_id': False,
			'online': True,
		}

		user = db['users'].find_one({'token': stories[ind]['user']}, db_filter)

		stories[ind]['online'] = user['online']

		# Удаление полей

		del stories[ind]['user']
		del stories[ind]['time']

		#

		ind += 1

	# Количество

	stories = stories[:count]

	# Видео

	for i in range(len(stories)):
		stories[i]['video'] = this.server['link'] + 'static/stories/' + stories[i]['video']
	
	# Ответ

	res = {
		'stories': stories,
	}

	return res

# Удаление

def delete(this, **x):
	# Проверка параметров

	check_params(x, (
		('id', True, int),
	))

	#

	story = db['stories'].find_one({'id': x['id']})

	# Неправильный ID

	if not story:
		raise ErrorWrong('id')

	# Нет прав

	if this.user['admin'] < 3 or story['user'] != this.user['token']:
		raise ErrorAccess('token')

	#

	db['stories'].delete_one(story)