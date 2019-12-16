import string
import random
import hashlib
import time
import re

from mongodb import db
from api._error import ErrorBusy, ErrorInvalid, ErrorWrong, ErrorAccess
from api._func import check_params, next_id


# Генерация токена

ALL_SYMBOLS = string.digits + string.ascii_letters
generate = lambda length=32: ''.join(random.choice(ALL_SYMBOLS) for _ in range(length))

# Проверить логин

def check_login(cont, user):
	# Логин уже зарегистрирован

	users = db['users'].find_one({'login': cont}, {'_id': True, 'id': True})
	if users and users['id'] != user['id']:
		raise ErrorBusy('login')

	# Недопустимый логин

	cond_length = not 3 <= len(cont) <= 20
	cond_symbols = len(re.findall('[^a-z0-9_]', cont))
	cond_letters = not len(re.findall('[a-z]', cont))

	if cond_length or cond_symbols or cond_letters:
		raise ErrorInvalid('login')

	# Системно зарезервировано

	RESERVED = (
		'admin', 'administrator', 'test', 'tester', 'author', 'bot', 'robot', 
		'root'
	)

	cond_id = cont[:2] == 'id'
	cond_reserv = cont in RESERVED

	if cond_id or cond_reserv:
		raise ErrorInvalid('login')

# Пароль

def check_password(cont):
	# Недопустимый пароль

	cond_length = not 6 <= len(cont) <= 40
	pass_rule = '[^a-zA-z0-9!@#$%^&*()\-+=;:,./?\|`~\[\]\{\}]'
	cond_symbols = len(re.findall(pass_rule, cont))
	cond_letters = not len(re.findall('[a-zA-Z]', cont))
	cond_digits = not len(re.findall('[0-9]', cont))

	if cond_length or cond_symbols or cond_letters or cond_digits:
		raise ErrorInvalid('password')

def process_password(cont):
	# check_password(cont)

	return hashlib.md5(bytes(cont, 'utf-8')).hexdigest()

# Регистрация аккаунта

def registrate(timestamp, login, password):
	# ID

	user_id = next_id('users')

	# Логин

	login = login.lower()
	# check_login(login, user)

	# Пароль

	password = process_password(password)

	#

	db['users'].insert({
		'id': user_id,
		'login': login,
		'password': password,
		'time': timestamp,
		'admin': 3,
	})

	return user_id

#


# # Регистрация

# def reg(this, **x):
# 	# Проверка параметров

# 	check_params(x, (
# 		('login', True, str),
# 		('password', True, str),
# 	))

# 	user_id = registrate(
# 		this.timestamp,
# 		login=x['login'],
# 		password=x['password'],
# 	)

# 	#

# 	token = generate()

# 	req = {
# 		'token': token,
# 		'id': user_id,
# 		'time': this.timestamp,
# 	}
# 	db['tokens'].insert(req)

# 	res = {
# 		'id': user_id,
# 		'token': token,
# 	}

# 	return res

# Авторизация

def auth(this, **x):
	# Проверка параметров

	check_params(x, (
		('login', True, str),
		('password', True, str),
	))

	# Пароль

	db_condition = {
		'login': x['login'].lower(),
	}

	db_filter = {
		'_id': False,
		'id': True,
		'admin': True,
		'password': True,
	}

	res = db['users'].find_one(db_condition, db_filter)

	if not res:
		# Регистрация

		user_id = registrate(
			this.timestamp,
			login=x['login'],
			password=x['password'],
		)
	
	else:
		# Неправильный пароль

		password = hashlib.md5(bytes(x['password'], 'utf-8')).hexdigest()

		if res['password'] != password:
			raise ErrorWrong('password')

		user_id = res['id']
	
	# Токен

	token = generate()

	req = {
		'token': token,
		'id': user_id,
		'time': this.timestamp,
	}

	db['tokens'].insert(req)

	# Ответ

	res = {
		'id': user_id,
		'token': token,
		'admin': 3,
	}

	return res

# Закрытие сессии

def exit(this, **x):
	# Не авторизован

	if not this.token:
		raise ErrorAccess('token')

	#

	res = db['tokens'].find_one({'token': this.token}, {'_id': True})

	# Неправильный токен

	if not res:
		raise ErrorWrong('token')

	#

	db['tokens'].remove(res['_id'])

# Проверить

def check(this, **x):
	if this.user['admin'] < 3:
		return {
			'error': 1,
		}

	return {
		'error': 0,
	}