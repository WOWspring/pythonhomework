# -*- encoding: utf-8 -*-
'''
@File : prime.py
@Time : 2020/03/20 22:37:46
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


# 判断数字是否为质数
for i in range(1, 10):
    for j in range(2, i):
        if i % j == 0:
            print("{0} = {1} * {2}".format(i, j, i / j))    #what different is the / and //?
            break
    else:
        print(i, "是质数")
