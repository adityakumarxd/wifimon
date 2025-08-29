import os

class Config:
    ROUTER_USERNAME = os.environ.get('ROUTER_USERNAME') or 'test'
    ROUTER_PASSWORD = os.environ.get('ROUTER_PASSWORD') or 'test'
    NETWORK_INTERFACE = os.environ.get('NETWORK_INTERFACE') or 'eth0'
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'