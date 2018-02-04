# 练习如何写人文件


#调用buid-in函数：open打开或者创建文件，
#如果exampleFile.txt不存在，就自动创建
#w在这里表示可以写的模式，如果是读那就'r'

#如果你的demo.py文件在桌面，那么exampleFile.txt也会在桌面创建
#如果你要指定到特定路径你可以这样写
#saveFile = open('C:\Users\Anthony\Desktop\exampleFile.txt', 'w')

text = "Sample"
appendText = '\nAppend new line for testing.'

#下面的'a'，就是append的意思,后面讲列表会有append方法介绍
saveFile = open('../Files/exampleFile.txt', 'a')
saveFile.write(appendText)
saveFile.close()
# 操作完文件后一定要记得关闭，释放内存资源

# 练习如何读取文件内容
readMe = open('../Files/exampleFile.txt', 'r').read()
print(readMe)
