
# 练习类和使用

'''''
类是用来管理函数的，类的引用是为了面向对象编程
Python同时支持面向过程编程和面向对象编程,没有使用class就是面向过程编程
'''


class Calculator:
	def addition(x, y):
		added = x + y
		print(added)

	def subtraction(x, y):
		sub = x - y
		print(sub)

	def multiplication(x, y):
		mult = x * y
		print(mult)

	def division(x, y):
		div = x / y
		print(div)


'''''
类的使用，一般先要初始化这个类的实例对象 
然后通过实例对象.方法名称去调用相关的实例方法或者类方法或者静态方法 

'''
# 直接类名.方法来调用
Calculator.multiplication(3, 5)
Calculator.addition(3, 5)
# 少写参数或者不写，会报错 ,比如：calculator.multiplication(3)

""" 
在不同类文件里，需要引入外部类，先实例化类的一个对象，然后调用 
这种情况，等学了导入包之后来介绍 
"""

