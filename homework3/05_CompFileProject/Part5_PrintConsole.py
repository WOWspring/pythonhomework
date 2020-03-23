# -*- encoding: utf-8 -*-
'''
@File : Part5_PrintConsole.py
@Time : 2020/03/23 22:56:32
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

import os

try:
    os.chdir(r"homework3\05_CompFileProject")
except FileNotFoundError as fnf_error:
    print(fnf_error)

try:
    with open("Blowing in the wind.txt", 'r+', encoding = 'utf-8') as f:
        temp = f.readline()
        while len(temp) > 0:
            print(temp)
            temp = f.readline()
except FileNotFoundError as fnf_error:
    print(fnf_error)