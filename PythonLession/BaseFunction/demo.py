
import time as t

print('hello Python 3')

"""
多行注释
"""
'''
多行注释
'''

print('我喜欢"香蕉"')  # 注释：单引号里是可以写双引号的字符串
print('we\' ar go to shopping.')  # 如果要单引号内使用单引号，需要转义字符\
print("我们发现这个\"地方\"不一样")
print("hi" + "Tom")  # 字符串采用加号连接
# print("Hi" + 5)  # 字符和数字链接报错，提示5必须要是str,不能是int
print("Hi" + str(5))
print(int('8') + 5)  # 字符可以强制转型int
print(float('8.5') + 5)  # 单精度，这里不能用Int

# 指数
print(4 ** 4)

# 变量可以是数字
var1 = 5
print(var1)

# 变量可以是字符
var2 = 'hello'
print(var2)

# 变量可以是运算表达式
var3 = 5 + 67
print(var3)

# 变量可以是函数
var4 = print('hello Python 3')

# 打印10以内的自然数
condition = 1
while condition < 10:
    print(condition)
    condition += 1  # 相当于 condition = condition + 1

# 打印1到9：写入列表
exampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for eachNumber in exampleList:
    print(eachNumber)

# 打印1到9：自带函数rang()
for i in range(1, 10):
    print(i)

# 这里介绍 if语句
x = 5
y = 8
z = 4
s = 5

if x < y:
    print('x is less than y')

if x < y > z:
    print('x is less than y and greater than z')

if x <= s:
    print('x is less than or equal to s')

if x > y:
    print('x is greater than y')
else:
    print('x is not greater than y')

if x > y:
    print('x is greater than y')
elif x < z:
    print('x is less than z')
else:
    print('上面的if 和elfi 语句都不会被执行的时候，才会到这里执行代码')

""" 
用关键字def开表示声明一个函数，格式如下 
def functionName(var1,var2): 
    代码块 
"""


def example():
    print('basic function example.')
    z = 3 + 9
    print(z)

example()  # 调用函数

''''' 
全局变量：在当前.py文件内，都随意地方都可以调用，例如函数内部调用全局变量 
局部变量：局部变量一般定义在函数体内部，只能当前这个函数调用，超过这个范围，其他无权访问 
这个局部变量 
'''
x = 6


def printFuc():
    y1 = 8
    z = 9
    print(y1 + z)
    print(x)  # 函数内部可以调用局部变量


printFuc()
# print(y1)  #提示y没有定义，这个地方调用局部变量会报错

x = input('What is your name?')
print('Hello',x)

#获取当前时间
timenow = t.localtime()
print(t.strftime('%Y-%m-%d %H:%M:%S',timenow))