# 🔍 Port Scanner

**Day 3 of daily tools — 2026-06-08**

---

## English

A fast, multi-threaded port scanner that checks which ports are open on a given host or IP address.

### Features
- Scan common ports, 1–1024, or full range (1–65535)
- Multi-threaded (100 concurrent connections)
- Shows service name for each open port
- Save results to `.txt` file
- Standalone `.exe` — no install needed

### Usage

**With exe:**
PortScanner.exe

With Python:

pip install -r requirements.txt

python port_scanner.py

Example Output
🔍 Scanning github.com (140.82.121.4)

Ports: common ports

────────────────────────────

[OPEN] 22 SSH

[OPEN] 80 HTTP

[OPEN] 443 HTTPS

────────────────────────────

3 open port(s) found.

فارسی
یک port scanner سریع و چند‌نخی که بررسی می‌کند کدام پورت‌های یک سرور یا IP باز هستند.

قابلیت‌ها
اسکن پورت‌های معروف، ۱ تا ۱۰۲۴، یا همه پورت‌ها (۱ تا ۶۵۵۳۵)
چند‌نخی (۱۰۰ اتصال همزمان)
نمایش نام سرویس برای هر پورت باز
ذخیره نتایج در فایل .txt
فایل .exe مستقل — نیازی به نصب ندارد
نحوه استفاده
با exe:

PortScanner.exe

با Python:

pip install requests

python port_scanner.py

No external libraries required — uses Python standard library only.
