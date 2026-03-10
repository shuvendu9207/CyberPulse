import pandas as pd
import numpy as np

class FeatureExtractor:
    def __init__(self):
        self.connection_counts = {}

    def extract(self, packet_dict):
        """
        Extracts features from a packet dictionary:
        - packet_size
        - protocol (numeric mapping)
        - destination_port
        - connection_rate (dummy logic for now)
        - payload_entropy (dummy logic)
        """
        features = {
            "packet_size": packet_dict.get("size", 0),
            "protocol": packet_dict.get("proto", 0),
            "destination_port": packet_dict.get("dst_port", 0),
            "connection_rate": self._calculate_rate(packet_dict.get("src_ip")),
            "payload_entropy": np.random.uniform(0, 8) # Placeholder for entropy calculation
        }
        return features

    def _calculate_rate(self, src_ip):
        if not src_ip: return 0
        self.connection_counts[src_ip] = self.connection_counts.get(src_ip, 0) + 1
        return self.connection_counts[src_ip]

if __name__ == "__main__":
    extractor = FeatureExtractor()
    test_packet = {"size": 64, "proto": 6, "dst_port": 80, "src_ip": "1.1.1.1"}
    print(f"Extracted Features: {extractor.extract(test_packet)}")
