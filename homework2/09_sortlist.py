# -*- encoding: utf-8 -*-
'''
@File : 09_sortlist.py
@Time : 2020/03/14 00:01:48
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);

def sortlist(m):
    m.sort()

mylist = list(map(int, input("请输入数组:").split()))
print(f"原数组为：{mylist}")
sortlist(mylist)
print(f"从小到大排序后的数组为：{mylist}")