#!/bin/python3
#Author: L4z4rt
from colorama import Fore, init
import requests, os, platform

def clr():   
    if platform.system() == "Linux":
        os.system("clear")
        
    elif platform.system()== "Windows":
        os.system("cls") 
        
def sendMessage(phone, message):
    key = "textbelt" # <-- Ingrese su api key de textbelt en esat variable
    resp = requests.post('https://textbelt.com/text', {
      'phone': phone,
      'message': message,
      'key': key
    })
    payload = resp.json()
    succesData = payload['success']
    try:
        quotaData = payload['quotaRemaining']
        textIdData = payload['textId']
        clr()
        print(f"{Fore.GREEN}< ---- Succes ---- >")
        print(f"Target: {phone}")
        print(f"Message: {message}")
        print(f"\nStatus: {succesData}")
        print(f"QuotaRemaining: {quotaData}")
        print(f"Id: {textIdData}")
    except:
        print(f"{Fore.RED}[*]Error: Verifique el numero destinatario y/o la cuota de su api(Recuerde que puede enviar un mensaje gratuito por dia)")
if __name__ == "__main__":
    phone = input("Phone(Add Code Country): ")
    message = input("Message: ")
    sendMessage(phone, message)
