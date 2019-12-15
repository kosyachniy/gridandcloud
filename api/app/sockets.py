from app import app, sio

import time

from mongodb import db

# Socket.IO

from threading import Lock
from flask_socketio import emit

thread = None
thread_lock = Lock()


# Онлайн

@sio.on('online', namespace='/main')
def online(x):
	# global thread
	# with thread_lock:
	# 	if thread is None:
	# 		thread = sio.start_background_task(target=background_thread)

	pass


if __name__ == '__main__':
	sio.run(app)


# def background_thread():
# 	while True:
# 		timestamp = time.time()

# 		#

# 		pass

# 		#

# 		time.sleep(5)