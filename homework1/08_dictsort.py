# -*- encoding: utf-8 -*-
'''
@File : 8.py
@Time : 2020/03/05 17:23:17
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# Question:设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资；  
# 将这10个员工，按照工资从高到低打印输出；
#    提示：可以组合使用我们的序列数据类型；

#列表排序可能较为容易， 每个员工以一条字典数据存储
StuffList = [
    {'snumber': 1201, 'sname': "周依", 'sage': 3,'ssalary': 2000},
    {'snumber': 1202, 'sname': "肖二", 'sage': 2,'ssalary': 2500},
    {'snumber': 1203, 'sname': "张三", 'sage': 4,'ssalary': 3000},
    {'snumber': 1204, 'sname': "李四", 'sage': 1,'ssalary': 1500},
    {'snumber': 1205, 'sname': "王五", 'sage': 6,'ssalary': 9500},
    {'snumber': 1206, 'sname': "燕六", 'sage': 2,'ssalary': 6400},
    {'snumber': 1207, 'sname': "彩期", 'sage': 4,'ssalary': 3300},
    {'snumber': 1208, 'sname': "吴霸", 'sage': 1,'ssalary': 800},
    {'snumber': 1209, 'sname': "黄玖", 'sage': 2,'ssalary': 5400},
    {'snumber': 1210, 'sname': "钱拾", 'sage': 3,'ssalary': 2900}
]

SortedStuffList = sorted(StuffList, key = lambda i: i['ssalary'], reverse = True)#按照工资降序排列   存疑，不太懂lambda表达式的用法
#每一个员工输出一行， 保证美观
for i in range(10):
    print(SortedStuffList[i])