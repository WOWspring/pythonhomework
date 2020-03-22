# -*- encoding: utf-8 -*-
'''
@File : setDef.py
@Time : 2020/03/20 22:24:28
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 使用两种方式创建集合，并进行相应操作 ,观察集合的性质
set1 = {2, 4, 6}
set2 = set("WOW")
print(set1)
print(set2)
print(set1 | set2)

set2.discard('W')
print(set2)
