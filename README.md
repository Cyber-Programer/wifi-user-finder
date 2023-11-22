# Wifi User Finder

This is a basic program made for finding all users who are connected to your network.

## Why use this tool?
- You can use this tool to monitor WiFi users.
- If you don't have admin rights on the WiFi, you can still use this tool to monitor users by simply connecting to the target WiFi.
- You can use this tool just for fun.
- This is an animated tool, so you're sure to enjoy it.

## How does this tool work?
- First, this tool collects your local IP.
- Then, it runs an IP range using the local IP.
- Next, it finds all active users using the IP.
- Finally, it displays the results as output.

## Which operating systems (OS) can run it?
- Termux
- Linux
- Ubuntu

You can try any other OS.

## How to install?
- To install this tool, you need some packages/tools:
  - First, you need Python.
  - Second, you need nmap.

### Termux Installation
```bash
apt-get update && apt-get upgrade
pkg update && pkg upgrade
pkg install git
pkg install python
pkg install nmap
git clone https://github.com/Cyber-Programer/wifi-user-finder.git
cd wifi-user-finder
python wifi.py
```
### Linux or Ubuntu
- installation

```bash
    sudo apt-get update && apt-get upgrade
    sudo apt-get install git
    sudo apt-get install python
    sudo apt-get install nma
```
```bash
    git clone https://github.com/Cyber-Programer/wifi-user-finder.git
    cd wifi-user-finder
    python wifi.py
```

## Tool 
```bash
               _  __ _
          (_)/ _(_)
 __      ___| |_ _
 \ \ /\ / / |  _| |
  \ V  V /| | | | |
   \_/\_/ |_|_| |_|

    Wifi connected user finder
                    (2rootv3)
                    
[+] requirement(1) OK
Your Local IP address: 192.168.12.109
----------------------------------------
[+] Total Ip Found: 7
[+] Wi-Fi Ip: 192.168.12.1
[+] Total user: 6

[+] Wi-Fi IP range:
--------------------
192.168.12.1
192.168.12.101
192.168.12.102
192.168.12.104
192.168.12.105
192.168.12.107
192.168.12.109
```
