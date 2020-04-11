# -*- encoding: utf-8 -*-
'''
@File : 01_@gettime.py
@Time : 2020/04/08 15:45:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#1  编写一个装饰器，能计算其他函数的运行时间；
import functools
import datetime

def gettime():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            begint = datetime.datetime.now()
            func(*args, **kw)
            endt = datetime.datetime.now()
            return endt - begint
        return wrapper
    return decorator

@gettime()
def plus(a, b):
    sum = 1
    for i in range(a, b):
        sum = sum * i

print(plus(1,2000))