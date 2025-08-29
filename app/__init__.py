from flask import Flask
from flask_socketio import SocketIO
from config import Config

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    socketio.init_app(app)

    from .routes import main_bp
    from .auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app
