# -*- encoding: utf-8 -*-
'''
@File : 01_geturl.py
@Time : 2020/04/22 16:27:36
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
#    提示，文件有1000行，注意控制每次读取的行数；

import os
import re
from itertools import islice

try:
    os.chdir(r'pythonhomework\homework7')
except FileNotFoundError as fnf_err:
    print(fnf_err)

def change2str(iter):
    temp = ''
    for t in iter:
        temp += t.strip('\n')
    return temp

with open('webspiderUrl.txt', 'r', encoding = 'utf-8') as f:
    with open('newUrl.txt', 'a+', encoding = 'utf-8') as nf:
        rawlist = [100 * i for i in range(10)]
        retxt = r'(http://www\.\w+\.[com,cn,net,org]{1,3})|(http://\d+(.\d+)+)'
        # retxt = r'http://www\.\w+\.[com,cn,net,org]{1,3}'
        # test = r'http'
        # ret = re.compile(retxt)
        for i in rawlist:
        #print(change2str(islice(f, 0, 99)))
        # temp = re.findall(retxt, change2str(islice(f, 0, 0 + 99)))
        # print(temp)
            temp = re.findall(retxt, change2str(islice(f, i, i + 99)))
            for t in temp:
                for x in t:
                    if len(x) >= 10:
                        nf.write(x + '\n')
