# -*- coding: utf-8 -*-
'''
	__new__作为构造器，起创建一个类实例的作用
	__init__作为初始化器，起初始化一个已被创建的实例的作用
'''

class sample(object):
	def __str__(self):
		print "sample"

class example(object):
	def __new__(cls):
		print "__new__ is called"
		return sample()

	def __init__(self):
		print "__init__ is called"

#example()

class oldStyleClass:
	def __new__(cls): 
		print("__new__ is called") # this line will never get called during construction

	def __init__(self):
		print "__self__ is called"

# oldStyleClass()

class newStyleClass(object):
	# In Python2, we need to specify the object as the base.
    # In Python3 it's default.
    def __new__(cls):
    	print "__new__ is called"
    	return super(newStyleClass, cls).__new__(cls)
    	
	def __init__(self):
		print "__init__ is called"
		print("self is: ", self)

newStyleClass()
