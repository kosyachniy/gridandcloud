from flask import Flask
from flask_cors import CORS

from sets import SERVER

#

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

# Socket.IO

from flask_socketio import SocketIO
sio = SocketIO(app, async_mode=None)

#


from app import api
from app import sockets