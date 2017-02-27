import smtplib
import poplib
from email.header import decode_header
from email.mime.text import MIMEText
import email

def send():
    sent = smtplib.SMTP('smtp.126.com')
    sent.login('normantian2004@126.com','normantian_8445')
    to=['normantian2004@126.com','229398612@qq.com']
    content=MIMEText('hello')
    content['Subject']='guan'
    content['From'] = 'normantian2004@126.com'
    content['To'] = ','.join(to)
##    print content['To']
    sent.sendmail('normantian2004@126.com',to,content.as_string())
    sent.close()
