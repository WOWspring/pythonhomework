# -*- encoding: utf-8 -*-
'''
@File : 01_input.py
@Time : 2020/03/23 16:31:26
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


#1 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；

import os

try:
    os.chdir("homework3")
except FileNotFoundError as fnf_error:
    print(fnf_error)

txtlist = []
temp = input("请输入字符串，以空行为结束：")
while len(temp) > 0:
    txtlist.append(temp)
    temp = input("请输入字符串，以空行为结束：")

try:
    with open("input.txt", 'w', encoding = 'utf-8') as f:
        for t in txtlist:
            f.writelines(t + '\n')
except FileNotFoundError as fnf_error:
    print(fnf_error)
except IOError:
    print('cannot open ','input.txt')
