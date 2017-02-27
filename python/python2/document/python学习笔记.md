#**Python 三目运算符 bool ? a : b 表达式**#
在python中没有类似java和C语言中的bool？a：b表达式
但是有变通实现的语句：

    print x if x<0 else y

另一种实现使用 and-or 
and-or主要是用来模仿 三目运算符 bool?a:b的，即当表达式bool为真，则取a否则取b，and-or 技巧，bool and a or b 表达式，当 a 在布尔上下文中的值为假时，不会像 C 语言表达式 bool ? a : b 那样工作。
所以我们需要一种安全的形式使用and-or：

	>>> a=""
	>>> b="second"
	>>> (1 and [a] or [b])
	['']
	>>> (1 and [a] or [b])[0]
	''
	>>> 
由于 [a] 是一个非空列表，所以它决不会为假。即使 a 是 0 或者 '' 或者其它假值，列表 [a] 也为真，因为它有一个元素。

#**xrange 和 range**#
##**xrange 和 range**##
语法：`range(stop)`

语法： `range(start,stop[,step])`

> xrange与range语法相同，但性能更好，更快更节省内存。
> range返回一个List。而xrange返回一个对象。



    for num in xrange(10):
    	print(num)
**xrange 比 range性能更好。推荐使用xrange替换range。**


----------

#**if判断**#
## if判断 ##
    if <判断条件1>：
    	<执行1>
    elif <判断条件2>：
      	<执行2>
    else
      	<执行3>

**只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。**

----------

#**循环**#
## enumerate() ##
当需要显示序列index时，使用enumrate函数 `enumrate(iterable[,start])` 示例如下：

	>>> for i, v in enumerate(['tic', 'tac', 'toe']):
	...     print i, v
	...
	0 tic
	1 tac
	2 toe

## zip() ##
当同时遍历两个或多个sequence时，使用zip函数，示例如下：
	
	>>> questions = ['name', 'quest', 'favorite color']
	>>> answers = ['lancelot', 'the holy grail', 'blue']
	>>> for q, a in zip(questions, answers):
	...     print 'What is your {0}?  It is {1}.'.format(q, a)
	...
	What is your name?  It is lancelot.
	What is your quest?  It is the holy grail.
	What is your favorite color?  It is blue.

## reversed()和 a[::-1] ##
倒序遍历sequence ，使用reversed函数：

	>>> for i in reversed(xrange(1,10,2)):
	...     print i
	...
	9
	7
	5
	3
	1
另一种优雅的倒序实现方式 **a[::-1]**：

	>>> a = [1,2,3,4,5]
	>>> for i in a[::-1]
			print i
## sorted() ##
要按顺序遍历一个序列，使用sorted()函数返回一个新的排序列表而源列表不变。

	>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
	>>> for f in sorted(set(basket)):
	...     print f
	...
	apple
	banana
	orange
	pear
## L[:] copy List ##
当遍历一个sequence时，需要改变sequence元素，推荐使用copy。示例代码如下：

	>>> words = ['cat', 'window', 'defenestrate']
	>>> for w in words[:]:  # Loop over a slice copy of the entire list.
	 		if len(w) > 6:
	... 		words.insert(0, w)
	...
	>>> words
	['defenestrate', 'cat', 'window', 'defenestrate']

  List 拷贝代码：

	>>> word = ['cat','dog']
	>>> word_copy = word
	>>> word.append('pig')
	>>> word_copy
	['cat', 'dog', 'pig']
	>>> word_copy = word[:] # list copy
	>>> word_copy
	['cat', 'dog', 'pig']
	>>> del word[0]
	>>> word
	['dog', 'pig']
	>>> word_copy
	['cat', 'dog', 'pig']

## 三个内置函数 map filter reduce 和列表推导(List Comprehensions)##
**map(func,list)**:将list的每一个元素传递给func的函数，这个函数有一个参数，且返回一个值，map将每一次调用函数返回的值组成一个新列表返回。

