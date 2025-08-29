import os

# The following router-related config settings are placeholders for future implementation.
# Uncomment and configure them when adding router login and network scanning functionality.

# ROUTER_IP = os.environ.get('ROUTER_IP', '192.168.1.1')  # Router admin IP address
# ROUTER_USERNAME = os.environ.get('ROUTER_USERNAME', 'admin')  # Router login username
# ROUTER_PASSWORD = os.environ.get('ROUTER_PASSWORD', 'password')  # Router login password
# NETWORK_SUBNET = os.environ.get('NETWORK_SUBNET', '192.168.1.0/24')  # Network subnet for scanning

# Secret key for Flask app session security (in use)
SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
