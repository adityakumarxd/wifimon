from flask_socketio import SocketIO

socketio = SocketIO()

def init_socketio(app):
    socketio.init_app(app)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    print('Received message: ' + data)
    socketio.send('Message received')