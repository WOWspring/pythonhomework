# -*- encoding: utf-8 -*-
'''
@File : stringMethod.py
@Time : 2020/03/20 18:37:41
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


# 实验查找子字符串，替换，计算长度等操作
a = 'Hello World'
print(a.index('llo'))
if a.find('llo') > 0:
    print('原字符串中有该字符串')
else:
    print('原字符串中没有该字符串')
print(a.replace('llo', 'ola'))
print(f'\'{a}\' 的长度是', len(a))
