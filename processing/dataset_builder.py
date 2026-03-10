import pandas as pd
import os
import json

DATA_LAKE_DIR = "data_lake/"
RAW_LOGS = "logs/sniffed_packets.json"

def build_dataset():
    if not os.path.exists(RAW_LOGS):
        print("[-] No raw logs found to build dataset.")
        return

    packets = []
    with open(RAW_LOGS, "r") as f:
        for line in f:
            packets.append(json.loads(line))

    df = pd.DataFrame(packets)
    output_path = os.path.join(DATA_LAKE_DIR, f"network_traffic_{pd.Timestamp.now().strftime('%Y%m%d')}.parquet")
    
    if not os.path.exists(DATA_LAKE_DIR):
        os.makedirs(DATA_LAKE_DIR)
        
    df.to_parquet(output_path)
    print(f"[+] Dataset saved to {output_path}")

if __name__ == "__main__":
    build_dataset()
