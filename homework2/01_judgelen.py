# -*- encoding: utf-8 -*-
'''
@File : 01_judgelen.py
@Time : 2020/03/13 11:20:46
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。

def judgelen(a, m):
    if m == 1:
        return len(a)
    else:
        return len(a.split())


x = input("请选择输入类型(1、字符串 2、列表 3、 元组)")
if x == '1':
    y = input("请输入字符串：")
elif x == '2':
    y = input("请输入列表，空格隔开：")
elif x == '3':
    y = input("请输入元组，空格隔开：")
else:
    print("输入错误！")
l = judgelen(y,int(x))
print("长度为：%d"  %(l))