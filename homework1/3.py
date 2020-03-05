# -*- encoding: utf-8 -*-
'''
@File : 3.py
@Time : 2020/03/05 14:59:30
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#Question:3 定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；
#随机构造
list1 = [2,54,6,2,101,36,4,96,7,9,9,51,3,0,3,12,6,4,6,546,4,56,2,0,.3,2,36,59,685,1,2,0,3,6,8,625,3,2]
list2 = [0,2,1,5,74,99,6,1,00,4,102,96,35,85625,1,5,20,0,5,2,541,225,2,4,86,58,25,412,5,3]
#剔除重复元素，然后利用集合求并集
set1 = set(list1)
set2 = set(list2)
result = set1 & set2 #求并集
print(f"两个列表中的相同元素有： {result}")