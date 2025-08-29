from scapy.all import sniff, IP, TCP, Raw
import re
from .socketio_server import notify_traffic

http_request_pattern = re.compile(rb"^(GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH|TRACE|CONNECT) (.+?) HTTP/1\.[01]\r\n", re.I)

def parse_http_request(payload):
    match = http_request_pattern.match(payload)
    if match:
        method = match.group(1).decode()
        path = match.group(2).decode()
        return {"method": method, "path": path}
    return None

def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP) and packet.haslayer(Raw):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
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

def start_sniffer():
    sniff(filter="tcp port 80", prn=packet_callback, store=0)
