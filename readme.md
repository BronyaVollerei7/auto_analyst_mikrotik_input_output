<div align="center">

# 📡 MikroTik Auto Analysis

<p>Sistem otomatis untuk mengambil, membersihkan, dan menganalisis data traffic<br/>dari perangkat <strong>MikroTik RouterOS</strong> dengan pendekatan modular.</p>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![RouterOS](https://img.shields.io/badge/MikroTik-RouterOS%20API-293239?style=for-the-badge&logo=mikrotik&logoColor=white)
![CSV](https://img.shields.io/badge/Format-CSV%20Processing-10b981?style=for-the-badge)

</div>

---

## 🚀 Features

| Icon | Fitur | Deskripsi |
|------|-------|-----------|
| 📡 | **Auto Fetch Traffic** | Ambil data traffic langsung dari MikroTik RouterOS secara otomatis |
| 🧹 | **Data Cleaning** | Preprocessing & cleaning otomatis untuk data yang siap dianalisis |
| 📊 | **Generate Report** | Laporan analisis traffic yang informatif dan terstruktur |
| 🧩 | **Modular & Scalable** | Struktur project yang mudah dikembangkan dan di-maintain |
| 🔑 | **Env-Based Config** | Konfigurasi aman berbasis `.env` tanpa hardcode credential |

---

## 📂 Project Structure

```
MIKROTIK_AUTO_ANALYSIS/
│
├── .venv/                           # 🐍 Virtual environment
├── analyst_data_clean/              # 🧹 Data hasil cleaning
├── analyst_data_raw/                # 📥 Data mentah dari MikroTik
│   └── traffic_raw_YYYYMMDD.csv
│
├── analyst_report/                  # 📋 Hasil report analisis
│
├── script/
│   ├── get_data_mikrotik.py         # 🔌 Fetch data
│   ├── process_traffic_mikrotik.py  # ⚙️  Processing
│   └── report_traffic_mikrotik.py   # 📝 Reporting
│
├── .env                             # 🔑 Credential (tidak di-push)
├── .env.example                     # 📄 Template environment
├── .gitignore
└── main.py                          # 🏁 Entry point
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/BronyaVollerei7/auto_analyst_mikrotik_input_output.git
cd auto_analyst_mikrotik_input_output
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

> 🪟 **Windows**
> ```bash
> .venv\Scripts\activate
> ```

> 🍎 **Mac / Linux**
> ```bash
> source .venv/bin/activate
> ```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Environment

```bash
cp .env.example .env
```

Isi dengan credential MikroTik kamu:

```env
MIKROTIK_IP=yourmikrotikIP
MIKROTIK_USER=yourmikroikuser
MIKROTIK_PASS=yourmikrotikpasword
MIKROTIK_PORT=yourmikrotikport
```

> ⚠️ **Jangan commit file `.env` ke repository!**

---

## ▶️ Usage

🔄 Menjalankan **full pipeline**:

```bash
python main.py
```

🧩 Menjalankan **per modul**:

```bash
python script/get_data_mikrotik.py
python script/process_traffic_mikrotik.py
python script/report_traffic_mikrotik.py
```

---

## 🔄 Workflow

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  📡 Collection    │────▶│  🔧 Processing    │────▶│  📊 Reporting    │
│                  │     │                  │     │                  │
│ get_data_        │     │ process_traffic_ │     │ report_traffic_  │
│ mikrotik.py      │     │ mikrotik.py      │     │ mikrotik.py      │
└──────────────────┘     └──────────────────┘     └──────────────────┘
```

1. **📡 Data Collection** — Mengambil data traffic langsung dari router MikroTik
2. **🔧 Data Processing** — Cleaning, transform, dan agregasi data traffic
3. **📊 Reporting** — Generate laporan analisis traffic yang terstruktur

---

## 📈 Output Directory

| Folder | Isi |
|--------|-----|
| 📥 `analyst_data_raw/` | Data mentah hasil fetch dari router |
| 🧹 `analyst_data_clean/` | Data setelah proses cleaning |
| 📋 `analyst_report/` | Laporan analisis final |

---

## 🔐 Security Notes

> [!WARNING]
> Jaga credential MikroTik kamu tetap aman!

- 🔑 Gunakan `.env` untuk menyimpan semua credential — jangan hardcode di dalam script
- 🚫 Jangan pernah expose username & password router ke publik atau push ke repository
- 👁️ Pastikan `.env` sudah terdaftar di `.gitignore` sebelum commit

---

## 🧠 Tech Stack

| Teknologi | Kegunaan |
|-----------|----------|
| 🐍 **Python 3.x** | Core language untuk semua script |
| 🐼 **Pandas** | Data manipulation & analysis |
| 🌐 **MikroTik RouterOS API** | Interface ke perangkat router |
| 📄 **CSV Processing** | Format data input & output |

---

## 📌 Use Case

Project ini cocok untuk:

- 🖥️ Monitoring traffic kantor
- 📶 Analisa penggunaan bandwidth
- 🔍 Audit jaringan internal
- 🤖 Automation reporting harian

---

## 🏗️ Future Improvements

- [ ] ⏰ Scheduler otomatis (cron / task scheduler)
- [ ] 🗄️ Database integration (PostgreSQL / MySQL)
- [ ] 🌐 Web dashboard (Flask / FastAPI)
- [ ] 📉 Visualisasi chart interaktif
- [ ] 🐳 Deployment ke server / container (Docker)

---

<div align="center">

## 👤 Author

**BronyaVollerei**

🛠️ *Developed for network traffic automation and data analysis workflow*

</div>