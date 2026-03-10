from scapy.all import sniff, IP, TCP, UDP
import json
import time
import os

LOG_FILE = "logs/sniffed_packets.json"

def packet_callback(packet):
    if IP in packet:
        packet_info = {
            "timestamp": time.time(),
            "src_ip": packet[IP].src,
            "dst_ip": packet[IP].dst,
            "proto": packet[IP].proto,
            "size": len(packet)
        }
        
        if TCP in packet:
            packet_info["dst_port"] = packet[TCP].dport
        elif UDP in packet:
            packet_info["dst_port"] = packet[UDP].dport
        else:
            packet_info["dst_port"] = 0

        # Save to a temporary log for the dashboard to read
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(packet_info) + "\n")

def start_sniffing(interface=None):
    print(f"[*] Starting packet sniffer on {interface if interface else 'default interface'}...")
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    if not os.path.exists("logs"):
        os.makedirs("logs")
    start_sniffing()
