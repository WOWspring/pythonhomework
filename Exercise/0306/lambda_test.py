# -*- encoding: utf-8 -*-
'''
@File : lambda.py
@Time : 2020/03/22 10:24:33
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# lambda表达式练习，重难点

num = [x for x in range(1, 21)]
x = filter(lambda x: x % 2 == 0, num)  #重点
print("0-20之间的偶数", list(x))
