🧰 Proxy Whitelister – Validate & Filter Working Proxies
Description:

The Proxy Whitelister is a Python-based tool designed to validate and filter live proxies from a given list. It checks each proxy for availability and functionality using real HTTP requests, and saves only the working (whitelisted) proxies to an output file. Ideal for penetration testers, scrapers, and security researchers who require fresh and functional proxy lists.

🔍 Features:
✅ Validates HTTP/HTTPS proxies
⚡ Multithreaded testing for high speed
📂 Input: Custom proxy list (proxy.txt)
💾 Output: Filtered working proxies (saveoutput.txt)
⌛ Timeout-controlled requests for accurate results
🧠 Easy to extend (SOCKS5, auth proxies, proxy chaining, etc.)

📦 Installation
bash
git clone https://github.com/REDPYTHON804/proxy-filter.git
cd proxy-filter
pip install -r requirements.txt

🚀 Usage
bash
python3 validate-proxies.py --input path/proxy.txt --output saveoutput.txt

📌 Example Proxy Format
makefile
185.192.70.243:3128
103.1.92.69:3128
