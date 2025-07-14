import requests
from termcolor import cprint
from urllib.parse import urlparse

def cek_proteksi(target_url):
    try:
        # Normalisasi URL
        if not target_url.startswith("http"):
            target_url = "http://" + target_url

        parsed_url = urlparse(target_url)
        host = parsed_url.netloc

        # Kirim permintaan HEAD
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        r = requests.get(target_url, headers=headers, timeout=10)

        proteksi_ditemukan = False

        # Deteksi dari header server
        server_header = r.headers.get('Server', '').lower()
        if 'cloudflare' in server_header or 'ddos' in server_header:
            proteksi_ditemukan = True

        # Deteksi kode status mencurigakan
        if r.status_code in [403, 429, 503]:
            proteksi_ditemukan = True

        # Deteksi jika ada JS challenge dari Cloudflare
        if 'cf-ray' in r.headers or 'cf-cache-status' in r.headers:
            proteksi_ditemukan = True

        if proteksi_ditemukan:
            cprint(f"[×] {host} dilindungi! (Punya proteksi anti-DDoS)", "red")
        else:
            cprint(f"[✓] {host} tidak memiliki proteksi! Rentan DDoS", "green")

    except requests.exceptions.RequestException as e:
        cprint(f"[!] Error: {e}", "red")

if __name__ == "__main__":
    print("=== CEK PROTEKSI ANTI DDOS ===")
    target = input("Masukkan URL target (https://...): ")
    cek_proteksi(target)