# -*- encoding: utf-8 -*-
'''
@File : 01_counter.py
@Time : 2020/04/03 08:39:55
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

def createCounter():
    a = 0
    def add1():
        nonlocal a      #用于访问外函数变量
        a = a + 1
        return a
    return add1

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')