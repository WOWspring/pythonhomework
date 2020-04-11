# -*- encoding: utf-8 -*-
'''
@File : 04_allkinddec.py
@Time : 2020/04/11 21:40:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

import functools

def npnr(func):
    @functools.wraps(func)
    def wrapper():
        print('npnr，没有参数，没有返回值的装饰器')
        func()
        print('调用结束')
        return
    return wrapper

def nphr(func):
    @functools.wraps(func)
    def wrapper():
        print('nphr，没有参数，有返回值的装饰器')
        result = func()
        print('调用结束')
        return result
    return wrapper

def hphr(func):
    @functools.wraps(func)
    def wrapper(*args, **kws):
        print('hphr，有参数，有返回值的装饰器')
        result = func(*args, **kws)
        print('调用结束')
        return result       
    return wrapper

def isprime(n):
    '''
    判断输入是否为质数
    '''
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    else:
        return True

@npnr
def p2000():
    for i in range(1,2001):
        if isprime(i):
            print('{}'.format(i), end = '\t')
    else:
        print('\n')

@nphr
def count():
    count = 0
    for i in range(2, 10001):
        if isprime(i):
            count += 1
    return count

@hphr
def countp(m):
    count = 0
    for i in range(2, m + 1):
        if isprime(i):
            count += 1
    return count

p2000()
print(count())
print(countp(20))