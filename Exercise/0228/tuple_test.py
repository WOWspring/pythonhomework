# -*- encoding: utf-8 -*-
'''
@File : tupleDef.py
@Time : 2020/03/20 22:31:48
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 定义元组，并进行相关操作
data = (100, 865, 6, 79)
print(data + (88, 77, 'str'))
print(data * 3)
print("最大值:", max(data))
print("最小值:", min(data))
print("for循环输出:")
for x in data:
    print(x)