**filter(func,list)**:将list的每一个元素传递给func的函数，这个函数有一个参数，返回bool类型的值，filter将返回True的元素组成新列表返回。

**reduce（func,list）**:将list的元素，挨个取出来和下一个元素通过func计算后将结果和再下一个元素继续计算
filter(function, sequence) 过滤 function(item) 为true：

	>>> def f(x): return x % 3 == 0 or x % 5 == 0
	...
	>>> filter(f, range(2, 25))
	[3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24]


 	>>> def f(x): return x in 'aeiou'

	>>> filter(f,('a','c','b','e'))
	('a', 'e')


`map(function,sequence)`  对于sequence 里面的每个item调用 `function(item)`返回值形成一个新的
list 示例代码：

	>>> def cube(x): return x**3
	...
	>>> map(cube,range(1,11))
	[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

如果操作的sequence多于一个，也可以调用function(item1,item2),示例代码：
	>>> seq = range(8)
	>>> def add(x,y): return x+y
	...
	>>> map(add,seq,seq)
	[0,2,4,6,8,10,12,14]

`reduce(function,sequence[,initial])` 返回一个值，对序列中的元素进行逐个计算，例如计算1-10的和：

	>>> def add(x,y): return x+y
	...
	>>> reduce(add,range(1,11))
	55

**注意如果sequence为空，那会抛出异常，需要设置initial** 示例代码：

	>>> def sum(seq):
	...     def add(x,y): return x+y
	...     return reduce(add, seq, 0)
	...
	>>> sum(range(1, 11))
	55
	>>> sum([])
	0
###列表推导###
将符合列表公式的代码写在列表定义中，可以简化代码。
例如：

	>>> squares = []
	>>> for x in range(10):
	...     squares.append(x**2)
	...
	>>> squares
	[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
等价于：

	squares = [x**2 for x in range(10)]

也可以等价于map和filter函数：

	>>> foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
`print(filter(lambda x: x % 3 == 0, foo))`
等价于
`print([x for x in foo if x % 3 == 0])`

`print(map(lambda x: x * 2 + 10, foo))`等价于
`print([x * 2 + 10 for x in foo])`

循环过滤素数算法：

	# 求2到49范围内的素数
	>>> nums = range(2, 50)
	>>> for i in range(2, 8):
      	 nums = [x for x in nums if x==i or x % i != 0]
	>>> nums
	[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
另一种实现：

	#单行程序扫描素数    

	from math import sqrt    
	N = 100   
	[ p for p in   range(2, N) if 0 not in [ p% d for d in range(2, int(sqrt(p))+1)] ]  

 
**一个需求演示**
假如有列表：

	books=[
        {"name":"C#从入门到精通","price":23.7,"store":"卓越"},
        {"name":"ASP.NET高级编程","price":44.5,"store":"卓越"},
        {"name":"C#从入门到精通","price":24.7,"store":"当当"},
        {"name":"ASP.NET高级编程","price":45.7,"store":"当当"},
        {"name":"C#从入门到精通","price":26.7,"store":"新华书店"},
        {"name":"ASP.NET高级编程","price":55.7,"store":"新华书店"}
      ]
- 求《ASP.NET高级编程》价格最便宜的店
		
		storename=min([b for b in books if b['name']=="ASP.NET高级编程"],key=lambda b:b['price'])["store"]

过程：先用列表解析取出《ASP.NET高级编程》的列表，通过min函数，比较字典的price键获取price最小的项。

-  求在新华书店购买两本书一样一本要花的钱
 
		price=sum([b['price'] for b in books if b['store']=="新华书店"])

- 求列表中有几本书：

		bookenames=list(set(b['name'] for b in books))

- 列表里的书都打五折
	
		books=map(lambda b:dict(name=b['name'],price=b['price']*0.5,store=b['store']),books)

- 《C#从入门到精通》的平均价格：

		avg=(lambda ls:sum(ls)/len(ls))([b['price'] for b in books if b['name']=="C#从入门到精通"])
定义一个lambda匿名函数求平均值`sum(ls)/len(ls)`然后传入参数。

- 求每本书的平均价格：

		book_avg=map(
			lambda bookname:
				#返回一个dictionary
				dict(name=bookname,
				#求价格平均值
				avg=(lambda ls:sum(ls)/len(ls))
				([b['price'] for b in books if b['name']==bookname])),
				list(set([b['name'] for b in books])))

或者列表推导实现：

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

step1 要求每本书的平均价格，首先要得到共有几本书，得到去重的书名列表`list(set([b['name'] for b in books]))` #去重后的书名列表.

step2 要求每一本书的均价，需要将计算均价的函数映射到每一本书上，于是

	map(
    	#计算均价的函数，
    	list(set([b['name'] for b in books])) #去重后的书名列表
	)

step3 计算平均价格可以参考上一个例子的方法：

	func=lambda bookname:
		(lambda ls:sum(ls)/len(ls))([b['price'] for b in books if b['name']==bookname])


----------

#**List**#
    >>> L = [1,3,4,5]
    >>> L = [1,'string',6.5,[1,2],True] # List中也可以类型不同

## **List 集合操作**
### List method that modify the list： ###
    list.append(object)
	list.extend(list2)
	list.pop()
	list.remove(object)
	list.reverse()
	list.sort()
	list.insert(int,object)

	l = [1,2,3]
	l = l + [4,5]
	>>> [1,2,3,4,5]

### List method that do not modify the list:： ###
	list.count(object)
	list.index(object)

### Stack(使用List) ###

	>>> stack = [3, 4, 5]
	>>> stack.append(6)
	>>> stack.append(7)
	>>> stack
	[3, 4, 5, 6, 7]
	>>> stack.pop()
	7
	>>> stack
	[3, 4, 5, 6]
	>>> stack.pop()
	6
	>>> stack.pop()
	5
	>>> stack
	[3, 4]

### Queue ###
使用from collections import deque

	>>> from collections import deque
	>>> queue = deque(["Eric", "John", "Michael"])
	>>> queue.append("Terry")           # Terry arrives
	>>> queue.append("Graham")          # Graham arrives
	>>> queue.popleft()                 # The first to arrive now leaves
	'Eric'
	>>> queue.popleft()                 # The second to arrive now leaves
	'John'
	>>> queue                           # Remaining queue in order of arrival
	deque(['Michael', 'Terry', 'Graham'])

###嵌套列表解析###
一个矩阵3*4的矩阵

	>>> matrix = [
 	[1, 2, 3, 4],
 	[5, 6, 7, 8],
 	[9, 10, 11, 12],
	 ]
转置行列：

	>>> [[row[i] for row in matrix] for i in range(4)]
	[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

等价于：

	>>> transposed = []
	>>> for i in range(4):
	...     transposed.append([row[i] for row in matrix])
	...
	>>> transposed
	[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

最好的选择：

	>>> zip(*matrix)
	[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

###del操作###
	>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
	>>> del a[0]
	>>> a
	[1, 66.25, 333, 333, 1234.5]
	>>> del a[2:4]
	>>> a
	[1, 66.25, 1234.5]
	>>> del a[:]
	>>> a
	[]


----------

#**tuple**#
有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改。例如：

	classmates = ('Michael', 'Bob', 'Tracy')
	
现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用`classmates[0]`，`classmates[-1]`，但不能赋值成另外的元素。

因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

**tuple陷阱** 你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来。
但是，要定义一个只有1个元素的tuple，如果你这么定义:

	>>> t=(1)
	>>> t
	1
定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
所以，**只有1个元素的tuple定义时必须加一个逗号**,，来消除歧义：

	t=(1,)
	t
	(1,)

可以这样对tuple赋值：

	t = 12345, 54321, 'hello!'

	>>> empty = () #空tuple
	>>> singleton = 'hello',    # <-- note trailing comma
	>>> len(empty)
	0
	>>> len(singleton)
	1
	>>> singleton
	('hello',)

对于tuple里面的值可以进行获取如下：

	>>> t = 12345, 54321, 'hello!'
	>>> x,y,z=t # x=12345, y=54321,z='hello'


----------

#**dic 和 set**#
##dict##
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
举个例子，假设要根据同学的名字查找对应的成绩，如果用list实现，需要两个list。给定一个名字，要查找对应的成绩，就先要在names中找到对应的位置，再从scores取出对应的成绩，list越长，耗时越长。

如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：
> 注意是花括号{key1:value1,key2:value2....}

	d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
	d['Michael']
	95
key不存在就会报错，先**判断key是否在dic中**：

1. key in dic
2. d.get(key) 判断是否为None
3. d.has_key(key) 判断 True or False

**dic中添加一个key-value：**
	
	dic.setdefault('Norman'，100)
或者

	dic['Norman'] = 100

**dic中删除一个key**

	dic.pop(key) 
或者

	del dic[key]

**dic获取keys**

	dic.keys()

**dict表达式初始化**

	>>> {X:X**2 for x in (2,4,6)}
	{2:4,4:16,6:36}

**dict 构造函数**

	>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
	{'sape': 4139, 'jack': 4098, 'guido': 4127}

*如果keys是string可以用如下构造函数：*
	
	>>> dict(sape=4139, guido=4127, jack=4098)
	{'sape': 4139, 'jack': 4098, 'guido': 4127}

**zip()**
zip函数返回一个tuple的list，可以将多个list相应位置的元素形成tuple，并且可以在参数前加*，可以实现unzip list功能。例如：

	>>> x = [1, 2, 3]
	>>> y = [4, 5, 6]
	>>> zipped = zip(x, y)
	>>> zipped
	[(1, 4), (2, 5), (3, 6)]
	>>> x2, y2 = zip(*zipped)
	>>> x == list(x2) and y == list(y2)
	True
**遍历dict获取K-V**
使用 `dict.iteritems()` 例如：

	>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
	>>> for k, v in knights.iteritems():
	...     print k, v
	gallahad the pure
	robin the brave

或者使用:

	>>> for key in dic.keys():
			print key, dic[key] #print key, dic.get(key)

##Set##
Set中内容无重复，声明一个空的set：`set()`
一些测试代码：

	>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
	>>> fruit = set(basket)               # create a set without duplicates
	>>> fruit
	set(['orange', 'pear', 'apple', 'banana'])
	>>> 'orange' in fruit                 # fast membership testing
	True
	>>> 'crabgrass' in fruit
	False

	>>> # Demonstrate set operations on unique letters 
	>from two words
	...
	>>> a = set('abracadabra')
	>>> b = set('alacazam')
	>>> a                                  # unique letters in a
	set(['a', 'r', 'b', 'c', 'd'])
	>>> a - b                              # letters in a but not in b 差集
	set(['r', 'd', 'b'])
	>>> a | b                              # letters in either a or b 并集
	set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
	>>> a & b                              # letters in both a and b 交集
	set(['a', 'c'])
	>>> a ^ b                              # letters in a or b but not both 对称差分
	set(['r', 'd', 'b', 'm', 'z', 'l'])

类似列表推导，Set使用{}：

	>>> a = {x for x in 'abracadabra' if x not in 'abc'}
	>>> a
	set(['r', 'd'])


set(list1) | set(list2)union包含 list1 和 list2 所有数据的新集合

set(list1) & set(list2)intersection包含 list1 和 list2 中共同元素的新集合

set(list1) – set(list2)difference在 list1 中出现但不在 list2 中出现的元素的集合

set(list1）^ set(list2) 对称差分，不同时出现在list1和list2里的元素

#### Set方法汇总
1. ```issubset()``` 判断一个set是否是另一个set的子集使用方法:
```	
	>>> set1 = {1,2,3}
	>>> {1,2}.issubset(set1)
	True
    >>> {4}.issubset(set1)
    False


2.  ``` union()``` 两个集合的并集，等同于set1 | set2，使用方法：
```
	>>>{1,2,3}.union({3,4,5,6})
	set([1,2,3,4,5,6])
```

3. ``` difference() ``` 两个set中，在set1中出现但不在set2中出现的元素集合，返回一个set，与 set1 - set2等同
```
	>>>{1,2,3}.difference({3,4,5,6})
	set([1, 2])
```

4. ``` intersection()``` 两个set的交集，等同于set1 & set2
```
	>>> {1,2,3}.intersection({1,2,4})
	set([1, 2])
```

5. ``` difference_update() ``` 两个set中，在set1中出现但不在set2中出现的元素集合赋给set1,即将difference()结果赋给set1,与 set1 = set1 - set2等同
```
	>>> set1 = {1,2,3}
	>>> set2 = {1,2,5}
	>>> set1.difference_update(set2)
	>>> set1
	set([3])
```

6. ``` intersection_update()``` 两个集合set1，set2的交集赋给set1，等同于set1 = set1 & set2
```
	>>> set1 = {1,2,3}
	>>> set2 = {1,2,5}
	>>> set1.intersection_update(set2)
	>>> set1
	set([1,2])
```

7. ```update()``` 和 ```union()``` union 返回set1 和 set2 所有数据的新集合，与set1 | set2等同。update相当于 set1 =  set1 | set2 

8. ``` remove()```和 ``` discard()``` 两个都是删除set中的元素，不同的是，remove要求删除的元素必须在set中，否则报错。而discard不要求元素必须在set中。
```
	>>> set1 = {1,2,3}
	>>> set1.remove(1)
	>>> set1.discard(2)
	>>> set1
	set([3])
	>>> set1.remove(10)
	Traceback (most recent call last):
	File "<pyshell#127>", line 1, in <module>
	set1.remove(10)
	KeyError: 10
```

#**Python 函数的参数**#
##默认参数##
第一版 power方法:
```
	def power(x):
		return x*x
```
如果第二版改成 ```power(x,n)```,求x的n次方：
```
    def power(x,n)：
    	s = 1
        while n>0:
        	n = n-1
            s = s*x
        return s
```
但是旧的调用```power(5)```会失败，我们可以设置默认参数来解决这个兼容问题。
```
    def power(x,n=2)：
    	s = 1
        while n>0:
        	n = n-1
            s = s*x
        return s
```

##可变参数##
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 +...
```
    def calc(*numbers):
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum
```
调用方式：
```
	>>> calc(1, 2, 3)
    14
    >>> calc(1, 3, 5, 7)
    84
    >>> nums = [1, 2, 3]
    >>> calc(*nums)
    14
```
##关键字参数##
关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
```
    def person(name, age, **kw):
        print 'name:', name, 'age:', age, 'other:', kw
```
调用方式：
```
	>>> person('Michael', 30)
	name: Michael age: 30 other: {}
    >>> person('Bob', 35, city='Beijing')
    name: Bob age: 35 other: {'city': 'Beijing'}
    >>> person('Adam', 45, gender='M', job='Engineer')
    name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
    简化写法：
    >>> kw = {'city': 'Beijing', 'job': 'Engineer'}
    >>> person('Jack', 24, **kw)
    name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```
##参数组合##
在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
```
    def func(a, b, c=0, *args, **kw):
        print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
```
调用方式：
```
    >>> func(1, 2)
    a = 1 b = 2 c = 0 args = () kw = {}
    >>> func(1, 2, c=3)
    a = 1 b = 2 c = 3 args = () kw = {}
    >>> func(1, 2, 3, 'a', 'b')
    a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
    >>> func(1, 2, 3, 'a', 'b', x=99)
    a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
```
最神奇的是通过一个tuple和dict，你也可以调用该函数
```
    >>> args = (1, 2, 3, 4)
    >>> kw = {'x': 99}
    >>> func(*args, **kw)
    a = 1 b = 2 c = 3 args = (4,) kw = {'x': 99}
```