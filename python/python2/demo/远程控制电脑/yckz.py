# -*- coding: utf-8 -*-
import time
import os
import sys
import poplib
import smtplib
from email.header import decode_header
from email.mime.text import MIMEText
import email

def sendMail(subject):
    sent = smtplib.SMTP('smtp.126.com')
    sent.login('normantian2004@126.com','normantian_8445')
    to=['normantian2004@126.com']
    content=MIMEText('hello')
    content['Subject']=subject
    content['From'] = 'normantian2004@126.com'
    content['To'] = ','.join(to)
##    print content['To']
    sent.sendmail('normantian2004@126.com',to,content.as_string())
    sent.close()

#此函数负责发送关机的标题（guan）给邮箱
def guanji():
    sendMail('guan')

def chongqi():
    sendMail('chong')

def read():
    #此函数负责读取邮件中的指令，指令为guan返回0，指令为chong返回1
    read = poplib.POP3('pop.126.com')
    read.user('normantian2004@126.com')
    read.pass_('normantian_8445')
    tongji = read.stat()#返回邮件基本统计信息
    str1 = read.top(tongji[0],0) #返回最近的邮件信息
    str2 = []
    for x in str1[1]: #编码与解码
        try:
            str2.append(x.decode())
        except:
            try:
                str2.append(x.decode('gbk'))
            except:
                str2.append(x.decode('big5'))
    msg = email.message_from_string('\n'.join(str2)) # 把string的邮件转换成email.message实例
    biaoti = decode_header(msg['subject'])
    if biaoti[0][1]: # 如果有第二个元素，说明有编码信息
        biaoti2 = biaoti[0][0].decode(biaoti[0][1])
    else:
        biaoti2 = biaoti[0][0]
    #此时成功获取到最近一封邮件标题 biaoti2
    if biaoti2 == 'guan':
        return 0
    if biaoti2 == 'chong':
        return 1
    read.quit()
if __name__=='__main__':
    while 1:
        time.sleep(2) #休眠2s
        r = read()
        if r == 0:
            os.system('shutdown -s -t 10')# 10s后关机
            break
        if r == 1:
            os.system('shutdown -r')#重启
            break
