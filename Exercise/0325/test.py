# -*- encoding: utf-8 -*-
'''
@File : test.py
@Time : 2020/03/25 08:33:37
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


from collections import namedtuple

a = namedtuple('Point', ['x','y'])

x = a(1,2)

print(x.x)