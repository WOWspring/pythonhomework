# -*- encoding: utf-8 -*-
'''
@File : read_and_sort.py
@Time : 2020/03/22 10:53:27
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 练习4 读取score.txt文件中的内容
# 对分数进行降序排序后
# 打印并输出到另一个文件sorted.txt中
import os

os.chdir('Exercise/0318')

scorelist = []
with open('stuinfo.txt', 'r', encoding='utf-8') as s:
    title = s.readline()  # 读取标题
    nexts = s.readline()    #类似java的读取
    while len(nexts) > 0:
        scorelist.append(nexts)
        nexts = s.readline()
#print(scorelist)

with open('sortedstuinfo.txt', 'w', encoding='utf-8') as ss:
    scorelist.sort(key=lambda x: x.split()[2])

    print(title, end='')  #读取的文件中有\n
    ss.write(title)
    # 打印成绩
    for item in scorelist:
        print(item, end='')
    ss.writelines(scorelist)
