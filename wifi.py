import socket
import subprocess
import re
import sys
import time

from time import sleep as s


class colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    BLUE = '\033[94m000'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    
class design:
    under= '-'*40
    x = '--------------------'
def logos(text,color=colors.RESET):
    for i in text:
        sys.stdout.write(color + i + colors.RESET)
        sys.stdout.flush()
        time.sleep(0.008)

logo = f'''
           _  __ _
          (_)/ _(_)
 __      ___| |_ _
 \ \ /\ / / |  _| |
  \ V  V /| | | | |
   \_/\_/ |_|_| |_|

    Wifi connected user finder
                    (2rootv3)
                    
'''
def animation(text,color=colors.RESET):
    for i in text:
        sys.stdout.write(color + i + colors.RESET)
        sys.stdout.flush()
        s(0.05)
    sys.stdout.write('\n')

def check_nmap_installation():
    try:
        # Try to run nmap to check if it's installed
        subprocess.run(['nmap', '-V'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        animation('[+] requirement(1) OK',colors.GREEN)

    except FileNotFoundError:
        animation("[-] nmap is not installed. Installing...",colors.RED)

        try:
            # Try to install nmap using apt (for Debian-based systems)
            subprocess.run(['apt', 'update'], check=True)
            subprocess.run(['apt', 'install', 'nmap'], check=True)
            animation("[-] nmap installed successfully.",colors.GREEN)

        except subprocess.CalledProcessError as e:
            animation(f"[-] Error installing nmap: {e}",colors.RED)
            exit(1)  # Exit with an error code


def get_local_ip():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
        return local_ip
    except socket.error as e:
        animation(f"[-] Socket error:{e}",colors.RED)
        return None

def scan_wifi_ip_range(local_ip):
    ip_range = '.'.join(local_ip.split('.')[:-1]) + '.0/24'
    try:
        output = subprocess.check_output(['nmap', '-sn', ip_range], universal_newlines=True)
        ip_list = re.findall(r"Nmap scan report for (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", output)
        return ip_list
    except subprocess.CalledProcessError as e:
        animation(f"[-] Error executing nmap command:{e}",colors.RED)
        return []

if __name__ == "__main__":
    logos(logo,colors.YELLOW)
    check_nmap_installation()
    local_ip_address = get_local_ip()
    if local_ip_address:
        animation(f'Your Local IP address: {local_ip_address}',colors.YELLOW)
        animation(design.under,colors.YELLOW)
        
        wifi_ip_range = scan_wifi_ip_range(local_ip_address)
        if wifi_ip_range: 
            total_user = len(wifi_ip_range)
            animation(f'[+] Total Ip Found: {total_user}',colors.CYAN)
            for wifi in wifi_ip_range:
                animation(f'[+] Wi-Fi Ip: {wifi}',colors.CYAN)
                break
            animation(f'[+] Total user: {total_user-1}',colors.CYAN)
            animation("\n[+] Wi-Fi IP range:",colors.MAGENTA)
            animation(design.x,colors.MAGENTA)
            for ip in wifi_ip_range:
                animation(ip,colors.GREEN)
        else:
            animation("[-] Failed to retrieve the Wi-Fi IP range.",colors.RED)
    else:
        animation("[-] Failed to retrieve the local IP address.",colors.RED)
