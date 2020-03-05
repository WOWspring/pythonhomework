# -*- encoding: utf-8 -*-
'''
@File : 2.py
@Time : 2020/03/05 14:33:45
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
#Question:一个字典中，存放了10个学生的学号（key）和分数（value）；请筛选输出，大于80分的同学（按照格式：学号：分数）；
#学号成绩字典
gradedict = {
    1201:85,
    1202:69,
    1203:63,
    1204:93,
    1205:58,
    1206:76,
    1207:88,
    1208:96,
    1209:35,
    1210:100
}

for key, value in gradedict.items():
    if value > 80:
        print(f"{key}: {value}")