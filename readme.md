<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>MikroTik Auto Analysis</title>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet"/>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg: #0a0e1a;
      --bg2: #0f1526;
      --bg3: #141b30;
      --card: #111827;
      --border: #1e2d4a;
      --accent: #00d4ff;
      --accent2: #7c3aed;
      --accent3: #10b981;
      --accent4: #f59e0b;
      --text: #e2e8f0;
      --muted: #64748b;
      --code-bg: #070b14;
    }

    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Syne', sans-serif;
      min-height: 100vh;
      overflow-x: hidden;
    }

    /* BG Grid */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background-image:
        linear-gradient(rgba(0,212,255,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,212,255,0.03) 1px, transparent 1px);
      background-size: 40px 40px;
      pointer-events: none;
      z-index: 0;
    }

    .container {
      max-width: 900px;
      margin: 0 auto;
      padding: 40px 24px 80px;
      position: relative;
      z-index: 1;
    }

    /* HERO */
    .hero {
      text-align: center;
      padding: 60px 0 48px;
      position: relative;
    }

    .hero::after {
      content: '';
      display: block;
      width: 200px;
      height: 200px;
      background: radial-gradient(circle, rgba(0,212,255,0.15), transparent 70%);
      position: absolute;
      top: 0; left: 50%;
      transform: translateX(-50%);
      pointer-events: none;
      border-radius: 50%;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(0,212,255,0.08);
      border: 1px solid rgba(0,212,255,0.2);
      color: var(--accent);
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      padding: 6px 16px;
      border-radius: 100px;
      margin-bottom: 24px;
      animation: fadeDown 0.6s ease both;
    }

    .hero h1 {
      font-size: clamp(2.2rem, 6vw, 3.8rem);
      font-weight: 800;
      line-height: 1.1;
      background: linear-gradient(135deg, #fff 30%, var(--accent) 70%, var(--accent2) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: fadeDown 0.6s 0.1s ease both;
      margin-bottom: 16px;
    }

    .hero p {
      color: var(--muted);
      font-size: 1.05rem;
      max-width: 540px;
      margin: 0 auto 32px;
      line-height: 1.7;
      animation: fadeDown 0.6s 0.2s ease both;
    }

    .badges {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 10px;
      animation: fadeDown 0.6s 0.3s ease both;
    }

    .badge {
      padding: 5px 14px;
      border-radius: 100px;
      font-size: 12px;
      font-weight: 700;
      font-family: 'JetBrains Mono', monospace;
      border: 1px solid;
    }
    .badge-blue  { background: rgba(0,212,255,0.08); border-color: rgba(0,212,255,0.3); color: var(--accent); }
    .badge-purple{ background: rgba(124,58,237,0.08); border-color: rgba(124,58,237,0.3); color: #a78bfa; }
    .badge-green { background: rgba(16,185,129,0.08); border-color: rgba(16,185,129,0.3); color: var(--accent3); }
    .badge-amber { background: rgba(245,158,11,0.08); border-color: rgba(245,158,11,0.3); color: var(--accent4); }

    /* DIVIDER */
    .divider {
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--border), transparent);
      margin: 40px 0;
    }

    /* SECTION TITLE */
    .section-title {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 24px;
    }

    .section-title .icon {
      width: 36px; height: 36px;
      border-radius: 10px;
      display: flex; align-items: center; justify-content: center;
      font-size: 18px;
      flex-shrink: 0;
    }

    .icon-blue   { background: rgba(0,212,255,0.12); }
    .icon-purple { background: rgba(124,58,237,0.12); }
    .icon-green  { background: rgba(16,185,129,0.12); }
    .icon-amber  { background: rgba(245,158,11,0.12); }
    .icon-red    { background: rgba(239,68,68,0.12); }

    .section-title h2 {
      font-size: 1.25rem;
      font-weight: 700;
      color: #fff;
    }

    /* FEATURE GRID */
    .feature-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 16px;
    }

    .feature-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 20px;
      display: flex;
      align-items: flex-start;
      gap: 14px;
      transition: border-color 0.2s, transform 0.2s;
    }
    .feature-card:hover {
      border-color: rgba(0,212,255,0.3);
      transform: translateY(-2px);
    }
    .feature-card .fc-icon { font-size: 22px; margin-top: 2px; }
    .feature-card h3 { font-size: 0.9rem; font-weight: 700; color: #fff; margin-bottom: 4px; }
    .feature-card p { font-size: 0.8rem; color: var(--muted); line-height: 1.5; }

    /* CODE BLOCK */
    .code-block {
      background: var(--code-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
      margin: 12px 0;
    }

    .code-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 16px;
      background: rgba(255,255,255,0.02);
      border-bottom: 1px solid var(--border);
    }

    .code-dots { display: flex; gap: 6px; }
    .code-dots span {
      width: 10px; height: 10px; border-radius: 50%;
    }
    .dot-red    { background: #ff5f57; }
    .dot-yellow { background: #febc2e; }
    .dot-green  { background: #28c840; }

    .code-lang {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--muted);
    }

    .code-block pre {
      padding: 16px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 13px;
      line-height: 1.7;
      color: #94a3b8;
      overflow-x: auto;
      white-space: pre;
    }

    .code-block pre .cmd  { color: var(--accent); }
    .code-block pre .comment { color: #334155; }
    .code-block pre .key  { color: #a78bfa; }
    .code-block pre .val  { color: var(--accent3); }
    .code-block pre .dir  { color: var(--accent4); }
    .code-block pre .tree { color: #334155; }

    /* STEPS */
    .steps { display: flex; flex-direction: column; gap: 0; }

    .step {
      display: flex;
      gap: 20px;
      position: relative;
      padding-bottom: 32px;
    }
    .step:last-child { padding-bottom: 0; }

    .step-left {
      display: flex;
      flex-direction: column;
      align-items: center;
      flex-shrink: 0;
    }

    .step-num {
      width: 36px; height: 36px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--accent2), var(--accent));
      display: flex; align-items: center; justify-content: center;
      font-weight: 800;
      font-size: 14px;
      color: #fff;
      flex-shrink: 0;
    }

    .step-line {
      width: 2px;
      flex: 1;
      background: linear-gradient(to bottom, var(--border), transparent);
      margin-top: 8px;
    }

    .step-content { padding-top: 6px; }
    .step-content h3 { font-size: 1rem; font-weight: 700; color: #fff; margin-bottom: 4px; }
    .step-content p  { font-size: 0.85rem; color: var(--muted); margin-bottom: 10px; line-height: 1.6; }

    /* WORKFLOW */
    .workflow-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0;
      position: relative;
    }

    .workflow-grid::before {
      content: '';
      position: absolute;
      top: 36px;
      left: calc(100% / 6);
      right: calc(100% / 6);
      height: 2px;
      background: linear-gradient(90deg, var(--accent), var(--accent2), var(--accent3));
    }

    .wf-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 24px 20px;
      text-align: center;
      position: relative;
      transition: border-color 0.2s, transform 0.2s;
    }
    .wf-card:hover { border-color: rgba(0,212,255,0.3); transform: translateY(-3px); }
    .wf-card:nth-child(2) { border-color: rgba(124,58,237,0.3); }
    .wf-card:nth-child(3) { border-color: rgba(16,185,129,0.3); }

    .wf-card .wf-icon {
      width: 56px; height: 56px;
      border-radius: 16px;
      display: flex; align-items: center; justify-content: center;
      font-size: 26px;
      margin: 0 auto 14px;
    }

    .wf-card h3 { font-size: 0.9rem; font-weight: 700; color: #fff; margin-bottom: 6px; }
    .wf-card p  { font-size: 0.78rem; color: var(--muted); line-height: 1.5; }
    .wf-card code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--accent);
      background: rgba(0,212,255,0.06);
      padding: 2px 8px;
      border-radius: 4px;
      display: inline-block;
      margin-top: 8px;
    }

    /* TECH STACK */
    .tech-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
    }

    .tech-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px 18px;
      display: flex;
      align-items: center;
      gap: 14px;
      transition: border-color 0.2s;
    }
    .tech-card:hover { border-color: rgba(0,212,255,0.2); }
    .tech-card .tech-icon { font-size: 26px; }
    .tech-card h4 { font-size: 0.9rem; font-weight: 700; color: #fff; }
    .tech-card p  { font-size: 0.75rem; color: var(--muted); }

    /* USE CASE */
    .usecase-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
    }
    .usecase-item {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px 18px;
      display: flex;
      align-items: center;
      gap: 12px;
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text);
      transition: border-color 0.2s, transform 0.2s;
    }
    .usecase-item:hover { border-color: rgba(0,212,255,0.2); transform: translateX(3px); }
    .usecase-item span:first-child { font-size: 22px; }

    /* FUTURE */
    .future-list { display: flex; flex-direction: column; gap: 10px; }
    .future-item {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 14px 18px;
      display: flex;
      align-items: center;
      gap: 14px;
      transition: border-color 0.2s;
    }
    .future-item:hover { border-color: rgba(124,58,237,0.3); }
    .future-item .fi-icon { font-size: 20px; flex-shrink: 0; }
    .future-item span:last-child { font-size: 0.88rem; color: var(--text); }
    .todo-dot {
      width: 16px; height: 16px; border-radius: 4px;
      border: 2px solid var(--border);
      flex-shrink: 0;
      margin-left: auto;
    }

    /* SECURITY */
    .security-box {
      background: rgba(239,68,68,0.05);
      border: 1px solid rgba(239,68,68,0.2);
      border-radius: 14px;
      padding: 24px;
    }
    .sec-item {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 10px 0;
      border-bottom: 1px solid rgba(239,68,68,0.08);
      font-size: 0.88rem;
    }
    .sec-item:last-child { border-bottom: none; padding-bottom: 0; }
    .sec-item .sec-icon { font-size: 18px; flex-shrink: 0; margin-top: 1px; }
    .sec-item p { color: var(--text); line-height: 1.5; }
    .sec-item p code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 12px;
      color: #f87171;
      background: rgba(239,68,68,0.1);
      padding: 1px 6px;
      border-radius: 4px;
    }

    /* OUTPUT */
    .output-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
    }
    .output-card {
      background: var(--card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px 16px;
      text-align: center;
      transition: border-color 0.2s, transform 0.2s;
    }
    .output-card:hover { transform: translateY(-3px); }
    .output-card:nth-child(1):hover { border-color: rgba(245,158,11,0.4); }
    .output-card:nth-child(2):hover { border-color: rgba(16,185,129,0.4); }
    .output-card:nth-child(3):hover { border-color: rgba(124,58,237,0.4); }
    .output-card .oc-icon { font-size: 30px; margin-bottom: 10px; }
    .output-card h4 { font-size: 0.85rem; font-weight: 700; color: #fff; margin-bottom: 6px; }
    .output-card code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      color: var(--muted);
    }

    /* AUTHOR */
    .author-card {
      background: linear-gradient(135deg, rgba(0,212,255,0.05), rgba(124,58,237,0.05));
      border: 1px solid rgba(0,212,255,0.2);
      border-radius: 16px;
      padding: 32px;
      text-align: center;
      position: relative;
      overflow: hidden;
    }
    .author-card::before {
      content: '';
      position: absolute;
      top: -40px; left: 50%;
      transform: translateX(-50%);
      width: 150px; height: 150px;
      background: radial-gradient(circle, rgba(0,212,255,0.1), transparent 70%);
      pointer-events: none;
    }
    .author-avatar {
      width: 72px; height: 72px;
      border-radius: 50%;
      background: linear-gradient(135deg, var(--accent2), var(--accent));
      display: flex; align-items: center; justify-content: center;
      font-size: 32px;
      margin: 0 auto 16px;
      border: 3px solid rgba(0,212,255,0.3);
    }
    .author-card h3 {
      font-size: 1.4rem;
      font-weight: 800;
      background: linear-gradient(135deg, #fff, var(--accent));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: 6px;
    }
    .author-card p {
      color: var(--muted);
      font-size: 0.88rem;
    }

    /* ANIMATIONS */
    @keyframes fadeDown {
      from { opacity: 0; transform: translateY(-16px); }
      to   { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 600px) {
      .workflow-grid { grid-template-columns: 1fr; }
      .workflow-grid::before { display: none; }
      .tech-grid { grid-template-columns: 1fr; }
      .usecase-grid { grid-template-columns: 1fr; }
      .output-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
<div class="container">

  <!-- HERO -->
  <div class="hero">
    <div class="hero-badge">🛰️ Network Intelligence Tool</div>
    <h1>MikroTik Auto Analysis</h1>
    <p>Sistem otomatis untuk mengambil, membersihkan, dan menganalisis data traffic dari perangkat MikroTik RouterOS dengan pendekatan modular.</p>
    <div class="badges">
      <span class="badge badge-blue">🐍 Python 3.x</span>
      <span class="badge badge-purple">🐼 Pandas</span>
      <span class="badge badge-green">🌐 RouterOS API</span>
      <span class="badge badge-amber">📄 CSV Processing</span>
    </div>
  </div>

  <div class="divider"></div>

  <!-- FEATURES -->
  <div class="section-title">
    <div class="icon icon-blue">🚀</div>
    <h2>Features</h2>
  </div>
  <div class="feature-grid">
    <div class="feature-card">
      <div class="fc-icon">📡</div>
      <div>
        <h3>Auto Fetch Traffic</h3>
        <p>Ambil data traffic langsung dari MikroTik RouterOS secara otomatis.</p>
      </div>
    </div>
    <div class="feature-card">
      <div class="fc-icon">🧹</div>
      <div>
        <h3>Data Cleaning</h3>
        <p>Preprocessing & cleaning otomatis untuk data yang siap dianalisis.</p>
      </div>
    </div>
    <div class="feature-card">
      <div class="fc-icon">📊</div>
      <div>
        <h3>Generate Report</h3>
        <p>Laporan analisis traffic yang informatif dan terstruktur.</p>
      </div>
    </div>
    <div class="feature-card">
      <div class="fc-icon">🧩</div>
      <div>
        <h3>Modular & Scalable</h3>
        <p>Struktur project yang mudah dikembangkan dan di-maintain.</p>
      </div>
    </div>
    <div class="feature-card">
      <div class="fc-icon">🔑</div>
      <div>
        <h3>Env-Based Config</h3>
        <p>Konfigurasi aman berbasis file <code style="font-family:monospace;font-size:11px;color:var(--accent);background:rgba(0,212,255,0.08);padding:1px 5px;border-radius:3px">.env</code> tanpa hardcode credential.</p>
      </div>
    </div>
  </div>

  <div class="divider"></div>

  <!-- PROJECT STRUCTURE -->
  <div class="section-title">
    <div class="icon icon-amber">📂</div>
    <h2>Project Structure</h2>
  </div>
  <div class="code-block">
    <div class="code-header">
      <div class="code-dots">
        <span class="dot-red"></span>
        <span class="dot-yellow"></span>
        <span class="dot-green"></span>
      </div>
      <span class="code-lang">📁 Directory Tree</span>
    </div>
    <pre><span class="dir">MIKROTIK_AUTO_ANALYSIS/</span>
<span class="tree">│</span>
<span class="tree">├──</span> <span class="dir">.venv/</span>                  <span class="comment"># 🐍 Virtual environment</span>
<span class="tree">├──</span> <span class="dir">analyst_data_clean/</span>     <span class="comment"># 🧹 Data hasil cleaning</span>
<span class="tree">├──</span> <span class="dir">analyst_data_raw/</span>       <span class="comment"># 📥 Data mentah dari MikroTik</span>
<span class="tree">│   └──</span> <span class="val">traffic_raw_YYYYMMDD.csv</span>
<span class="tree">│</span>
<span class="tree">├──</span> <span class="dir">analyst_report/</span>         <span class="comment"># 📋 Hasil report analisis</span>
<span class="tree">│</span>
<span class="tree">├──</span> <span class="dir">script/</span>
<span class="tree">│   ├──</span> <span class="key">get_data_mikrotik.py</span>      <span class="comment"># 🔌 Fetch data</span>
<span class="tree">│   ├──</span> <span class="key">process_traffic_mikrotik.py</span> <span class="comment"># ⚙️  Processing</span>
<span class="tree">│   └──</span> <span class="key">report_traffic_mikrotik.py</span>  <span class="comment"># 📝 Reporting</span>
<span class="tree">│</span>
<span class="tree">├──</span> <span class="key">.env</span>                    <span class="comment"># 🔑 Credential (tidak di-push)</span>
<span class="tree">├──</span> <span class="key">.env.example</span>            <span class="comment"># 📄 Template environment</span>
<span class="tree">├──</span> <span class="key">.gitignore</span>
<span class="tree">└──</span> <span class="cmd">main.py</span>                 <span class="comment"># 🏁 Entry point</span></pre>
  </div>

  <div class="divider"></div>

  <!-- INSTALLATION -->
  <div class="section-title">
    <div class="icon icon-green">⚙️</div>
    <h2>Installation</h2>
  </div>
  <div class="steps">
    <div class="step">
      <div class="step-left">
        <div class="step-num">1</div>
        <div class="step-line"></div>
      </div>
      <div class="step-content">
        <h3>Clone Repository</h3>
        <p>Download project ke lokal kamu.</p>
        <div class="code-block">
          <div class="code-header">
            <div class="code-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
            <span class="code-lang">bash</span>
          </div>
          <pre><span class="cmd">git clone</span> https://github.com/username/mikrotik-auto-analysis.git
<span class="cmd">cd</span> mikrotik-auto-analysis</pre>
        </div>
      </div>
    </div>

    <div class="step">
      <div class="step-left">
        <div class="step-num">2</div>
        <div class="step-line"></div>
      </div>
      <div class="step-content">
        <h3>Create Virtual Environment</h3>
        <p>Buat dan aktifkan virtual environment Python.</p>
        <div class="code-block">
          <div class="code-header">
            <div class="code-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
            <span class="code-lang">bash</span>
          </div>
          <pre><span class="cmd">python</span> -m venv .venv

<span class="comment"># 🪟 Windows</span>
.venv\Scripts\activate

<span class="comment"># 🍎 Mac / Linux</span>
<span class="cmd">source</span> .venv/bin/activate</pre>
        </div>
      </div>
    </div>

    <div class="step">
      <div class="step-left">
        <div class="step-num">3</div>
        <div class="step-line"></div>
      </div>
      <div class="step-content">
        <h3>Install Dependencies</h3>
        <p>Install semua library yang dibutuhkan.</p>
        <div class="code-block">
          <div class="code-header">
            <div class="code-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
            <span class="code-lang">bash</span>
          </div>
          <pre><span class="cmd">pip install</span> -r requirements.txt</pre>
        </div>
      </div>
    </div>

    <div class="step">
      <div class="step-left">
        <div class="step-num">4</div>
      </div>
      <div class="step-content">
        <h3>Setup Environment</h3>
        <p>Copy template dan isi credential MikroTik kamu.</p>
        <div class="code-block">
          <div class="code-header">
            <div class="code-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
            <span class="code-lang">bash</span>
          </div>
          <pre><span class="cmd">cp</span> .env.example .env</pre>
        </div>
        <div class="code-block">
          <div class="code-header">
            <div class="code-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
            <span class="code-lang">.env</span>
          </div>
          <pre><span class="key">MIKROTIK_HOST</span>=<span class="val">192.168.x.x</span>
<span class="key">MIKROTIK_USER</span>=<span class="val">admin</span>
<span class="key">MIKROTIK_PASSWORD</span>=<span class="val">yourpassword</span></pre>
        </div>
      </div>
    </div>
  </div>

  <div class="divider"></div>

  <!-- USAGE -->
  <div class="section-title">
    <div class="icon icon-blue">▶️</div>
    <h2>Usage</h2>
  </div>
  <div class="code-block">
    <div class="code-header">
      <div class="code-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
      <span class="code-lang">bash — Full Pipeline</span>
    </div>
    <pre><span class="cmd">python</span> main.py</pre>
  </div>
  <div class="code-block">
    <div class="code-header">
      <div class="code-dots"><span class="dot-red"></span><span class="dot-yellow"></span><span class="dot-green"></span></div>
      <span class="code-lang">bash — Per Modul</span>
    </div>
    <pre><span class="cmd">python</span> script/get_data_mikrotik.py
<span class="cmd">python</span> script/process_traffic_mikrotik.py
<span class="cmd">python</span> script/report_traffic_mikrotik.py</pre>
  </div>

  <div class="divider"></div>

  <!-- WORKFLOW -->
  <div class="section-title">
    <div class="icon icon-purple">🔄</div>
    <h2>Workflow</h2>
  </div>
  <div class="workflow-grid">
    <div class="wf-card">
      <div class="wf-icon icon-blue">📡</div>
      <h3>Data Collection</h3>
      <p>Mengambil data traffic langsung dari router MikroTik</p>
      <code>get_data_mikrotik.py</code>
    </div>
    <div class="wf-card">
      <div class="wf-icon icon-amber">🔧</div>
      <h3>Data Processing</h3>
      <p>Cleaning, transform, dan agregasi data traffic</p>
      <code>process_traffic_mikrotik.py</code>
    </div>
    <div class="wf-card">
      <div class="wf-icon icon-green">📊</div>
      <h3>Reporting</h3>
      <p>Generate laporan analisis traffic yang terstruktur</p>
      <code>report_traffic_mikrotik.py</code>
    </div>
  </div>

  <div class="divider"></div>

  <!-- OUTPUT -->
  <div class="section-title">
    <div class="icon icon-amber">📈</div>
    <h2>Output Directory</h2>
  </div>
  <div class="output-grid">
    <div class="output-card">
      <div class="oc-icon">📥</div>
      <h4>Raw Data</h4>
      <code>analyst_data_raw/</code>
    </div>
    <div class="output-card">
      <div class="oc-icon">🧹</div>
      <h4>Clean Data</h4>
      <code>analyst_data_clean/</code>
    </div>
    <div class="output-card">
      <div class="oc-icon">📋</div>
      <h4>Report</h4>
      <code>analyst_report/</code>
    </div>
  </div>

  <div class="divider"></div>

  <!-- SECURITY -->
  <div class="section-title">
    <div class="icon icon-red">🔐</div>
    <h2>Security Notes</h2>
  </div>
  <div class="security-box">
    <div class="sec-item">
      <div class="sec-icon">🔑</div>
      <p>Gunakan <code>.env</code> untuk menyimpan semua credential — jangan hardcode di dalam script.</p>
    </div>
    <div class="sec-item">
      <div class="sec-icon">🚫</div>
      <p>Jangan pernah expose username & password router ke publik atau push ke repository.</p>
    </div>
    <div class="sec-item">
      <div class="sec-icon">👁️</div>
      <p>Pastikan <code>.env</code> sudah terdaftar di <code>.gitignore</code> sebelum commit.</p>
    </div>
  </div>

  <div class="divider"></div>

  <!-- TECH STACK -->
  <div class="section-title">
    <div class="icon icon-blue">🧠</div>
    <h2>Tech Stack</h2>
  </div>
  <div class="tech-grid">
    <div class="tech-card">
      <div class="tech-icon">🐍</div>
      <div>
        <h4>Python 3.x</h4>
        <p>Core language untuk semua script</p>
      </div>
    </div>
    <div class="tech-card">
      <div class="tech-icon">🐼</div>
      <div>
        <h4>Pandas</h4>
        <p>Data manipulation & analysis</p>
      </div>
    </div>
    <div class="tech-card">
      <div class="tech-icon">🌐</div>
      <div>
        <h4>MikroTik RouterOS API</h4>
        <p>Interface ke perangkat router</p>
      </div>
    </div>
    <div class="tech-card">
      <div class="tech-icon">📄</div>
      <div>
        <h4>CSV Processing</h4>
        <p>Format data input & output</p>
      </div>
    </div>
  </div>

  <div class="divider"></div>

  <!-- USE CASE -->
  <div class="section-title">
    <div class="icon icon-green">📌</div>
    <h2>Use Case</h2>
  </div>
  <div class="usecase-grid">
    <div class="usecase-item"><span>🖥️</span><span>Monitoring traffic kantor</span></div>
    <div class="usecase-item"><span>📶</span><span>Analisa penggunaan bandwidth</span></div>
    <div class="usecase-item"><span>🔍</span><span>Audit jaringan internal</span></div>
    <div class="usecase-item"><span>🤖</span><span>Automation reporting harian</span></div>
  </div>

  <div class="divider"></div>

  <!-- FUTURE IMPROVEMENTS -->
  <div class="section-title">
    <div class="icon icon-purple">🏗️</div>
    <h2>Future Improvements</h2>
  </div>
  <div class="future-list">
    <div class="future-item">
      <div class="fi-icon">⏰</div>
      <span>Scheduler otomatis (cron / task scheduler)</span>
      <div class="todo-dot"></div>
    </div>
    <div class="future-item">
      <div class="fi-icon">🗄️</div>
      <span>Database integration (PostgreSQL / MySQL)</span>
      <div class="todo-dot"></div>
    </div>
    <div class="future-item">
      <div class="fi-icon">🌐</div>
      <span>Web dashboard (Flask / FastAPI)</span>
      <div class="todo-dot"></div>
    </div>
    <div class="future-item">
      <div class="fi-icon">📉</div>
      <span>Visualisasi chart interaktif</span>
      <div class="todo-dot"></div>
    </div>
    <div class="future-item">
      <div class="fi-icon">🐳</div>
      <span>Deployment ke server / container (Docker)</span>
      <div class="todo-dot"></div>
    </div>
  </div>

  <div class="divider"></div>

  <!-- AUTHOR -->
  <div class="author-card">
    <div class="author-avatar">👤</div>
    <h3>BronyaVollerei</h3>
    <p>🛠️ Developed for network traffic automation and data analysis workflow</p>
  </div>

</div>
</body>
</html>