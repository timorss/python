from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message['from'] = 'Timor Sulimani'
message['to'] = 'timorss@gmail.com'
message['subject'] = 'this is a text'
message.attach(MIMEText('Body'))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("timorss@gmail.com", 'Mkhyef2912')
    smtp.send_message(message)
    print('sen...')
