#!env/bin/python
from app import app

from sets import SERVER
import logging


if __name__ == '__main__':
	logging.warning('starting server')
	app.run(
		host=SERVER['ip'],
		port=SERVER['port'],
		debug=True,
		threaded=True,
	)
	logging.warning('server started')