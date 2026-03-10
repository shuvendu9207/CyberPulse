import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import pandas as pd
import os
import glob
from ml.model import CyberPulseDNN, save_model
from processing.feature_extractor import FeatureExtractor

def load_data_from_lake(data_lake_dir="data_lake/"):
    files = glob.glob(os.path.join(data_lake_dir, "*.parquet"))
    if not files:
        print("[-] No training data found in data lake.")
        return None
    
    dfs = [pd.read_parquet(f) for f in files]
    return pd.concat(dfs, ignore_index=True)

def train_model(epochs=10, batch_size=32, lr=0.001):
    print("[*] Starting model retraining...")
    df = load_data_from_lake()
    if df is None: return

    extractor = FeatureExtractor()
    features_list = []
    labels_list = []

    print(f"[*] Processing {len(df)} samples...")
    for _, row in df.iterrows():
        feat = extractor.extract(row.to_dict())
        features_list.append(list(feat.values()))
        # Labeling logic: 0 for normal, 1 for large packets (pseudo-threat)
        # In real IDS, this would be based on actual labels.
        label = 1 if feat['packet_size'] > 1000 else 0
        labels_list.append(label)

    X = torch.tensor(features_list, dtype=torch.float32)
    y = torch.tensor(labels_list, dtype=torch.long)

    dataset = TensorDataset(X, y)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    model = CyberPulseDNN(input_dim=X.shape[1], output_dim=10) # 10 classes as per specification
    if torch.cuda.is_available():
        model.cuda()
    
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)

    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for inputs, targets in loader:
            if torch.cuda.is_available():
                inputs, targets = inputs.cuda(), targets.cuda()
            
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        
        print(f"Epoch {epoch+1}/{epochs} | Loss: {running_loss/len(loader):.4f}")

    save_model(model)
    print("[+] Training complete. Model updated.")

if __name__ == "__main__":
    train_model()
