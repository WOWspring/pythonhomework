# -*- encoding: utf-8 -*-
'''
@File : 01_cmplistdeque.py
@Time : 2020/03/25 15:57:32
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 1 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；
#   用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
#   提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
#   十个元素差值过小，尝试10000个
import datetime
from collections import deque
#定义一个长度为10的列表

bin_list_time = datetime.datetime.now()
mylist = [x for x in range(10000)]
#print(mylist)
mylist.insert(0,-1)
mylist.append(10000)
end_list_time = datetime.datetime.now()

dur_list_time = end_list_time - bin_list_time


bin_deque_time = datetime.datetime.now()
mydeque = deque([x for x in range(10000)])
#print(mydeque)
mydeque.appendleft(-1)
mydeque.append(10000)
end_deque_time = datetime.datetime.now()

dur_deque_time = end_deque_time - bin_deque_time

# print(bin_list_time, end_list_time, dur_list_time)
# print(dur_deque_time)
print("十个元素结论不够明显，将原题的10个元素改为10000个时间差值较为明显")
print(dur_list_time - dur_deque_time)