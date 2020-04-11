# -*- encoding: utf-8 -*-
'''
@File : 02_declog.py
@Time : 2020/04/11 14:40:07
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#2  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中

import datetime
import functools
import os

try:
    os.chdir('pythonhomework\homework5')
except FileNotFoundError as fuf_err:
    print(fuf_err)

def log():
    def decorater(func):
        @functools.wraps(func)        
        def wrapper(*args, **kw):
            with open('log.txt', 'a+', encoding = 'utf-8') as f:
                f.write('函数{}在{}被调用了,参数是{}{}\n'.format(func.__name__, datetime.datetime.now(), *args, **kw))
                result = func(*args, **kw)
                return result
        return wrapper
    return decorater

@log()
def plus(a, b):
    return a + b
@log()
def minus(a, b):
    return a - b

plus(1,3)
minus(1,8)
plus(2,8)
