from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.db import models
from django.contrib.auth.models import User
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



# Create your models here.
PASSWORD = "t3Qj9VHFemTyv5v"


def send_email(message, subject, Email_To, tag): 
    msg = MIMEMultipart()    
    msg['Subject'] = subject
    msg['From'] = "nomreazma@gmail.com"
    msg['To'] = Email_To
    msg['tag'] = tag
    msg.attach(MIMEText(message, 'plain'))    
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.login(msg['From'], PASSWORD)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
