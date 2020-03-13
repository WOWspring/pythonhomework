# -*- encoding: utf-8 -*-
'''
@File : 06_Fibonacci.py
@Time : 2020/03/13 23:24:22
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#定义一个函数, 打印输出n以内的斐波那契数列;

def Fibonacci(n):
    a = 0
    b = 1
    print(f"{a}", end = ' ')
    while b < n:
        print(f"{b}", end = ' ')
        b,a = b + a, b

num = input("请输入n的值：")
Fibonacci(int(num))