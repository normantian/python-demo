# -*- coding:utf-8 -*-
import requests
import os
import time
from multiprocessing.dummy import Pool as ThreadPool

dst = '/Users/tianfei/Documents/python/python2/demo/爬虫/'
#保存图片到本地路径
'''
def saveImage(user_id,imgType):
    headers_1 = {
        "Host": "www.itslaw.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        "Cookie": ""
    }

    imgUrl = spellUrl(user_id,imgType)
    imgName = '%s.jpg' %(user_id)
    
    #response = requests.get("".join([imgUrl,imgType]),headers=headers_1,stream = True)
    response = requests.get(imgUrl,headers=headers_1,stream = True)
    image = response.content
    
    path = dst+imgType+"\\"+imgName
    print 'save the file: %s \n' %(path)
    with open(path,'wb') as img:
        img.write(image)
    img.close()
'''
def saveImg(user_id,imgType):
    headers_1 = {
        "Host": "www.itslaw.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        "Cookie": ""
    }

    imgUrl = spellUrl(user_id,imgType)
    imgName = '%s.jpg' %(user_id)
    
    #response = requests.get(imgUrl,headers=headers_1,stream = True)
    #image = response.content

    
    path = dst+imgType+"/"+imgName
    print 'save the file: %s \n' %(path)
    '''
    with open(path,'wb') as img:
        img.write(image)
    img.close()
    '''

    from contextlib import closing
    with closing(requests.get(imgUrl,headers = headers_1,stream = True)) as response:
        #打开文件
        with open(path,'wb') as fd:
            #每128写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)
    

def read_userid():
    txt_path = os.getcwd() + "/user_id.txt"
    li = []
    
    '''
    with open(txt_path,'rt') as handle:
        for line in filter(None, handle):
            li.append(os.path.splitext(line)[0].strip('\n'))
    return li

    '''
    with open(txt_path,'r') as f:
        for line in f.readlines():
            #print line.strip('\n')
            #print line
            li.append(line.strip())
    return li
    
    '''
    for line in open(txt_path):
        print line,
        li.append(line)
    
   
    f = open(txt_path,'rt')
    lines = f.readlines()
    for line in lines:
        print line,
        li.append(line)
    f.close()
    return li
    '''
def check_dir(dst_path):
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)

def saveImgs(param):
    #print param
    user_id,img_type = param
    saveImg(user_id,img_type)
    #print url,user_id
    
def spellUrl(user_id,img_type):
    return 'http://www.itslaw.com/api/v1/users/user/%s/avatar/%s'%(user_id,img_type)

def getImgUrls(userid_list,imgTypes):
    return [(user_id,img_type) for user_id in userid_list for img_type in imgTypes]
    
def run():
    check_dir(dst)
    imgTypes = ['large','small','medium']
    #imgTypes = ['large']
    for imgType in imgTypes:
        check_dir(dst+imgType)
    
    userid_list = read_userid()

    url_dic = getImgUrls(userid_list,imgTypes)

    #print url_dic
    #print userid_list

    '''
    start_time = time.time()
    #单线程实现
    for user_id in userid_list:
        for imgType in imgTypes:
            #saveImage('http://www.itslaw.com/api/v1/users/user/%s/avatar/'%(user_id),imgType,'%s.jpg'%(user_id))
            saveImg(user_id,imgType)
    end_time = time.time()

    print '单线程耗时 : ' + str(end_time - start_time) + ' s'
    #单线程耗时 : 64.882999897 s
    '''
    pool = ThreadPool(4)
    time3 = time.time()
    results = pool.map(saveImgs,url_dic)
    pool.close()
    pool.join()
    time4 = time.time()
    print '多线程耗时 : ' + str(time4 - time3) + ' s'
    
    #多线程耗时 : 27.5050001144 s
    #ThreadPool(2) 多线程耗时 : 35.0290000439 s
    # Thread(5) 17.2320001125 s
    #ThreadPool(6)  23.1900000572 s
    # ThreadPool 个数最好是4,5 性能比较好
    
run()
#test()
