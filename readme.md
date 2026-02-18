<div align="center">

# MikroTik Auto Analysis

<p>An automated system to fetch, clean, and analyze network traffic data<br/>from <strong>MikroTik RouterOS</strong> devices with a modular approach.</p>

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![RouterOS](https://img.shields.io/badge/MikroTik-RouterOS%20API-293239?style=for-the-badge&logo=mikrotik&logoColor=white)
![CSV](https://img.shields.io/badge/Format-CSV%20Processing-10b981?style=for-the-badge)

</div>

---

## 🚀 Features

| Icon | Feature | Description |
|------|---------|-------------|
| 📡 | **Auto Fetch Traffic** | Automatically retrieve traffic data directly from MikroTik RouterOS |
| 🧹 | **Data Cleaning** | Automated preprocessing & cleaning for analysis-ready data |
| 📊 | **Generate Report** | Produce informative and well-structured traffic analysis reports |
| 🧩 | **Modular & Scalable** | Clean project structure that's easy to extend and maintain |
| 🔑 | **Env-Based Config** | Secure credential management via `.env` — no hardcoding |

---

## 📂 Project Structure

```
MIKROTIK_AUTO_ANALYSIS/
│
├── .venv/                           # 🐍 Virtual environment
├── analyst_data_clean/              # 🧹 Cleaned output data
├── analyst_data_raw/                # 📥 Raw data from MikroTik
│   └── traffic_raw_YYYYMMDD.csv
│
├── analyst_report/                  # 📋 Analysis reports
│
├── script/
│   ├── get_data_mikrotik.py         # 🔌 Data fetching
│   ├── process_traffic_mikrotik.py  # ⚙️  Data processing
│   └── report_traffic_mikrotik.py   # 📝 Report generation
│
├── .env                             # 🔑 Credentials (never commit this)
├── .env.example                     # 📄 Environment template
├── .gitignore
└── main.py                          # 🏁 Entry point
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/BronyaVollerei7/auto_analyst_mikrotik_input_output.git
cd auto_analyst_mikrotik_input_output
```

### 2️⃣ Create a Virtual Environment

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

### 4️⃣ Configure Environment

```bash
cp .env.example .env
```

Fill in your MikroTik credentials:

```env
MIKROTIK_IP=yourmikrotikIP
MIKROTIK_USER=yourmikrotikuser
MIKROTIK_PASS=yourmikrotikpassword
MIKROTIK_PORT=yourmikrotikport
```

> ⚠️ **Never commit your `.env` file to the repository!**

---

## ▶️ Usage

🔄 Run the **full pipeline**:

```bash
python main.py
```

🧩 Run **individual modules**:

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

1. **📡 Data Collection** — Fetch raw traffic data directly from the MikroTik router
2. **🔧 Data Processing** — Clean, transform, and aggregate the traffic data
3. **📊 Reporting** — Generate structured and readable analysis reports

---

## 📈 Output Directory

| Folder | Contents |
|--------|----------|
| 📥 `analyst_data_raw/` | Raw data fetched from the router |
| 🧹 `analyst_data_clean/` | Data after cleaning & processing |
| 📋 `analyst_report/` | Final analysis reports |

---

## 🔐 Security Notes

> [!WARNING]
> Keep your MikroTik credentials safe at all times!

- 🔑 Always use `.env` to store credentials — never hardcode them in scripts
- 🚫 Never expose your router's username & password in public repositories
- 👁️ Make sure `.env` is listed in `.gitignore` before making any commits

---

## 🧠 Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 **Python 3.x** | Core language for all scripts |
| 🐼 **Pandas** | Data manipulation & analysis |
| 🌐 **MikroTik RouterOS API** | Interface to the router device |
| 📄 **CSV Processing** | Input & output data format |

---

## 📌 Use Cases

This project is ideal for:

- 🖥️ Office network traffic monitoring
- 📶 Bandwidth usage analysis
- 🔍 Internal network auditing
- 🤖 Automated daily reporting

---

## 🏗️ Future Improvements

- [ ] ⏰ Automated scheduler (cron / task scheduler)
- [ ] 🗄️ Database integration (PostgreSQL / MySQL)
- [ ] 🌐 Web dashboard (Flask / FastAPI)
- [ ] 📉 Interactive chart visualization
- [ ] 🐳 Server / container deployment (Docker)

---

<div align="center">

## 👤 Author

**BronyaVollerei**

🛠️ *Developed for network traffic automation and data analysis workflow*

</div>