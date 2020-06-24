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
        """

        Args:
            pw:Password, used to connect to the database and handle exceptions.
        """
        try:
            self.__database_name = 'job_search'
            self.__db = sql.connect(
                'localhost',
                'root',
                pw,
                self.__database_name
            )
            self.__cursor = self.__db.cursor()
            self.__default_table = 'pythondeveloperjob'
            self.__defalut_struct = {
                'id': (int, 0),
                'JobTitle': (str, 255),
                'CompanyName': (str, 255),
                'WorkPosition': (str, 255),
                'Salary': (float, 20),
                'PublishTime': (str, 255)
            }
        except Exception as e:
            print('connect failed.')
            traceback.print_exc()
            exit(0)

    def search(self):
        """

        Returns:
            Return the result of traversal search
        """
        try:
            self.__cursor.execute('SELECT * FROM {}'.format(self.__default_table))
            return self.__cursor.fetchall()
        except Exception as e:
            print('search index error')
            traceback.print_exc()
            raise e

    def insert(self, JobTitle, CompanyName, WorkPosition, Salary, PublishTime):
        """

        Args:
            JobTitle:JobTitle.
            CompanyName:CompanyName.
            WorkPosition:WorkPosition.
            Salary:Salary.
            PublishTime:PublishTime.

        Returns:
            Insert a new piece of data into the database.
        """
        try:
            sqltxt = f"INSERT INTO {self.__default_table} " \
                     f"(JobTitle, CompanyName, WorkPosition, Salary, PublishTime)" \
                     f"VALUES ({repr(JobTitle)}, {repr(CompanyName)}, {repr(WorkPosition)}, {repr(Salary)}, {repr(PublishTime)})"
            self.__cursor.execute(sqltxt)
            self.__db.commit()
        except Exception as e:
            print('Syntax error in sqltxt.')
            traceback.print_exc()
            return

    def real_delete(self, id_):
        """

        Args:
            id_: Flag to delete the corresponding row of the database.

        Returns:
            Delete the corresponding row indicated by the database tag.
        """
        try:
            self.__cursor.execute('DELETE FROM {} WHERE id={}'.format(self.__default_table, repr(id_)))
            self.__db.commit()
        except Exception as e:
            print('real_delete error.')
            traceback.print_exc()
            return

    def exit(self):
        """

        Returns:
            Close database and cursor, disconnect.
        """
        try:
            self.__cursor.close()
            self.__db.close()
        except Exception as e:
            print('exit error.')
            traceback.print_exc()
        finally:
            exit(0)

    def alter_id(self):
        """

        Returns:
            After clearing the list, the primary key ID automatically increases to zero.
        """
        try:
            self.__cursor.execute('alter table {} AUTO_INCREMENT=1;'.format(self.__default_table))
            self.__db.commit()
        except:
            traceback.print_exc()


def chart_clear(sql: SQL):
    """

    Args:
        sql: The self constructed database class using pymysql.

    Returns:
        Clear default database.
    """
    for i in sql.search():
        sql.real_delete(i[0])




