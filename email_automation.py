#sent_mail_with_attachment

import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from_addr = '**@gmail.com'
to_addr = '**@gmail.com'
subject = 'stock_statement!!'
content = '''Hi Team,
PFA stock statement .

regards,
unknown'''

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
body = MIMEText(content, 'plain')
msg.attach(body)
filename = 'test.txt'

with open(filename,'r') as f :
    attachment = MIMEApplication(f.read(),Name = basename(filename))
    attachment['Content-Disposition'] = 'attachment ; filename="{}"'.format(basename(filename))
    
    
msg.attach(attachment)
server = smtplib.SMTP('smtp.gmail.com', port=587)
server.ehlo()
server.starttls()
#server.connect('smtp.gmail.com', 587)
server.login('**@gmail.com' , 'PassW0RD')
server.send_message(msg,from_addr = from_addr , to_addrs=[to_addr])
