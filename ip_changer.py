import requests
import time
import os
import random



TOR_PROXY = {   #replaceable
    'http': 'socks5h://127.0.0.1:9050', 
    'https': 'socks5h://127.0.0.1:9050'
}

MESSAGES = {
    'en': {
        'welcome': "=== Automatically IP Changer ===",
        'interval_prompt': "Enter time interval in seconds (e.g. 30): ",
        'count_prompt': "Enter how many times to change IP (0 = infinite): ",
        'invalid_number': "Invalid number entered.",
        'infinite_mode': "Starting infinite mode. Press Ctrl+C to stop.",
        'changing_ip': "[+] Reloading Tor service...",
        'ip_output': "New IP address: ",
        'error': "Failed to get IP: "
    },
    'tr': {
        'welcome': "=== Tor IP Değiştirici ===",
        'interval_prompt': "Kaç saniyede bir IP değiştirilsin? (örnek: 30): ",
        'count_prompt': "Kaç kez IP değiştirilsin? (0 = sonsuz): ",
        'invalid_number': "Geçersiz sayı girdiniz.",
        'infinite_mode': "Sonsuz döngü başlatıldı. Durdurmak için Ctrl+C.",
        'changing_ip': "[+] Tor servisi yeniden yükleniyor...",
        'ip_output': "Yeni IP adresi: ",
        'error': "IP alınamadı: "
    }
}

def colorize(text, color_code):
    return f"{color_code}{text}\033[0m"


def get_ip(lang):
    try:
        response = requests.get("https://checkip.amazonaws.com", proxies=TOR_PROXY, timeout=10)
        return response.text.strip()
    except Exception as e:
        return f"{MESSAGES[lang]['error']} {e}"


def change_tor_ip(lang):
    print(MESSAGES[lang]['changing_ip'])
    os.system("sudo systemctl reload tor")  
    time.sleep(5)  


def print_ascii_art():
    os.system("clear")
    ascii_art = """ 
    
       _  _  _         _              _                _
      | || |(_)       | |            (_)              | |
  ___ | || | _   ___  | |_   ______   _  _ __     ___ | |__    __ _  _ __    __ _   ___  _ __
 / _ \| || || | / _ \ | __| |______| | || '_ \   / __|| '_ \  / _` || '_ \  / _` | / _ \| '__|
|  __/| || || || (_) || |_           | || |_) | | (__ | | | || (_| || | | || (_| ||  __/| |
 \___||_||_||_| \___/  \__|          |_|| .__/   \___||_| |_| \__,_||_| |_| \__, | \___||_|
                                        | |                                  __/ |
                                        |_|                                 |___/

    """
    print(ascii_art)

def main():
    print_ascii_art()

    

    lang = input("Choose language (en/tr):").lower()
    if lang not in MESSAGES:
        print("Unsupported language. Default: en")
        lang = 'en'

    print(MESSAGES[lang]['welcome'])

    try:
        interval = int(input(MESSAGES[lang]['interval_prompt']))
        count = int(input(MESSAGES[lang]['count_prompt']))
    except ValueError:
        print(MESSAGES[lang]['invalid_number'])
        return  

    if count == 0:
        print(MESSAGES[lang]['infinite_mode'])  #forever
        while True:
            change_tor_ip(lang)
            print(MESSAGES[lang]['ip_output'], get_ip(lang))  #visible output
            time.sleep(random.randint(interval - 5, interval + 5))  
    else:
        for i in range(count):
            change_tor_ip(lang)
            new_ip = get_ip(lang)
            print(f"[{i+1}/{count}] {MESSAGES[lang]['ip_output']}{colorize(new_ip, '\033[92m')}")
            time.sleep(interval)

if __name__ == "__main__":
    main()  
