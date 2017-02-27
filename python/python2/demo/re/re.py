# -*- coding: utf-8 -*-
import re

numbers = ["123 555 6789","1-(123)-555-6789",
           "(123-555-6789","(123).555.6789","(123) 525 6789"]

#检测电话美国电话号码的正则表达式
for number in numbers:
    pattern = re.match(r'^'
    r'(1[-\s.])?' # optional '1-', '1.' or '1'
    r'(\()?' # optional opening parenthesis
    r'\d{3}' # the area code
    r'(?(2)\))' # if there was opening parenthesis, close it
    r'[-\s.]?' # followed by '-' or '.' or space
    r'\d{3}' # first 3 digits
    r'[-\s.]?' # followed by '-' or '.' or space
    r'\d{4}$', number)#, re.DEBUG) # last 4 digits

    if pattern:
        print '{0} is valid'.format(number)
    else:
        print '{0} is not valid'.format(number)

#贪婪与非贪婪
html = 'Hello <a href="http://pypix.com" title="pypix">Pypix</a>'

m = re.findall('<a.*>.*<\/a>', html) #贪婪
if m:
    print m

html2 = 'Hello <a href="http://pypix.com" title="pypix">Pypix</a> Hello <a href="http://example.com" title"example">Example</a>'

m = re.findall('<a.*>.*<\/a>', html2) # 贪婪
if m:
    print m
#['<a href="http://pypix.com" title="pypix">Pypix</a> Hello <a href="http://example.com" title"example">Example</a>']

m = re.findall('<a.*?>.*?<\/a>', html2) #非贪婪
if m:
    print m
#结果
#['<a href="http://pypix.com" title="pypix">Pypix</a>', '<a href="http://example.com" title"example">Example</a>']

'''
(?=exp)	匹配exp前面的位置
(?<=exp)	匹配exp后面的位置
(?!exp)	匹配后面跟的不是exp的位置
(?<!exp)	匹配前面不是exp的位置
'''
strings = [ "hello foo", # returns False
"hello foobar" ] # returns True
#首先匹配 foo，然后检测是否接着匹配 bar
for string in strings:
    pattern = re.search(r'foo(?=bar)', string)
    if pattern:
        print 'True'
    else:
        print 'False'
print '==' * 30
#匹配foo，当且仅当它的后面没有跟着 bar
strings = [ "hello foo", # returns True
"hello foobar", # returns False
"hello foobaz"] # returns True

for string in strings:
    pattern = re.search(r'foo(?!bar)', string)
    if pattern:
        print 'True'
    else:
        print 'False'
print '==' * 30

#匹配一个不是跟在 foo 后面的 bar
strings = [ "hello bar", # returns True
"hello foobar", # returns False
"hello bazbar"] # returns True

for string in strings:
    pattern = re.search(r'(?<!foo)bar',string)
    if pattern:
        print 'True'
    else:
        print 'False'
print '==' * 30
#条件(IF-Then-Else)模式
#(?(?=regex)then|else)
#检测打开和闭合的尖括号
strings = [ "<pypix>", # returns true
"<foo", # returns false
"bar>", # returns false
"hello" ] # returns true

for string in strings:
    pattern = re.search(r'^(<)?[a-z]+(?(1)>)$', string)
    if pattern:
        print 'True'
    else:
        print 'False'
#1 表示分组 (<)，当然也可以为空因为后面跟着一个问号。当且仅当条件成立时它才匹配关闭的尖括号。

print '==' * 30
'''分组，由圆括号括起来，将会捕获到一个数组，然后在后面要用的时候可以被引用。
但是我们也可以不捕获它们。
'''
string = 'Hello foobar' 
pattern = re.search(r'(f.*)(b.*)', string) 
print "f* => {0}".format(pattern.group(1)) # prints f* => foo
print "b* => {0}".format(pattern.group(2)) # prints b* => bar

#(?:exp) 匹配exp,不捕获匹配的文本，也不给此分组分配组号
pattern = re.search(r'(?:H.*)(f.*)(b.*)', string)
if pattern:
    print "f* => {0}".format(pattern.group(1)) # f* => foo
    print "b* => {0}".format(pattern.group(2)) # b* => bar

#组命名
'''
(?Ppattern)
'''
pattern = re.search(r'(?P<fstar>f.*)(?P<bstar>b.*)', string) 
print "f* => {0}".format(pattern.group('fstar')) # prints f* => foo
print "b* => {0}".format(pattern.group('bstar')) # prints b* => bar
#我们可以添加另外一个分组了，而不会影响模式数组里其他的已存在的组
pattern = re.search(r'(?P<hi>H.*)(?P<fstar>f.*)(?P<bstar>b.*)', string) 
print "f* => {0}".format(pattern.group('fstar')) # prints f* => foo
print "b* => {0}".format(pattern.group('bstar')) # prints b* => bar
print "h* => {0}".format(pattern.group('hi')) # prints b* => Hello

#在 Python 中 re.sub() 可以用来给正则表达式替换添加回调函数
template = "Hello [first_name] [last_name], \
Thank you for purchasing [product_name] from [store_name]. \
The total cost of your purchase was [product_price] plus [ship_price] for shipping. \
You can expect your product to arrive in [ship_days_min] to [ship_days_max] business days. \
Sincerely, \
[store_manager_name]" 
# assume dic has all the replacement data
# such as dic['first_name'] dic['product_price'] etc...
dic = { 
"first_name" : "John", 
"last_name" : "Doe", 
"product_name" : "iphone", 
"store_name" : "Walkers", 
"product_price": "$500", 
"ship_price": "$10", 
"ship_days_min": "1", 
"ship_days_max": "5", 
"store_manager_name": "DoeJohn" 
} 
#result = re.compile(r'\[(.*)\]') 
#print result.sub('John', template, count=1)

def multiple_replace(dic, text):
    pattern = "|".join(map(lambda key : re.escape("["+key+"]"), dic.keys()))
    print pattern
    return re.sub(pattern, lambda m: dic[m.group()[1:-1]], text) 
print multiple_replace(dic, template)
