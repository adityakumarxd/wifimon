from flask_socketio import join_room
from .extensions import socketio

@socketio.on('join_room')
def on_join(room):
    join_room(room)
