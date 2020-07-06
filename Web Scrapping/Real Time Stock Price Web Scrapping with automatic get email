# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 22:16:10 2020

@author: Manish Singh
"""

import smtplib, ssl
import requests
import bs4
from bs4 import BeautifulSoup

def parsePrice():
    # Used Yahoo Finace for share prices
    req = requests.get('https://in.finance.yahoo.com/quote/TATAMOTORS.NS?p=TATAMOTORS.NS')
    soup = bs4.BeautifulSoup(req.text, "lxml")
    price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
    return price

def send_mail():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "sender@gmail.com"  # Enter your address
    receiver_email = "receiver@gmail.com"  # Enter receiver address
    password = input("Type your password and press enter: ")
    message = "Updated share price is " + str(parsePrice())
    
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        
send_mail()
