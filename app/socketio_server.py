from .extensions import socketio

def notify_traffic(device_ip, data):
    # Emit to a global room 'all' to simplify client subscriptions
    socketio.emit('new_traffic', data, room='all')
