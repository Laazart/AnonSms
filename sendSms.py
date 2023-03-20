#!/bin/python3
#Author: L4z4rt
from colorama import Fore, init
import requests
import os
import platform

def clr():   
    if platform.system() == "Linux":
        os.system("clear")
        
    elif platform.system()== "Windows":
        os.system("cls") 
        
def sendMessage(x, y):
    key = "textbelt"
    resp = requests.post('https://textbelt.com/text', {
      'phone': x,
      'message': y,
      'key': key
    })
    payload = resp.json()
    succesData = payload['success']
    try:   
        quotaData = payload['quotaRemaining']
    except :
        print(f"{Fore.RED}\n[*] Ingrese un numero valido!")
        exit()
    try:         
        textIdData = payload['textId']
        clr()
        print(f"{Fore.GREEN}< ---- Succes ---- >")
        print(f"Target: {phone}")
        print(f"Message: {message}")
        print(f"\nStatus: {succesData}")
        print(f"QuotaRemaining: {quotaData}")
        print(f"Id: {textIdData}")
    except:
        errorData = payload['error']
        clr()
        print(f"{Fore.RED}< ---- Error ---- >")
        print(f"Status: {succesData}")
        print(f"Error: {errorData}")
        print(f"QuotaRemaining: {quotaData}")
if __name__ == "__main__":
    phone = input("Phone: ")
    message = input("Message: ")
    sendMessage(phone, message)
