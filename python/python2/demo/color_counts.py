# -*- coding: utf-8 -*-
'''
对列表中各项目进行计数有各种各样的方法，
接下来我们将通过观察每一种方法的代码风格，来分析这些技术的不同之处
'''
# Python 1.4
colors = ["brown","red","green","yellow","brown","brown","black","red"]
color_counts={}
for c in colors:
    if color_counts.has_key(c):
        color_counts[c] = color_counts[c] + 1
    else:
        color_counts[c] = 1
print color_counts
#另一种写法
for c in colors:
    if not color_counts.has_key(c):
        color_counts[c] = 0
    color_counts[c] = color_counts[c] + 1
print color_counts

#try块写法
for c in colors:
    try:
        color_counts[c] = color_counts[c] + 1
    except KeyError:
        color_counts[c] = 1
print color_counts

#get写法 Python1.5
for c in colors:
    color_counts[c] = color_counts.get(c,0) + 1
print color_counts

#setdefault 方法 Python 2.0
for c in colors:
    color_counts.setdefault(c, 0)
    color_counts[c] += 1
print color_counts

#fromkeys 方法 Python 2.3
color_counts = dict.fromkeys(colors,0)
for c in colors:
    color_counts[c] += 1
print color_counts

#生成器表达式 Python 2.4
'''
这段代码的复杂度是 O(n2)，与复杂度为 O(n) 的代码相比，
这段代码的美观度和可读性更差。这次的改变只是一次很有趣的实验，
但是这种一行式的方法更不符合 Python 的风格
'''
color_counts = dict((c, colors.count(c)) for c in set(colors))
print color_counts

#defaultdict 方法 Python 2.5
from collections import defaultdict
color_counts = defaultdict(int)
for c in colors:
    color_counts[c] += 1
print color_counts

#计数 Python 2.7
from collections import Counter
color_counts = Counter(colors)
print color_counts

