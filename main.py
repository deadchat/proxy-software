import os
import ctypes
import requests
import pyfiglet
import threading
from colorama import Fore
from pystyle import Colorate, Colors, Center, Box

def cls():
    os.system("cls" if os.name == "nt" else "clear")

class logger:
    def info(message):
        print(f"[ {Fore.CYAN}INFO{Fore.RESET} ] {message}")
    def success(message):
        print(f"[ {Fore.LIGHTGREEN_EX}SUCCESS{Fore.RESET} ] {message}")
    def warning(message):
        print(f"[ {Fore.YELLOW}WARNING{Fore.RESET} ] {message}")
    def error(message):
        print(f"[  {Fore.LIGHTRED_EX}ERROR{Fore.RESET}  ] {message}")
    

class _modules:
    def scrape():
        http = [
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
        ]
        socks4 = [
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt"
        ]
        socks5 = [
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        ]
        cls()
        type = input("TYPE [http, socks4, socks5] $> ")
        if type == "http": pass
        elif type == "socks4": pass
        elif type == "socks5": pass
        else: _modules.scrape()

        ping = input("PING [in s] $> ")
        try: ping = float(ping)
        except: logger.error("The Ping is not a Float."); _modules.scrape()

        output = input("OUTPUT FILE $> ")

        file = open(f"output/{output}.txt", "w")

        with requests.Session() as session:
            if type == "http": type = http
            elif type == "socks4": type = socks4
            elif type == "socks5": type = socks5
            
            for list in type:
                proxies = session.get(list).text
                for proxy in proxies.split("\n"):
                    try:
                        session.get(f"http://{proxy}", timeout=(ping)).text
                    except Exception as e:
                        # print(e)
                        logger.error(proxy); continue
                    else:
                        file.write(f"{proxy}\n")
                        logger.success(proxy)
            file.close()

    def multithread(function):
        for i in range(5):
            threading.Thread(target=function).start()

class _base:
    def main():
        cls(); ctypes.windll.kernel32.SetConsoleTitleW("Proxy Software")
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(pyfiglet.figlet_format("ProxyScraper"))))
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter("Made by tear#3925")))
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(Box.DoubleCube("[1] Scrape Proxies \n[2] Exit"))))
        choice = input(Colorate.Horizontal(Colors.blue_to_purple, "$> "))
        if choice == "1": _modules.multithread(_modules.scrape())
        elif choice == "2": os._exit(0)
        else: _base.main()

if __name__ == "__main__":
    _base.main()