# -*- encoding: utf-8 -*-
'''
@File : 03_randodd.py
@Time : 2020/03/13 19:14:18
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#编写一个函数, 传入一个数字列表, 输出列表中的奇数;
#   数字列表请用随机数函数生成;
import random

def inputodd(a):
    temp = []
    for i in range(len(a)):
        if a[i] % 2 == 1:
            temp += [a[i],] 
    print(f"列表中的奇数有：{temp}")


listlen = 20  #列表长度
randlist = [random.randint(1,100) for i in range(listlen)]
print(f"原列表为：{randlist}")
inputodd(randlist)