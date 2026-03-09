import requests
import json
import os

THREATFOX_API_URL = "https://threatfox.abuse.ch/export/json/recent/"
INTEL_FILE = "logs/threat_intel.json"

def fetch_threat_intel():
    print("[*] Fetching latest threat intelligence from ThreatFox...")
    try:
        response = requests.get(THREATFOX_API_URL)
        if response.status_code == 200:
            data = response.json()
            with open(INTEL_FILE, "w") as f:
                json.dump(data, f, indent=4)
            print("[+] Threat intelligence updated successfully.")
            return data
        else:
            print(f"[-] Failed to fetch threat intel: {response.status_code}")
    except Exception as e:
        print(f"[-] Error: {str(e)}")
    return None

if __name__ == "__main__":
    if not os.path.exists("logs"):
        os.makedirs("logs")
    fetch_threat_intel()
