from .extensions import socketio

def notify_traffic(device_ip, data):
    socketio.emit('new_traffic', data, room=device_ip)
