import os
from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tajny-kluc-pre-caller'
# Povolíme CORS, aby sa dalo pripojiť aj z desktopovej appky alebo webu
socketio = SocketIO(app, cors_allowed_origins="*")

# Jednoduchá úvodná stránka, aby bolo vidieť, že server žije
@app.route('/')
def index():
    return "we are online"
