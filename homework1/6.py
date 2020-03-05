# -*- encoding: utf-8 -*-
'''
@File : 6.py
@Time : 2020/03/05 16:45:45
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

#Question: 前面2个元素为0，1，输出100以内的斐波那契数列；

#利用列表存数组， 迭代计算
Fibonacci = [0,1]

while Fibonacci[-1] < 100:
    temp = Fibonacci[-1] + Fibonacci[-2]
    if temp > 100:
        break
    else:
        Fibonacci += [temp]

print(f"100以内的斐波那契数列为： {Fibonacci}")
