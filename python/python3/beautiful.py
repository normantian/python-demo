import urllib
import urllib.request
import re
import time
from threading import *
from bs4 import BeautifulSoup

screenLock = Semaphore(value=1)
headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}
main_url = 'http://www.symmz.com'
num = 1
pages = set()
pages.add(main_url)

def downloadimg(url,depth):
    if depth != 0:
        print(depth)
        print(url)
        req = urllib.request.Request(url,headers=headers)
        html = urllib.request.urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(html,'html.parser')
        imgurllist = soup.find_all('img',{'src':re.compile(r'http://.+.jpg')})
        urllist = soup.find_all('a',{'href':re.compile(r'/.+?/.+?.html')})
        local_path='/Users/tianfei/Documents/images/'
        global num
        for item in imgurllist:
            print(item["src"])
            url = item["src"]
            path = local_path + str(num)+'.jpg'
            urllib.request.urlretrieve(url,path)
            num += 1
            screenLock.acquire()
            print(str(num)+' img was downloaded\n')
            screenLock.release()
            for url in urllist:
                if url not in pages:
                    global main_url
                    #newurl = main_url+url['href']
                    if str(url['href']).startswith('http'):
                        newurl = url['href']
                    else:
                        newurl = main_url+url['href']
                    downloadimg(newurl,depth-1)
                    pages.add(url)
                    time.sleep(1)
    else:
        return

def main():
    downloadimg(main_url,3)

if __name__=='__main__':
    main()
