# -*- encoding: utf-8 -*-
'''
@File : 02_stuclass.py
@Time : 2020/04/12 18:44:47
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 二 定义一个学生Student类。有下面的类属性：
# 1 姓名 name
# 2 年龄 age
# 3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
# 类方法：
# 1 获取学生的姓名：get_name() 返回类型:str
# 2 获取学生的年龄：get_age() 返回类型:int
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
# 写好类以后，可以定义2个同学测试下:

class student:
    name = ''
    age = 0
    score = {
        'Chinese': 0,
        'Math': 0,
        'English': 0
    }

    def __init__(self, name, age, CNgrade, MTgrade, ENGgrade):
        self.name = name
        self.age = age
        self.score['Chinese'] = CNgrade
        self.score['Math'] = MTgrade
        self.score['English'] = ENGgrade

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def get_score(self):
        return self.score[max(self.score, key = self.score.get)]    #max  get 可以取得字典最大键值的键

xiaoming = student('小明', 18, 98, 56, 73)
print(xiaoming.get_age())
print(xiaoming.get_name())
print(xiaoming.get_score())

wangfang = student('王芳', 20, 66, 84, 71)
print(wangfang.get_name())
print(wangfang.get_age())
print(wangfang.get_score())