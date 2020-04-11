# -*- encoding: utf-8 -*-
'''
@File : 02_reduce.py
@Time : 2020/04/01 08:49:15
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#reduce可以轻松实现阶乘
from functools import reduce

print(reduce(lambda X, Y: X * Y, range(1, 6)))