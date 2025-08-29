import subprocess
from flask import current_app

def scan_network_devices():
    subnet = current_app.config.get('NETWORK_SUBNET', '192.168.1.0/24')
    devices = []

    try:
        result = subprocess.check_output(['arp-scan', '-l'], text=True)
        lines = result.split('\n')
        
        for line in lines:
            parts = line.split()
            if len(parts) >= 2:
                ip, mac = parts[0], parts[1]
                devices.append({'ip': ip, 'mac': mac, 'hostname': 'Unknown'})
    except Exception as e:
        print(f"Error scanning network: {e}")

    return devices
