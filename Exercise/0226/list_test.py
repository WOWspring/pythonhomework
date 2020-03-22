# -*- encoding: utf-8 -*-
'''
@File : list_test.py
@Time : 2020/03/20 07:54:37
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 列表练习，尝试求列表最大值，最小值，求和，平均值
# 使用for循环计算列表元素和
score = [82, 5, 91, 65, 58, 40, 100, 90, 47, 78]
sum = 0
for i in range(len(score)):
    sum += score[i]

print('最高分:', max(score))
print('最低分:', min(score))
print('总分:', sum)
print('平均分:', sum / len(score))
