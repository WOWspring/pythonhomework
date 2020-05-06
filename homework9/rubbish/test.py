# -*- encoding: utf-8 -*-
'''
@File : test.py
@Time : 2020/05/05 16:47:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

from socket import *

s = socket(AF_INET, SOCK_STREAM)
print(type(s))
t = s.accept(('0.0.0.0', 9999))
print(type(t))