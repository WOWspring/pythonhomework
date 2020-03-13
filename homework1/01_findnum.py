# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/03/05 11:44:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#Question：元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；
#练习要点， 生成0到50这些数的列表:尝试列表解析式，for循环的两种赋值以及list（range）
# numlist = [i for i in range(0,51)]
# numlist = []
# for i in range(0, 51):
#     numlist += [i]
# numlist= []
# for i in range(0,51):
#     numlist.append(i)
#全数列表
numlist = list(range(0,51))
#奇数列表
odd = list(range(1,51,2))
print(f"0-50中的奇数有{odd}")
#偶数列表
even = list(range(0,51,2))
print(f"0-50中的偶数有{even}")
#质数列表
prime = []
for i in range(2,51):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime.append(i)
print(f"0-50的质数有{prime}")
#同时被23整除的列表
mutilist = []
for i in range(0,51):
    if i % 2 == 0 and i % 3 == 0:
        mutilist += [i]
print(f"0-50中同时被2、3整除的列表有{mutilist}")