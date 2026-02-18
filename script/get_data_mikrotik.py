import csv
import os
from dotenv import load_dotenv
from routeros_api import RouterOsApiPool
from datetime import datetime
from pathlib import Path

def collect_traffic():

      load_dotenv()
      # Setup MikroTik API
      ROUTER_IP = os.getenv("MIKROTIK_IP")
      PORT      = int(os.getenv("MIKROTIK_PORT", "8728"))
      USERNAME  = os.getenv("MIKROTIK_USER")
      PASSWORD  = os.getenv("MIKROTIK_PASS")      

      if not all([ROUTER_IP, USERNAME, PASSWORD]):
            raise RuntimeError("Yang bener lah apaan!! env nya dlu lah tolol")      

      try:
      # Login Connection Mikrotik
            routing_api = RouterOsApiPool(
            host=ROUTER_IP,
            username=USERNAME,
            password=PASSWORD,
            port=PORT,
            plaintext_login=True
            )

            api = routing_api.get_api()

            # Ambil Interface
            interfaces = api.get_resource('/interface')
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # File Path Loc
            BASE_DIR = Path(__file__).resolve().parent.parent
            RAW_DIR = BASE_DIR / "analyst_data_raw"
            RAW_DIR.mkdir(exist_ok=True)
            date_str  = datetime.now().strftime("%Y%m%d")
            file_path = os.path.join(RAW_DIR, f"traffic_raw_{date_str}.csv")
            file_exists = os.path.isfile(file_path)

            with open(file_path, "a", newline="", encoding="utf-8") as f:
                  writer = csv.writer(f)

                  if not file_exists:
                        writer.writerow(["timestamp", "interface", "rx_byte", "tx_byte"])

                  for i in interfaces.get():
                        name = i.get("name")
                        rx   = int(i.get("rx-byte", 0))
                        tx   = int(i.get("tx-byte", 0))

                        if name and ("ether" in name or "bridge" in name):
                              writer.writerow([timestamp, name, rx, tx])

            routing_api.disconnect()
            print(f"Data Train Berhasil ke save di {file_path}")
      except Exception as e:
            routing_api.disconnect()
            print("❌ ERROR:", e)
      