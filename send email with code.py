import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
html=Template(Path('ht.html').read_text())
email=EmailMessage()
email['from']='Vasudeva'
email['to']='kilaru.kilaru@gmail.com'
email['subject']='Hi'
#email.set_content('greetings:hiiiii!')
email.set_content(html.substitute({'name':'dingDing'}),'html')
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp :
smtp.ehlo()
smtp.starttls()
smtp.login('some.address@email.com','xxxxx@yyyy')
smtp.send_message(email)
print('ran well')
