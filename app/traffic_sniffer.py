import threading
from scapy.all import sniff, IP, TCP
from flask import current_app
from .socketio_server import notify_traffic

def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        if packet[TCP].dport == 80 or packet[TCP].sport == 80:  # HTTP traffic only
            info = {
                'src_ip': ip_src,
                'dst_ip': ip_dst,
                'timestamp': packet.time
            }
            notify_traffic(info)

def start_sniffer():
    sniff(filter="tcp port 80", prn=packet_callback, store=0)  # Non-blocking sniffing
