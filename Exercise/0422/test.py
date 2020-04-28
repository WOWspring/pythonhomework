# -*- encoding: utf-8 -*-
'''
@File : test.py
@Time : 2020/04/22 09:27:17
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

here put the import lib

from multiprocessing import Process
name = [11,22]

def a():
        print(name)
        name.append(5)
        print(name)

# def b()
if  __name__ == "__main__":    
    x = Process(target = a)
    x.start()

# import re

# retxt = r'http://www\.\w+\.[com,cn,net,org]{1,3}|http://\d+(.\d+)+'
# txt = 'http://61.49.58.131'
# print(re.match(retxt,txt))