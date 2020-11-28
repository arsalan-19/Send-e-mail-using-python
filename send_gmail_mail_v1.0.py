# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 23:36:16 2020

@author: Arsalan
"""

#import packages
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename

#Email Body
mail_content = '''Hello,\nThis is a simple mail. 1 attachments is there the mail and is sent using Python SMTP library.\nThank You'''

#The e-mail addresses
sender_address = 'abc@gmail.com'
receiver_address = 'def@outlook.com'

# To Login into Gmail "app passwords" are used (Link: https://support.google.com/mail/answer/185833?hl=en)
sender_pass = "***16 character code here***"

#Or else ask for password everytime (Best practice is to import username and password from an external file instead of adding it in the code itself)
#sender_pass = input(str("Please enter your password: "))

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line

#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))

# External file attachment
file = "important.txt"
with open(file, "rb") as fil:
    part = MIMEApplication(fil.read(),Name=basename(file))
# After the file is closed
part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
message.attach(part)

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
#session = smtplib.SMTP_SSL('smtp.gmail.com') 
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')