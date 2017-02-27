# -*- coding:utf-8 -*- ＃  
import urllib  
import re  
import sys  
#import chardet  
  
def GetHtml( url):  
    page = urllib.urlopen(url)  
    contex = page.read()  
    return contex  
  
  
def GetLink(html):  
    #reg = r' <ul class="nav-hd"><li><a href="(.+)">(.+)</a></li>'
    reg = r'<ul class="nav-hd">(.*?)</ul>'  
    imgre = re.compile(reg)  
    imglist = re.findall(imgre,html)  
    return imglist  
  
url = "http://www.taobao.com/"  
get =  GetLink(GetHtml(url).decode('GB2312').encode('utf-8'))   
  
print sys.getfilesystemencoding()  
#print 'Html is encoding by : %',chardet.detect(GetHtml(url))  
  
for each in get:  
    for list in each:  
        print list,  
    print '\n'  
