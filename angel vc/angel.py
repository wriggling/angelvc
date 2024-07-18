import os
import sys
import json
import requests
import websocket
import colorama
from colorama import Fore
import pystyle
from pystyle import Colors, Write, Box, Colorate, Center
import time
from time import sleep
os.system("title " + "ANGEL VC - @cxcvc on discord")
purple = Colors.red_to_purple
greentheme = Colors.green_to_yellow

t = time.localtime()
t1 = time.strftime("%H:%M:%S", t)

SELF_MUTE = True
SELF_DEAF = True

def clear(): return os.system('cls') if os.name == 'nt' else os.system('clear')


clear()
GUILD_ID = input('Type Server ID here: ')
CHANNEL_ID = input('Type Channel ID here: ')
status = input('Want to appear on online, dnd, or idle: ')
usertoken = input('Welcome! Enter your Token Here: ')
if not usertoken:
  print("[ERROR] Please add a token inside Secrets.")

  clear()
  sys.exit()

clear()
headers = {"Authorization": usertoken, "Content-Type": "application/json"}

validate = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers)
if validate.status_code != 200:
  print("[ERROR] Your token might be invalid. Please check it again.")
  sys.exit()

userinfo = requests.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers).json()
username = userinfo["username"]
discriminator = userinfo["discriminator"]
userid = userinfo["id"]

def joiner(token, status):
    ws = websocket.WebSocket()
    ws.connect('wss://gateway.discord.gg/?v=9&encoding=json')
    start = json.loads(ws.recv())
    heartbeat = start['d']['heartbeat_interval']
    auth = {"op": 2,"d": {"token": token,"properties": {"$os": "Windows 10","$browser": "Google Chrome","$device": "Windows"},"presence": {"status": status,"afk": False}},"s": None,"t": None}
    vc = {"op": 4,"d": {"guild_id": GUILD_ID,"channel_id": CHANNEL_ID,"self_mute": SELF_MUTE,"self_deaf": SELF_DEAF}}
    ws.send(json.dumps(auth))
    ws.send(json.dumps(vc))
    time.sleep(heartbeat / 1000)
    ws.send(json.dumps({"op": 1,"d": None}))

def run_joiner():
  clear()
print(Colorate.Vertical(Colors.green_to_red, f"""

  ░░░░░░                                                                                              ▒▒  
      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░    ░░                                                      ░░    ░░▒▒▒▒▒▒▓▓▒▒▒▒    
  ▓▓▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░                  ANGEL                   ▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓
      ░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒               VC               ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░    
    ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒░░         SELFBOT          ░░▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓                   █████╗ ███╗   ██╗ ██████╗ ███████╗██╗
    ░░▒▒▓▓▓▓▓▓▓▓██▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒         BY           ▒▒▒▒▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░                  ██╔══██╗████╗  ██║██╔════╝ ██╔════╝██║
    ░░▓▓▓▓▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓██▒▒▓▓██▒▒▒▒▓▓▒▒▒▒      CHEX        ░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▒▒▓▓▓▓                    ███████║██╔██╗ ██║██║  ███╗█████╗  ██║ 
          ▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒                  ▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓                        ██╔══██║██║╚██╗██║██║   ██║██╔══╝  ██║
          ▒▒▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▒▒▒▒▒▒              ▒▒▒▒▓▓▒▒▓▓████▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▒▒                        ██║  ██║██║ ╚████║╚██████╔╝███████╗███████╗   
              ▓▓▒▒▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██▒▒▓▓▓▓▒▒░░            ▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▒▒▒▒                          ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝
                  ▓▓▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓████▓▓▒▒▒▒▒▒          ▒▒▒▒▒▒▓▓██▓▓▓▓▓▓██▓▓▓▓██▓▓██▒▒▓▓              
                      ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▒▒▒▒▒▒░░        ▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒                  
                              ▓▓▓▓▓▓██▓▓▓▓▒▒██▒▒▒▒▓▓░░    ▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓                                                       @cxcvc on discord      
                                ▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▒▒▓▓▓▓░░▒▒▓▓▒▒▓▓████▓▓▓▓▓▓▓▓▒▒                                                         ANGEL: V0
                                  ▓▓▓▓▓▓▓▓▓▓██████▓▓░░    ▓▓▒▒██▓▓██▓▓▓▓▓▓▒▒                                                           Start: {t1}
                                  ░░▓▓▓▓▓▓▓▓██████▒▒        ▓▓██▓▓▓▓▓▓▓▓▓▓                                                             
                                    ▓▓▓▓▓▓▓▓██████          ▓▓████▓▓████                                                 
                                      ██▓▓▓▓██████          ▒▒████▓▓▓▓▓▓                                  
                                      ▒▒▓▓▓▓██▓▓░░            ▓▓██▓▓▓▓                                    
                                        ▒▒▓▓░░                  ░░▓▓░░                                    
                                          ▓▓                      ██                 \n\n\n\n 

                                Logged in as @{username} ({userid}).                    
""",4))
while True:
    joiner(usertoken, status)
    time.sleep(30)

run_joiner()
