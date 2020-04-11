# -*- encoding: utf-8 -*-
'''
@File : 01_calculater.py
@Time : 2020/04/01 08:34:14
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def muti(a, b):
    return a * b

def divi(a, b):
    return a / b

def calculate(a, b, func):
    print(func(a, b))

a, t, b = input("请输入表达式：").split()
a = int(a)
b = int(b)
if t == '+':
    calculate(a, b, plus)
elif t == '-':
    calculate(a, b, minus)
elif t == '*':
    calculate(a, b, muti)
elif t == '/':
    calculate(a, b, divi)
else:
    print('表达式错误！')