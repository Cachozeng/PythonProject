# 常见的一些常识问题汇总

# !/user/bin/python
# 这个是linux下python文件的写法，告诉程序，这个文件是python去运行，而不是shell去运行

# 下面这个例子


def max(a, b):
	if a > b:
		print(a)
	else:
		print(b)

if __name__ == '__main__':
	print('main method')

max(3,5)

''''' 
上面__main__的含义： 
意思就是说让你写的脚本模块既可以导入到别的模块中用，另外该模块自己也可执行 
如果你不写if __name__ == '__main__':,那么这个代码中的max（）方法只能被 
别的类导入后，进行调用，但是不能被该模块自己执行max() 
先尝试了解下，接下来介绍模块的导入，你可以试试练习，体会下 

'''

# 函数中使用pass


def fuc():
	pass
	# 这里的pass就是TBD的意思，待定，暂时不知道如何实现这个方法，写上pass，程序就不会报错