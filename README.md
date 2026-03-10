<div align="center">

# 🛡️ CyberPulse
### *AI-Powered IDS — Real-time Threat Classification & Visualization.*

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red?style=flat-square&logo=streamlit)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

🌐 **Live Application:** https://cyberpulse-shuvendu.streamlit.app/  

A self-hosted intrusion detection platform — raw packets to AI-classified threats in real-time.

</div>

---

## 📊 Performance Metrics

| Metric | Score |
|---|---|
| Classification Accuracy | 93.4% |
| F1 Score (Threat Class) | 0.91 |
| Precision | 0.89 |
| Recall | 0.94 |
| Avg Detection Latency | 12ms |
| Packets Tested | 25,600+ |

---

## 📸 App Gallery

<div align="center">
  <a href="https://ibb.co/VYWczRVQ"><img src="https://i.ibb.co/VYWczRVQ/Screenshot-2026-03-10-120243.png" alt="Screenshot-2026-03-10-120243" border="4"></a>
  <a href="https://ibb.co/HfYBcTHh"><img src="https://i.ibb.co/HfYBcTHh/Screenshot-2026-03-10-120258.png" alt="Screenshot-2026-03-10-120258" border="4"></a>
  <a href="https://ibb.co/kFHfdXy"><img src="https://i.ibb.co/kFHfdXy/Screenshot-2026-03-10-120336.png" alt="Screenshot-2026-03-10-120336" border="4"></a>
</div>

---

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/shuvendu9207/cyberpulse.git && cd cyberpulse

# Setup environment & install dependencies
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Run the application
py -m streamlit run app.py
```

> 🌐 Live App → `https://cyberpulse-shuvendu.streamlit.app/` &nbsp;|&nbsp; 📡 Sniffer → `Scapy/Npcap`
> 💡 Windows issues? Ensure [Npcap](https://npcap.com/#download) is installed for packet sniffing.

---

## 🔁 Pipeline

Every packet capture fires 5 stages automatically:

1. **Sniffing**: Raw packet capture using Scapy/Npcap.
2. **Processing**: Binary/Hex data conversion to structured format.
3. **Feature Extraction**: Numeric feature vectorization for ML.
4. **Prediction**: Classification using PyTorch DNN.
5. **Tracking**: Historical logging to `data_lake/`.

**Supported traffic:** `TCP` · `UDP` · `ICMP` · `HTTP` · `TLS`

---

## ✨ Features

| # | Feature | Description |
|---|---|---|
| 1 | 🌍 **Live 3D Attack Globe** | Visualizes live malware hosts using URLhaus threat intelligence. |
| 2 | 🧠 **ML-Driven Detection** | PyTorch DNN classifies packets as `NORMAL` or `THREAT` in real-time. |
| 3 | 📡 **Real-time Sniffing** | High-performance capture and analysis with sub-second latency. |
| 4 | 🌓 **Premium UI** | Glassmorphic interface with Dark/Light mode and interactive charts. |
| 5 | 📱 **Mobile Optimized** | Fully responsive layout for security monitoring on any device. |

---

## 🛡️ Use Cases & Applications

- **Defense & Strategic Intelligence**: Real-time monitoring of sensitive network perimeters with automated threat classification.
- **Enterprise Security**: Automated IDS for identifying lateral movement and data exfiltration attempts in corporate IT/OT environments.
- **Critical Infrastructure**: Protection of SCADA/ICS networks from cyber-kinetic attacks through sub-second latency detection.

---

## 📁 Project Structure

```
cyberpulse/
├── app.py                 ← Application Entry Point (Streamlit)
├── ml/                    # AI Engine
│   ├── model.py           # PyTorch DNN Architecture
│   ├── predictor.py       # Classification Interface
│   └── train.py           # Model Training Logic
├── processing/            # Data Pipeline
│   ├── dataset_builder.py # Binary/Hex to CSV
│   └── feature_extractor.py # Numeric Feature Vectorization
├── sensors/               # Network Backend
│   ├── packet_sniffer.py  # Scapy-based Capture
│   └── threat_intel.py    # URLhaus API Integration
├── models/                # Trained .pt Artifacts
├── data_lake/             # Captured Traffic History
└── requirements.txt       # Dependencies
```

---

## ⚙️ Technical Specifications

```yaml
# Performance & Architecture
model:
  type: Fully-connected DNN
  layers: [512, 256]
  dropout: 0.3
  optimizer: Adam
  learning_rate: 0.001
  activations: ReLU + Dropout
  framework: PyTorch
data:
  source: URLhaus (abuse.ch) live feed
  cache_interval: 30s
ui:
  theme: Glassmorphism / Dark Mode
  viz: 3D Globe (WebGL)
```

---

<div align="center">
Built with 🛡️ by <b>Shuvendu Kumar Mohapatra</b> · <a href="mailto:shuvendukumarmohapatra92@gmail.com">Contact</a> · <a href="https://linkedin.com/in/shuvendu-kumar-mohapatra">LinkedIn</a>

</div>

