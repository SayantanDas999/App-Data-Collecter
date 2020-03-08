# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 14:49:23 2020

@author: Sayantan
"""

from email.mime.text import MIMEText
import smtplib

def send_email(email,height,avg_height,count):
    from_email="aakashi.roy@gmail.com"
    from_password="ohmygod9"
    to_email=email
    
    subject="Height Details"
    message="Hey User, Your Height is <strong>%s</strong> cm. The Average Height of all the member is <strong>%s</strong> cm. Result has been calculated out of <strong>%s</strong> people." % (height,avg_height,count)
    
    msg=MIMEText(message,'html')
    msg["Subject"]=subject
    msg["From"]=from_email
    msg["To"]=to_email
    
    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
    
    