# -*- coding:utf-8 -*-
import requests
import os

dst = 'e:\\baidu_img\\'
#保存图片到本地路径
def saveImage(imgUrl,dst1,imgName= 'default.jpg'):
    response = requests.get(imgUrl,stream = True)
    image = response.content
    #dst = 'e:\\baidu_img\\'
    path = dst1+"\\"+imgName
    print 'save the file: %s \n' %(path)
    with open(path,'wb') as img:
        img.write(image)
    img.close()

def getClassify():
    url_2 = "http://www.tngou.net/tnfs/api/classify"
    r = requests.get(url_2)
    r = r.json()
    
    classify_list = []
    for line in r['tngou']:
        classify_list.append(line['id'])
    return classify_list
    
    
#开始
def run_classify(classify_id,dst1):
    url_1 = "http://www.tngou.net/tnfs/api/list"
    #url_2 = "http://www.tngou.net/tnfs/api/classify"
    src_header = "http://tnfs.tngou.net/image"
    headers_1 = {'apikey':'995d38897457ab274b725a284d01010c'}
    params_1 = {
        'page':1,
        'rows':20,
        'id':classify_id      #需根据classify结果才能知道
    }
    r = requests.get(url_1,params=params_1,headers=headers_1)
    r = r.json()
    total = int(r['total'])
    if total % 20 == 0:
        page_total = total / 20
    else:
        page_total = total / 20 + 1
    print '%s 主题共 %s页，共 %s 张图片 ' %(classify_id,page_total,total)
    for page in xrange(1,page_total+1):
        params_2 = {
            'page':page,
            'rows':20,
            'id':classify_id     #需根据classify结果才能知道
        }
        r = requests.get(url_1,params=params_2,headers=headers_1)
        r = r.json()
        for line in r['tngou']:
            title = line['title']
            img = line['img']
            src_path = src_header+img
            saveImage(src_path,dst1,title+'.jpg')
def run():
    li = getClassify()
    for classify_id in li:
        dst1 = "".join([dst,str(classify_id)]) 
        if not os.path.exists(dst1):
            os.mkdir(dst1)
        run_classify(classify_id,dst1)
run()
