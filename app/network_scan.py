import subprocess
import platform
import re
from flask import current_app
from mac_vendor_lookup import MacLookup
MacLookup().update_vendors()

ip_regex = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
mac_regex = re.compile(r"([0-9A-Fa-f]{2}[:\-]){5}([0-9A-Fa-f]{2})")

mac_lookup = MacLookup()

def get_mac_vendor(mac):
    try:
        return mac_lookup.lookup(mac)
    except Exception:
        return "Unknown Vendor"

def deduplicate_devices(devices):
    seen = set()
    unique_devices = []
    for d in devices:
        if d['ip'] not in seen:
            unique_devices.append(d)
            seen.add(d['ip'])
    return unique_devices

def scan_network_devices_unix():
    devices = []
    try:
        result = subprocess.check_output(['arp-scan', '-l'], text=True)
        lines = result.split('\n')
        for line in lines:
            parts = line.split()
            if len(parts) >= 2:
                ip, mac = parts[0], parts[1]
                if ip_regex.match(ip) and mac_regex.match(mac):
                    vendor = get_mac_vendor(mac)
                    devices.append({'ip': ip, 'mac': mac, 'vendor': vendor, 'hostname': 'Unknown'})
    except Exception as e:
        print(f"Error scanning network on Unix/macOS: {e}")
    return deduplicate_devices(devices)

def scan_network_devices_windows():
    devices = []
    try:
        result = subprocess.check_output(['arp', '-a'], text=True)
        lines = result.splitlines()
        for line in lines:
            parts = line.split()
            if len(parts) >= 2:
                ip_candidate = parts[0].strip("()")
                mac_candidate = parts[1]
                if ip_regex.match(ip_candidate) and mac_regex.match(mac_candidate):
                    vendor = get_mac_vendor(mac_candidate)
                    devices.append({'ip': ip_candidate, 'mac': mac_candidate, 'vendor': vendor, 'hostname': 'Unknown'})
    except Exception as e:
        print(f"Error scanning network on Windows: {e}")
    return deduplicate_devices(devices)

def scan_network_devices():
    system_platform = platform.system()
    if system_platform == 'Windows':
        return scan_network_devices_windows()
    else:
        return scan_network_devices_unix()
