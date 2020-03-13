# -*- encoding: utf-8 -*-
'''
@File : 01_caculate.py
@Time : 2020/03/14 00:08:05
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#编写一个函数cacluate, 可以实现2个数的运算(加,减 乘,除)

def caculate(a,b,operator):
    a = int(a)
    b = int(b)
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b

temp = input("请输入两个元素的运算表达式:").split()
print(f"运算结果是：{temp[0]} {temp[1]} {temp[2]} = {caculate(temp[0], temp[2], temp[1])}")
