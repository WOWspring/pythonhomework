# -*- encoding: utf-8 -*-
'''
@File : 02_decoratertest.py
@Time : 2020/04/03 09:39:55
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

def log(text):
    def decorator(func):
        def wrapper(*argv, **kwrags):
            print(text)
            res = func(*argv, **kwrags)
            return res
        return wrapper
    return decorator

@log("加法被执行了")
def plus(a, b):
    return a + b

print(plus(1,3))


