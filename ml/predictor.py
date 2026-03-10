import torch
from ml.model import load_model
from processing.feature_extractor import FeatureExtractor
import numpy as np

class Predictor:
    def __init__(self, model_path="models/cyberpulse_ids_model.pt"):
        self.extractor = FeatureExtractor()
        try:
            self.model = load_model(model_path)
        except Exception as e:
            print(f"[-] Could not load model: {e}. Using dummy predictor.")
            self.model = None

    def predict(self, packet_dict):
        features = self.extractor.extract(packet_dict)
        # Convert features to tensor
        input_data = torch.tensor([list(features.values())], dtype=torch.float32)
        
        if self.model:
            with torch.no_grad():
                output = self.model(input_data)
                prediction = torch.argmax(output, dim=1).item()
        else:
            # Dummy prediction logic if model is missing
            prediction = 1 if features['packet_size'] > 1000 else 0
            
        return {
            "prediction": prediction,
            "threat_level": "High" if prediction > 0 else "Low",
            "features": features
        }

if __name__ == "__main__":
    predictor = Predictor()
    test_packet = {"size": 1500, "proto": 6, "dst_port": 443, "src_ip": "192.168.1.1"}
    print(predictor.predict(test_packet))
