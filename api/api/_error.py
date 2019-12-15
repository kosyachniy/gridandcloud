# Не все параметры

class ErrorSpecified(Exception):
	def __init__(self, par):
		self.txt = par

# Занято

class ErrorBusy(Exception):
	def __init__(self, par):
		self.txt = par

# Недопустимый
# Не проходит по критерям

class ErrorInvalid(Exception):
	def __init__(self, par):
		self.txt = par

# Неправильный
# Проходит по критериям, но неверный

class ErrorWrong(Exception):
	def __init__(self, par):
		self.txt = par

# Загрузка на сервер

class ErrorUpload(Exception):
	def __init__(self, par):
		self.txt = par

# Нет прав

class ErrorAccess(Exception):
	def __init__(self, par):
		self.txt = par

# Неправильный тип данных

class ErrorType(Exception):
	def __init__(self, par):
		self.txt = par