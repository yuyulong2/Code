# -*-coding:utf-8-*-

# 输入
# python提供了两个内置函数从标准输入读入（键盘）一行文本
# in_1 = input("请输入1")
# raw_input 没用了
# input函数可以接受一个python表达式作为输入
# in_2 = input("请输入一个函数:") #也没有用了
# print(in_2)

#打开和关闭文件
# file object = open(file_name [, access_mode][, buffering])
fo = open('tianyancha.txt','w')
fo.write("www.ranoob.com")
fo.close()


