from app import socketio
from flask_socketio import emit

def notify_traffic(data):
    socketio.emit('new_traffic', data, broadcast=True)
