# -*- encoding: utf-8 -*-
'''
@File : sorted.py
@Time : 2020/03/22 10:31:31
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


# sort等不同排序方式的实验，菜鸟教程
from random import randint


def printScore(score):
    print("      学号     成绩")
    print("-------------------")
    for n, s in score:
        print("%12s %5d" % (n, s))


scoreslist = [( str(i), randint(50, 100)) for i in range(20)]
# 使用lambda表达式指定key
sortedlist = sorted(scoreslist, key=lambda x: x[1])
print("原成绩列表:")
printScore(scoreslist)
print("降序排列后的成绩:")
printScore(sortedlist)
