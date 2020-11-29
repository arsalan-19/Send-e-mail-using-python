# Send-e-mail-using-python

The repository contains the code to send emails using different source mail portals i.e. Gmail and Outlook

Following are the minor changes need to be done in the code while using different mail services 

**1. To send using Gmail:**
(a) For Gmail sender email authentication "App password" is needed which we can get by following the steps explained [here](Link: https://support.google.com/mail/answer/185833?hl=en) <br />
(b) While creating session change the host_name to 'smtp.gmail.com' and port number to '587' <br />
session = smtplib.SMTP('smtp.gmail.com', 587)

**2. To send using Outlook:**
(a) Here login email and password is sufficient (No need for any other details) <br />
(b) While creating session change the host_name and port number as per displayed in the Outlook Mail >> Settings >> Search for "POP and IMAP" >> SMTP setting <br />
session = smtplib.SMTP('smtp.office365.com', 587)
