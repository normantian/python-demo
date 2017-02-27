#coding=utf-8
#!/usr/bin/env python
import re
import requests
import sys
import codecs
import os
import os.path

from time import time

stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys)  
sys.setdefaultencoding('utf-8')
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde

baseUrl = "http://www.diqudaima.com"

def  ShowCity():
    html=requests.get("http://www.diqudaima.com/")
    citys= re.findall('<li><a href="(.*?)" target="_blank">', html.text,re.S)
    txtFile = 'C:/Users/Norman/Desktop/DEV/areaCode.txt'
    if os.path.exists(txtFile):
        os.remove(txtFile)
    f = codecs.open(txtFile,'w','utf-8')

    cities = [x for x in citys if not x.startswith("http")]
    
    for city in cities:
        #print city
        ShowArea(city,f)
    f.close()
def ShowArea(city,f):
    html=requests.get(baseUrl+city)
    areas = re.findall('<li><a href="(.*?)" target="_blank">',html.text,re.S)
    for a in areas:
        GetCode(a,f)

def GetCode(area,f):
    #print baseUrl+area
    html=requests.get(baseUrl+area)
    html.encoding = 'gbk'
    #print html.text.encode('utf-8')
    areas = re.findall('<li>(.*?)</li>',html.text,re.S)
    for a in areas:
        print a.encode('utf-8')
        f.write(a.encode('utf-8')+"\r\n")
        #res=re.findall('>(.*?)</a> 地区编码：(.*?) 邮编：(.*?) 电话区号：(.*?)</li>', a,re.S)
        #res=re.findall('>(.*?)</a> 地区编码：(.*?) 邮编', a,re.S)
        #res=re.findall('地区编码：(.*?) 邮编', a,re.S)
        #res=re.findall('<li>')
        #for content in res:
        #    print content.encode('utf-8')
        #f.write(a.encode('utf-8')+"\r\n")
    
def  main():
    ShowCity()


if __name__=='__main__':
    t1 = time()
    print 'net spider working','=='*20
    main()
    print 'well done','=='*20,'use time:',time()-t1

