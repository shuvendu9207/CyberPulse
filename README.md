# 🛡️ CyberPulse — AI-Powered IDS Dashboard

**CyberPulse** is a professional, real-time Intrusion Detection System (IDS) dashboard. It integrates live network packet sniffing, AI-driven threat classification using PyTorch, and a dynamic 3D globe visualization of global attack patterns using live internet threat intelligence.

---

## 🚀 Quick Start
To get the dashboard running immediately:
```bash
# Clone
git clone https://github.com/shuvendu9207/cyberpulse.git && cd cyberpulse

# Setup & Install
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt

# Run
py -m streamlit run app.py
```
> **Prerequisite:** [Npcap](https://npcap.com/#download) must be installed on Windows for packet sniffing functionality.

---

## ✨ Key Features
- 🌍 **Live 3D Attack Globe**: Sychronized with [URLhaus](https://urlhaus.abuse.ch) data, visualizing live malware hosts attacking globally.
- 🧠 **ML-Driven Detection**: Deep Learning model (PyTorch DNN) classifies every captured packet as `NORMAL` or `THREAT` based on traffic patterns.
- 📡 **Real-time Sniffing**: Uses Scapy to capture and analyze live network traffic with sub-second latency.
- 🌓 **Premium UI**: Glassmorphic dashboard with Dark/Light mode support and auto-rotating live threat feed.
- 📱 **Mobile Optimized**: Responsive layout with compact analytics for security monitoring on the go.

---

## 🗂️ Technical Architecture & Structure
The project is built with a modular architecture:
- `app.py`: The dashboard engine (Streamlit) and real-time UI logic.
- `ml/`: Contains the PyTorch `model.py`, `train.py` for retraining, and the high-level `predictor.py`.
- `processing/`: Intelligent `feature_extractor.py` converts raw hex/binary packets into numerical ML input.
- `sensors/`: Backend packet sniffers that feed the real-time logs.
- `models/`: Persistent storage for optimized PyTorch weight files (`.pt`).
- `data_lake/`: Aggregated datasets of captured traffic for future model improvements.

---

## 🛠️ Technical Specifications
- **Model**: Fully-connected Deep Neural Network (DNN) with ReLU activations and Dropout layers.
- **Data Source**: URLhaus (abuse.ch) live feed, cached every 30s to provide up-to-the-minute global threat intel.
- **Frontend**: Streamlit with custom CSS/JS for glassmorphism and 3D globe rendering.
- **Networking**: Scapy for raw packet manipulation and protocol analysis.

---

## 👤 Author
**Shuvendu Kumar Mohapatra**
- 📧 [shuvendukumarmohapatra92@gmail.com](mailto:shuvendukumarmohapatra92@gmail.com)
- 🐙 [GitHub: shuvendu9207](https://github.com/shuvendu9207)
- 🔗 [LinkedIn: shuvendu-kumar-mohapatra](https://linkedin.com/in/shuvendu-kumar-mohapatra)

---
<p align="center">
  <b>CyberPulse v1.5.0</b> — Advanced AI-Powered Network Security Dashboard
</p>
