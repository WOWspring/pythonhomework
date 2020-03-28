# -*- encoding: utf-8 -*-
'''
@File : 08_countip.py
@Time : 2020/03/27 17:53:16
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 8 京东二面笔试题
# 1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
# 2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip

import random
import os

try:
    os.chdir(r'pythonhomework\homework4')
except FileNotFoundError as fnf_error:
    print(fnf_error)

#生成文件
with open('ip.txt', 'w', encoding = 'utf-8') as f:
    for i in range(1200):
        enddex = random.randint(1,254)
        tempip = '172.25.254.' + str(enddex)
        f.writelines(tempip + '\n')

#读取文件，统计频率
countlist = []
temp = []
with open('ip.txt', 'r', encoding = 'utf-8') as f:
    temp = f.readlines()
    for i in temp:
        i.strip('\n')
countlist = [(i, temp.count(i))for i in set(temp)]

#找前十大的数字，新做法，找到一个最大的，删掉一个
for i in range(10):
    ip = ''
    max = 0
    for j in countlist:
        if j[1] > max:
            max = j[1]
            ip = j[0].strip('\n')
    print(f'{ip}出现的次数为{max}')
    temp = [ip + '\n', max]         #拼接回去
    countlist.remove(tuple(temp))
