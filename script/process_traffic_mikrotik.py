import pandas as pd
from pathlib import Path

def clean_traffic(date_str: str):

      BASE_DIR = Path(__file__).resolve().parent.parent     

      RAW_DIR   = BASE_DIR / "analyst_data_raw"
      CLEAN_DIR = BASE_DIR / "analyst_data_clean"

      CLEAN_DIR.mkdir(exist_ok=True)

      raw_file   = RAW_DIR / f"traffic_raw_{date_str}.csv"
      clean_file = CLEAN_DIR / f"traffic_clean_{date_str}.csv"

      if not raw_file.exists():
         raise FileNotFoundError(f"RAW file tidak ditemukan: {raw_file}")

    # Load
      df = pd.read_csv(raw_file)

    # timestamp
      df["timestamp"] = pd.to_datetime(df["timestamp"])

    # sort supaya delta bener
      df = df.sort_values(["interface", "timestamp"])

    # Delta Calc
      df["rx_delta_byte"] = df.groupby("interface")["rx_byte"].diff()
      df["tx_delta_byte"] = df.groupby("interface")["tx_byte"].diff()

    #  Remove pertama
      df = df.dropna()
      df = df[(df["rx_delta_byte"] >= 0) & (df["tx_delta_byte"] >= 0)]

    # Convert ke MB kalau di excel tuh byte / (1024*1024)
      df["rx_delta_mb"] = (df["rx_delta_byte"] / 1_048_576).round(2)
      df["tx_delta_mb"] = (df["tx_delta_byte"] / 1_048_576).round(2)

    # Clean Buat CSV cuyt 
      clean_df = df[
            [
            "timestamp",
            "interface",
            "rx_delta_byte",
            "tx_delta_byte",
            "rx_delta_mb",
            "tx_delta_mb",
            ]
      ]

      # save
      clean_df.to_csv(clean_file, index=False)

      print(f"Processing Data ke Clean Berhasil Di save: {clean_file}")

