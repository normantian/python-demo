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

def ShowWeather(city,f):
    res =str(city).split('" title="')
    print res[1],u'(白天-->夜间)'
    html=requests.get("http://www.tianqihoubao.com/weather/{0}".format(res[0]))
    weather=re.search('<table width="100%" border="0" class="b" cellpadding="1" cellspacing="1">(.*?)</table>', html.text,re.S).group(1)
    res=re.findall('<tr>(.*?)</tr>', weather,re.S)
    for x in res[2:]:
        w = re.findall('>(.*?)<', x,re.S)
        for y in w[1:]:
            if len(y.strip())<=0:
                pass
            else:
                print y.replace('&nbsp;','')
                f.write(y.replace('&nbsp;','')+'\n')
        print '--'*40
        f.write(''.join([str('='*20),'\n']))
    print  '\n','*'*40
    f.write(''.join([str('*'*20),'\n']))

def  ShowCity():
    html=requests.get("http://www.tianqihoubao.com/weather/province.aspx?id=420000")
    citys= re.findall('<td style="height: 22px" align="center"><a href="(.*?)">', html.text,re.S)
    txtFile = 'C:/Users/Norman/Desktop/DEV/weather.txt'
    if os.path.exists(txtFile):
        os.remove(txtFile)
    f = codecs.open(txtFile,'w','utf-8')
    for city in citys:
        ShowWeather(city,f)
    f.close()


def  main():
    ShowCity()


if __name__=='__main__':
    t1 = time()
    print 'net spider working','=='*20
    main()
    print 'well done','=='*20,'use time:',time()-t1

