import torch
import torch.nn as nn
import torch.nn.functional as F

class CyberPulseDNN(nn.Module):
    def __init__(self, input_dim=5, output_dim=10):
        super(CyberPulseDNN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, output_dim)
        
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

def save_model(model, path="models/cyberpulse_ids_model.pt"):
    torch.save(model.state_dict(), path)
    print(f"[*] Model saved to {path}")

def load_model(path="models/cyberpulse_ids_model.pt", input_dim=5):
    model = CyberPulseDNN(input_dim=input_dim)
    if torch.cuda.is_available():
        model.load_state_dict(torch.load(path))
        model.cuda()
    else:
        model.load_state_dict(torch.load(path, map_location=torch.device('cpu')))
    model.eval()
    return model

if __name__ == "__main__":
    model = CyberPulseDNN()
    print(model)
    # Create a dummy model file if it doesn't exist
    import os
    if not os.path.exists("models"):
        os.makedirs("models")
    save_model(model)
