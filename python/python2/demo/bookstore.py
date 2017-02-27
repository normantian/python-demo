#!/usr/bin/env python
# -*- coding: utf-8 -*-
books=[
        {"name":u"C#从入门到精通","price":23.7,"store":u"卓越"},
        {"name":u"ASP.NET高级编程","price":44.5,"store":u"卓越"},
        {"name":u"C#从入门到精通","price":24.7,"store":u"当当"},
        {"name":u"ASP.NET高级编程","price":45.7,"store":u"当当"},
        {"name":u"C#从入门到精通","price":26.7,"store":u"新华书店"},
        {"name":u"C#入门经典","price":45.7,"store":u"Amazon"},
        {"name":u"ASP.NET高级编程","price":55.7,"store":u"新华书店"}
      ]
#求在新华书店购买两本书一样一本要花的钱
price=sum([b['price'] for b in books if b['store']==u"新华书店"])
print '\n新华书店购买两本书一样一本要花的钱:',price

#求《ASP.NET高级编程》价格最便宜的店
storename=min([b for b in books if b['name']==u"ASP.NET高级编程"],key=lambda b:b['price'])["store"]
print u'\n《ASP.NET高级编程》价格最便宜的店:',storename

#列表中有几本书
booknames=list(set(b['name'] for b in books))
print '\n',booknames

#2.5 《C#从入门到精通》的平均价格：
avg=(lambda ls:sum(ls)/len(ls))([b['price'] for b in books if b['name']==u"C#从入门到精通"])
print u'\n《C#从入门到精通》的平均价格：',avg

#列表里的书都打五折	
books2=map(lambda b:dict(name=b['name'],price=b['price']*0.5,store=b['store']),books)
print books2

#《C#从入门到精通》的平均价格：
avg=(lambda ls:sum(ls)/len(ls))([b['price'] for b in books if b['name']==u"C#从入门到精通"])
print u'\n《C#从入门到精通》平均价格：',avg 

#求每本书的平均价格:
book_avg=[
				#返回一个dictionary(name,price)
				dict(name=bookname,
				#求价格平均值
				avg=(lambda ls:sum(ls)/len(ls))
				([b['price'] 
				for b in books if b['name']==bookname]))
			    for bookname in
				##去重后的书名列表
				list(set([b['name'] for b in books]))]

print u'\n每本书的平均价格',book_avg

#书籍中最低价格
min_price = min([item[p] for item in books for p in item if p=='price'])
print u'\n书籍中最低价格:',min_price

#C#相关书籍检索
for item in books:
    for p in item:
        if item['name'].find('C#')>=0:
            print item[p],  #C#相关书籍
            
cs_book = [item[p] for item in books for p in item if item['name'].find('C#')>=0]
print u'C#相关书籍:\n',cs_book
