# Email Module using SMTP library (Adopted from Nael Shiab of http://naelshiab.com/)
#
# Sends e-mail via GMail server

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
def email(toAddr, fromAddr, subject, message, password):
	msg = MIMEMultipart()
	msg['From'] = fromAddr
	msg['To'] = toAddr
	msg['Subject'] = subject
	 
	body = message
	msg.attach(MIMEText(body, 'plain'))
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromAddr, password)
	text = msg.as_string()
	server.sendmail(fromAddr, toAddr, text)
	server.quit()
