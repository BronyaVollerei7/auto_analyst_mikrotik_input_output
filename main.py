from datetime import datetime,timedelta
import time 
from script.get_data_mikrotik import collect_traffic
from script.process_traffic_mikrotik import clean_traffic
from script.report_traffic_mikrotik import report_traffic

# Jarak Jalan nya sekarang 5 menit sekali doang
MINUTE = 60
# Kalau Mau nambah Jam tinggal rubah run duration di depan nya itu aja jadi jam berapa cuy 
HOUR   = 3600
INTERVAL_SECONDS = 5 * MINUTE
RUN_DURATION     = 3 * HOUR

def main():
  
      start_time = datetime.now()
      end_time   = start_time + timedelta(seconds=RUN_DURATION)
      print(f"Data Collect Mulai {start_time}")
      data_count = 0

      while datetime.now() < end_time:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Ambil jam {now}")
            data_count += 1

            collect_traffic()

            #  No Sleep
            if datetime.now() + timedelta(seconds=INTERVAL_SECONDS) > end_time:
                  break

            time.sleep(INTERVAL_SECONDS)
      
      print("Ambil Data 1 jam")
      print(f"total_data {data_count}")
      date_str = start_time.strftime("%Y%m%d")
      clean_traffic(date_str)
      report_traffic(date_str)

if __name__ == "__main__":
    main()
