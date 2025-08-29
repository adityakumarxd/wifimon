import socket
import struct
import binascii

class TrafficSniffer:
    def __init__(self, interface):
        self.interface = interface
        self.sock = None

    def start_sniffing(self):
        self.sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
        self.sock.bind((self.interface, 0))

    def stop_sniffing(self):
        if self.sock:
            self.sock.close()
            self.sock = None

    def parse_packet(self, raw_data):
        eth_header = raw_data[:14]
        eth = struct.unpack('!6s6sH', eth_header)
        dest_mac = binascii.hexlify(eth[0]).decode()
        src_mac = binascii.hexlify(eth[1]).decode()
        eth_protocol = eth[2]

        return {
            'dest_mac': dest_mac,
            'src_mac': src_mac,
            'protocol': eth_protocol,
            'raw_data': raw_data
        }

    def sniff(self):
        while True:
            raw_data, addr = self.sock.recvfrom(65536)
            packet = self.parse_packet(raw_data)
            print(packet)  
