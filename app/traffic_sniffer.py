import netifaces
from scapy.all import sniff, IP, TCP, Raw
import re
from .socketio_server import notify_traffic

http_request_pattern = re.compile(
    rb"^(GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH|TRACE|CONNECT) (.+?) HTTP/1\.[01]\r\n",
    re.I
)

def parse_http_request(payload):
    match = http_request_pattern.match(payload)
    if match:
        method = match.group(1).decode()
        path = match.group(2).decode()
        return {"method": method, "path": path}
    return None

def get_default_interface():
    gateways = netifaces.gateways()
    default_gateway = gateways.get('default')
    if default_gateway:
        iface = default_gateway.get(netifaces.AF_INET)
        if iface:
            return iface[1]
    return 'en0'  # fallback

def parse_tls_sni(data):
    try:
        if data[0] != 0x16:
            return None
        handshake = data[5:]
        if handshake[0] != 0x01:
            return None
        idx = 38
        session_id_len = handshake[38]
        idx += 1 + session_id_len
        cipher_suites_len = int.from_bytes(handshake[idx:idx+2], 'big')
        idx += 2 + cipher_suites_len
        comp_methods_len = handshake[idx]
        idx += 1 + comp_methods_len
        extensions_len = int.from_bytes(handshake[idx:idx+2], 'big')
        idx += 2
        end = idx + extensions_len
        while idx + 4 <= end:
            ext_type = int.from_bytes(handshake[idx:idx+2], 'big')
            ext_len = int.from_bytes(handshake[idx+2:idx+4], 'big')
            idx += 4
            if ext_type == 0x0000:  # Server Name extension
                server_name_list_len = int.from_bytes(handshake[idx:idx+2], 'big')
                idx += 2
                server_name_type = handshake[idx]
                idx += 1
                server_name_len = int.from_bytes(handshake[idx:idx+2], 'big')
                idx += 2
                server_name = handshake[idx:idx+server_name_len].decode()
                return server_name
            idx += ext_len
    except Exception:
        return None

def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst

        if packet.haslayer(Raw):
            payload = bytes(packet[Raw])
            http_data = parse_http_request(payload)
            if http_data:
                info = {
                    'src_ip': ip_src,
                    'dst_ip': ip_dst,
                    'method': http_data['method'],
                    'path': http_data['path'],
                    'timestamp': packet.time
                }
                notify_traffic(ip_src, info)
                return

            sni = parse_tls_sni(payload)
            if sni:
                info = {
                    'src_ip': ip_src,
                    'dst_ip': ip_dst,
                    'method': 'SNI',
                    'path': sni,
                    'timestamp': packet.time
                }
                notify_traffic(ip_src, info)
                return

        info = {
            'src_ip': ip_src,
            'dst_ip': ip_dst,
            'method': 'TCP',
            'path': 'N/A',
            'timestamp': packet.time
        }
        notify_traffic(ip_src, info)

def start_sniffer():
    try:
        iface = get_default_interface()
        print(f"Using network interface: {iface}")
        sniff(iface=iface, filter='tcp', prn=packet_callback, store=0)
    except PermissionError:
        print("Permission denied: You need to run the app with elevated privileges (sudo).")
    except Exception as e:
        print(f"Error starting sniffer: {e}")
