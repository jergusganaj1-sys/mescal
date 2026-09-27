from flask import Flask
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tajny-kluc-zabezpecenia'

# Použijeme threading režim, ktorý je maximálne stabilný a nepadá na verziách Pythonu
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

@app.route('/')
def index():
    return "Server pre Online Caller beží v poriadku! 🎙️"

@socketio.on('connect')
def handle_connect():
    print("Klient sa pripojil.")

@socketio.on('disconnect')
def handle_disconnect():
    print("Klient sa odpojil.")

@socketio.on('join_call')
def on_join(data):
    room = data.get('room', 'global_room')
    join_room(room)
    print(f"Používateľ vstúpil do miestnosti: {room}")
    emit('status', {'msg': f'Úspešne pripojený do miestnosti: {room}'}, room=room)

@socketio.on('leave_call')
def on_leave(data):
    room = data.get('room', 'global_room')
    leave_room(room)
    print(f"Používateľ opustil miestnosť: {room}")

@socketio.on('audio_data')
def handle_audio(data):
    room = data.get('room')
    audio = data.get('audio')
    # Preposlanie audio dát všetkým ostatným v miestnosti
    emit('audio_stream', {'audio': audio}, room=room, include_self=False)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
