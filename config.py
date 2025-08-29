import os
from dotenv import load_dotenv

# Load environment variables from .env file if present (for local development)
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    ROUTER_IP = os.environ.get('ROUTER_IP', '192.168.1.1')
    ROUTER_USERNAME = os.environ.get('ROUTER_USERNAME', 'admin')
    ROUTER_PASSWORD = os.environ.get('ROUTER_PASSWORD', 'password')
    NETWORK_SUBNET = os.environ.get('NETWORK_SUBNET', '192.168.1.0/24')
