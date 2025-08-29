from flask import Flask
from config import Config
from threading import Thread
from .traffic_sniffer import start_sniffer
from .extensions import socketio
from .socketio_events import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    socketio.init_app(app)

    from .routes import main_bp
    from .auth import auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    Thread(target=start_sniffer, daemon=True).start()

    return app
