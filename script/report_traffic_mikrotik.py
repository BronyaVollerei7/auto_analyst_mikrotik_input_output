import pandas as pd
from pathlib import Path

def report_traffic(date_str: str):

      BASE_DIR = Path(__file__).resolve().parent.parent

      CLEAN_DIR = BASE_DIR / "analyst_data_clean"
      REPORT_ROOT = BASE_DIR / "analyst_report"

      # Change Date string
      date_folder = pd.to_datetime(date_str).strftime("%Y-%m-%d")

      # pake konsep folder = tanggal
      REPORT_DIR = REPORT_ROOT / date_folder
      REPORT_DIR.mkdir(parents=True, exist_ok=True)

      clean_file = CLEAN_DIR / f"traffic_clean_{date_str}.csv"

      if not clean_file.exists():
            raise FileNotFoundError(f"CLEAN file tidak ditemukan: {clean_file}")

      # clean data
      df = pd.read_csv(clean_file)
      df["timestamp"] = pd.to_datetime(df["timestamp"])

      # summary
      summary = df.groupby("interface").agg(
            avg_rx_mb=("rx_delta_mb", "mean"),
            avg_tx_mb=("tx_delta_mb", "mean"),
            total_rx_mb=("rx_delta_mb", "sum"),
            total_tx_mb=("tx_delta_mb", "sum"),
      ).reset_index()

      total_rx = summary["total_rx_mb"].sum()
      total_tx = summary["total_tx_mb"].sum()

      summary_file = REPORT_DIR / "summary.csv"
      summary.to_csv(summary_file, index=False)

      # peak traffic
      peak_rx_df = (
      df.loc[df.groupby("interface")["rx_delta_mb"].idxmax()]
      .assign(type="RX", value_mb=lambda x: x["rx_delta_mb"])
      [["interface", "type", "timestamp", "value_mb"]]
      )

      peak_tx_df = (
      df.loc[df.groupby("interface")["tx_delta_mb"].idxmax()]
      .assign(type="TX", value_mb=lambda x: x["tx_delta_mb"])
      [["interface", "type", "timestamp", "value_mb"]]
      )

      peak_df = pd.concat([peak_rx_df, peak_tx_df], ignore_index=True)

      peak_file = REPORT_DIR / "peak.csv"
      peak_df.to_csv(peak_file, index=False)

      # Report Text
      peak_rx_rows = peak_df[peak_df["type"] == "RX"]
      peak_tx_rows = peak_df[peak_df["type"] == "TX"]

      peak_rx_rows = peak_rx_rows.sort_values("value_mb", ascending=False)
      peak_tx_rows = peak_tx_rows.sort_values("value_mb", ascending=False)

      rx_lines = "\n".join(
      f"- {row.interface} | {row.timestamp} | {row.value_mb:.2f} MB"
      for row in peak_rx_rows.itertuples()
      )

      tx_lines = "\n".join(
      f"- {row.interface} | {row.timestamp} | {row.value_mb:.2f} MB"
      for row in peak_tx_rows.itertuples()
      )     

      report_text = f"""
AUTO ANALYST REPORT - {date_folder}

PEAK RX PER INTERFACE
{rx_lines}

PEAK TX PER INTERFACE
{tx_lines}

DAILY TOTAL
- RX Total : {total_rx:.2f} MB
- TX Total : {total_tx:.2f} MB
      """

      report_file = REPORT_DIR / "report.txt"
      report_file.write_text(report_text.strip())

      print("REPORT Success DIBUAT:")
      print(f"- {summary_file}")
      print(f"- {peak_file}")
      print(f"- {report_file}")
