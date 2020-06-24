#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 17:43
# @Author  : Ryu
# @Site    : 
# @File    : jobsql.py.py
# @Software: PyCharm

import pymysql as sql
import traceback


class SQL(object):
    def __init__(self, pw):
        '''__init__初始化
        确认密码之后初始化connect和cursor，执行SQL语句
        INPUT： pw 密码，用于连接数据库，做异常处理
        OUTPUT: 无返回值
        '''
        try:
            # 数据库名
            self.__database_name = 'job_search'
            # connect对象
            self.__db = sql.connect(
                'localhost',
                'root',
                pw,
                self.__database_name
            )
            # 创建cursor，用于执行后续的SQL语句
            self.__cursor = self.__db.cursor()
            # 数据库中默认的操作表
            self.__default_table = 'pythondeveloperjob'
            # 默认表中的数据类型以及最大长度
            self.__defalut_struct = {
                'id': (int, 0),
                'JobTitle': (str, 255),
                'CompanyName': (str, 255),
                'WorkPosition': (str, 255),
                'Salary': (float, 20),
                'PublishTime': (str, 255)
            }
        #异常处理还可以细化，太过宽泛
        except Exception as e:
            print('connect failed.')
            traceback.print_exc()
            exit(0)

    def search(self):
        try:
            self.__cursor.execute('SELECT * FROM {}'.format(self.__default_table))
            return self.__cursor.fetchall()
        except Exception as e:
            print('search index error')
            traceback.print_exc()
            raise e

    def insert(self, JobTitle, CompanyName, WorkPosition, Salary, PublishTime):
        try:
            sqltxt = f"INSERT INTO {self.__default_table} " \
                     f"(JobTitle, CompanyName, WorkPosition, Salary, PublishTime)" \
                     f"VALUES ({repr(JobTitle)}, {repr(CompanyName)}, {repr(WorkPosition)}, {repr(Salary)}, {repr(PublishTime)})"
            # 检验测试
            print(sqltxt)
            self.__cursor.execute(sqltxt)
            self.__db.commit()
        except Exception as e:
            print('Syntax error in sqltxt.')
            traceback.print_exc()
            return

    def real_delete(self, id_):
        try:
            self.__cursor.execute('DELETE FROM {} WHERE id={}'.format(self.__default_table, repr(id_)))
            self.__db.commit()
        except Exception as e:
            print('real_delete error.')
            traceback.print_exc()
            return

    def exit(self):
        try:
            self.__cursor.close()
            self.__db.close()
        except Exception as e:
            print('exit error.')
            traceback.print_exc()
        finally:
            exit(0)

    # def alter_id(self):
    #     try:
    #         self.__cursor.execute('alter table {} AUTO_INCREMENT=1;'.format(self.__default_table))
    #         self.__db.commit()
    #     except:
    #         traceback.print_exc()


def chart_clear(sql: SQL):
    for i in sql.search():
        sql.real_delete(i[0])




