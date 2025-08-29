import os
import subprocess

def scan_network():
    """
    Scans the local network for devices and returns a list of IP addresses.
    """
    try:
        output = subprocess.check_output(['arp-scan', '-l']).decode('utf-8')
        devices = []
        for line in output.splitlines()[2:]:  
            parts = line.split()
            if len(parts) > 1:
                devices.append(parts[0])  # first part = IP address
        return devices
    except Exception as e:
        print(f"Error scanning network: {e}")
        return []

def get_device_info(ip_address):
    device_info = {
        'ip_address': ip_address,
        'hostname': os.popen(f'nslookup {ip_address}').read().strip(),
        'status': 'active'  
    }
    return device_info