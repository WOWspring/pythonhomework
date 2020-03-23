# -*- encoding: utf-8 -*-
'''
@File : 03_sortstugr.py
@Time : 2020/03/23 16:44:18
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数); 然后按照分数从高到低进行排序输出

import os

try:
    os.chdir("homework3")
except FileNotFoundError as fnf_error:
    print(fnf_error)
    
gradetuple = []
title = ''

try:
    with open("stupythongra.txt", 'r', encoding = 'utf-8' ) as f:
        title = f.readline()    #去掉第一行
        t = f.readline().strip('\n')  #去掉尾部的换行
        while len(t) > 0:
            temp = t.split()
            gradetuple.append((temp[0], temp[1], int(temp[2])))
            t = f.readline().strip('\n')
except FileNotFoundError as fnf_error:
    print(fnf_error)
except IOError:
    print('cannot open ','input.txt')

#print(gradetuple)   #测试检查用
gradetuple.sort(key = lambda x : x[2], reverse = True)
#print(gradetuple)
print(title)
for x in gradetuple:
    print(f"{x[0]}\t{x[1]}\t{x[2]}")

    