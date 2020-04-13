# -*- encoding: utf-8 -*-
'''
@File : 04_stuinfo.py
@Time : 2020/04/12 22:47:03
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
#       封装方法，求单个学生的总分，平均分，以及打印学生的信息。

class student:

    def __init__(self, name, age, sex, CNg, MTg, ENGg):
        '''
        提高封装类的健壮性
        '''
        if not (isinstance(name, str) and isinstance(sex, str)):
            raise Exception('名字和性别应当是字符串！')
        if not (isinstance(age, int) and isinstance(ENGg, int) and isinstance(MTg, int) and isinstance(CNg, int)):
            raise Exception('年龄、成绩都应当是整数！')
        if ENGg < 0 or ENGg > 100 or CNg < 0 or CNg > 100 or MTg > 100 or MTg < 0 or age < 0:
            raise Exception('成绩范围为0-100， 年龄不可能为负！')
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__ENGg = ENGg
        self.__MTg = MTg
        self.__CNg = CNg
    
    def __getsum(self):
        return self.__CNg + self.__ENGg + self.__MTg
    
    def __getagv(self):
        return (self.__CNg + self.__ENGg + self.__MTg) / 3

    def __getinfo(self):
        if self.__sex == 'man':
            print('this student\'s name is {}, who is a {} and {} years old, his Chinese grade is {}, Math grade is {}, English grade is {}.'.format(self.__name, self.__sex, self.__age, self.__CNg, self.__MTg, self.__ENGg))
        else:
            print('this student\'s name is {}, who is a {} and {} years old, her Chinese grade is {}, Math grade is {}, English grade is {}.'.format(self.__name, self.__sex, self.__age, self.__CNg, self.__MTg, self.__ENGg))
           
#各类创建实例的错误实验
# xiaoming = student('小明', -19, 'man', 58, 11, 90)
xiaoming = student('小明', 19, 'man', 58, 11, 90)
print(xiaoming._student__getsum())
xiaoming._student__getinfo()