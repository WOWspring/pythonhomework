# -*- encoding: utf-8 -*-
'''
@File : 06_stupygrade.py
@Time : 2020/04/13 22:01:38
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 六  用面向对象,实现一个学生Python成绩管理系统;
#       学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
#       实现对学生信息及成绩的增,删,改,查方法;

import os

class py_gra_arr:

    def __init__(self):
        try:
            os.chdir(r'pythonhomework\homework6\06_pygra')
        except FileNotFoundError as identifier:
            print(identifier)

        self.__geainfo = []
        with open('stugra.txt', 'r', encoding = 'utf-8') as f:
            title = f.readline().strip('\n').split()
            txt = f.readline().strip('\n').split()
            while(len(txt) != 0):
                temp = {}
                for i, k in enumerate(txt):
                    if i == 2:    
                        temp[title[i]] = txt[i]
                    else:
                        temp[title[i]] = int(txt[i])
                self.__geainfo.append(temp)
                txt = f.readline().strip('\n').split()
    
    def display(self):
        for i in self.__geainfo:
            print(i)
        
    def add_stu_info(self, banji, number, name, grade):
        if not(isinstance(banji, int) or isinstance(number, int) or isinstance(name, str) or isinstance(grade, int)):
            raise Exception('输入数据格式有误！')
        temp = {
            '班级': banji,
            '学号': number,
            '姓名': name,
            '成绩': grade
        }
        with open('stugra.txt', 'a+', encoding = 'utf-8') as f:
            print(f'{banji}\t{number}\t{name}\t{grade}')
            #f.write(f'{banji}\t{number}\t{name}\t{grade}\n') 存疑
            f.write(f'\n{banji}  {number}  {name}  {grade}\n') 
        with open('stugra.txt', 'r', encoding = 'utf-8') as f:
            lines = f.readlines()
            print(lines)
        self.__geainfo.append(temp)

    def del_stu_info(self, banji, number):
        if not(isinstance(banji, int) or isinstance(number, int)):
            raise Exception('输入格式有误！')
        for i, k in enumerate(self.__geainfo):
            if k['班级'] == banji and k['学号'] == number:
                del self.__geainfo[i]
                lines = []
                # with open('stugra.txt', 'r', encoding = 'utf-8') as f:
                #     with open('stugra.txt', 'r+', encoding = 'utf-8') as g:
                #         for t in f.readlines():
                #             temp = t.strip('\n').split()
                #             print(temp)
                #             if len(temp) == 0:
                #                 pass
                #             elif temp[0] == '班级':
                #                 g.write(t)
                #             elif int(temp[0]) == banji and int(temp[1]) == number:
                #                 pass
                #             else:
                #                 g.write(t) 
                with open('stugra.txt', 'r', encoding = 'utf-8') as f:
                    lines = f.readlines()
                
                print(lines)
                
                with open('stugra.txt', 'w', encoding = 'utf-8') as f:
                    for t in lines:
                        temp = t.strip('\n').split()
                        if len(temp) == 0:
                            pass
                        elif temp[0] == '班级':
                            f.write(t)
                        elif int(temp[0]) == banji and int(temp[1]) == number:
                            continue
                        else:
                            f.write(t)
                break
        else:
            print('没有匹配的成绩数据，删除失败！')

    def update_grade(self, banji, number, grade):
        if not(isinstance(banji, int) or isinstance(number, int)):
            raise Exception('输入格式有误！')
        for i, k in enumerate(self.__geainfo):
            if k['班级'] == banji and k['学号'] == number:
                self.__geainfo[i]['成绩'] = grade
                with open('stugra.txt', 'r', encoding = 'utf-8') as f:
                    lines = f.readlines()
                
                print(lines)
                
                with open('stugra.txt', 'w', encoding = 'utf-8') as f:
                    for t in lines:
                        temp = t.strip('\n').split()
                        if len(temp) == 0:
                            pass
                        elif temp[0] == '班级':
                            f.write(t)
                        elif int(temp[0]) == banji and int(temp[1]) == number:
                            f.write('{}  {}  {}  {}\n'.format(banji, number, temp[2], grade))
                        else:
                            f.write(t)
                break
        else:
            print('没有匹配的成绩数据，更新失败！')        

    def search_info(self, banji, number):
        if not(isinstance(banji, int) or isinstance(number, int)):
            raise Exception('输入格式有误！')
        for i, k in enumerate(self.__geainfo):
            if k['班级'] == banji and k['学号'] == number:
                print(self.__geainfo[i])
                break
        else:
            print('没有匹配的成绩数据，查找失败！')

PGA = py_gra_arr()
PGA.display()
PGA.add_stu_info(1807, 23, '谢渊博', 55)
PGA.del_stu_info(1801, 8)
PGA.update_grade(1802, 1, 88)
PGA.search_info(1803, 18)
