# -*- encoding: utf-8 -*-
'''
@File : 5.py
@Time : 2020/03/05 16:27:22
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#Question:  使用random模块，生成随机数，来初始化一个列表，元组；
#使用了 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法；

import random

#构造一个20个元素的， 1-50的随机整数列表和元组
randlist = []
randtuple = ()
for i in range(20):
    randlist += [random.randint(1,50)]
    randtuple += (random.randint(1,50),)  # 不可迭代,利用逗号把括号运算符变成元组表示

print(f"随机列表为：{randlist}")
print(f"随机元组为：{randtuple}")