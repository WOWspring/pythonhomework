# -*- encoding: utf-8 -*-
'''
@File : 02_getsum.py
@Time : 2020/03/13 19:03:09
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

target = map(int, input("请输入要求和的n个数：").split())
print("求和的结果为：%d" %sum(target))