# -*- encoding: utf-8 -*-
'''
@File : string_test.py
@Time : 2020/03/20 13:04:25
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 定义各种类型的字符串、段落以及转义字符，并进行输出
#尝试单双引号的字符串输出，以及段落形式的输出
a = '这个用的是单引号'
b = "这个用的是双引号"
print(a)
print(b)

c = "换行实验 \n制表符实验 \t\"转义字符实验\""
print(c)

parah = """这是一个段落
        This is a paragraph， tab test
    试验一下敲空格会有什么效果
"""
print(parah)
