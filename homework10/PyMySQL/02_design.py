#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/18 22:58
# @Author  : Ryu
# @Site    : 
# @File    : 02_design.py.py
# @Software:

# 2  设计一个留言本的表（ID，留言内容，留言人，留言时间，是否删除）（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
#    使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；

# 留言板表头id, content, user, time, is_deleted
# 留言板格式int, varchar(1023), varchar(10), time, int(1)

import pymysql as sql
from datetime import datetime
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
            self.__database_name = 'test'
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
            self.__default_table = 'MessageBoard'
            # 默认表中的数据类型以及最大长度
            self.__defalut_struct = {
                'content': (str, 1023),
                'user': (str, 10),
                'time': (str, 19),
                'is_deleted': (int, 1)
            }
        #异常处理还可以细化，太过宽泛
        except Exception as e:
            print('connect failed.')
            traceback.print_exc()
            exit(0)

    def __check_instance(self, content=None, user=None, time=None):
        '''__check
        用于检查涉及到的参数是否符合数据库要求
        INPUT:  content: 留言内容，type=str, len < 1023
                user: 留言人，type=str, len<10
                time: 留言时间，type=datetime, %Y-%m-%d %H:%M:%S, datetime.getTime()
        OUTPUT: assert触发异常并捕获
        '''
        L = [content, user, time]
        struct_type = ['content', 'user', 'time']
        try:
            for i, k in enumerate(L):
                if k != None:
                    temp = self.__defalut_struct[struct_type[i]]
                    assert isinstance(k, temp[0])
                    assert len(k) <= temp[1]
        except Exception as e:
            # print(data_type[ind])
            print('Invalid data struct. Please check it out.')
            traceback.print_exc()
            raise e

    def insert(self, content, user):
        '''insert
        插入数据的函数，不封装，参数要求完备。is_deleted默认为0，即不可设置
        INPUT:  content 留言内容
                user    用户
                time    留言时间
        OUTPUT: 无返回值，异常处理
        '''
        time = get_time()
        try:
            #检查格式
            self.__check_instance(content, user, time)
        except Exception as e:
            traceback.print_exc()
            return
        try:
            sqltxt = f"INSERT INTO {self.__default_table} " \
                     f"(content, user, time, is_deleted) " \
                     f"VALUES ({repr(content)}, {repr(user)}, {repr(time)}, 0)"
            # 检验测试
            # print(sqltxt)
            self.__cursor.execute(sqltxt)
            self.__db.commit()
        except Exception as e:
            print('Syntax error in sqltxt.')
            traceback.print_exc()
            return

    def delete(self, id_):
        '''delete
        删除函数，依据id来删除对应行，对应数据库为is_deleted置1，未做覆盖操作，可暂时保留数据
        INPUT:  id_  数据库中的对应行
        OUTPUT: 无返回值，异常处理
        '''
        try:
            #检验id类型
            assert isinstance(id_, int)
            self.__cursor.execute('UPDATE {} SET is_deleted=1 WHERE id={}'.format(self.__default_table,repr(id_)))
            self.__db.commit()
        except Exception as e:
            #Exception中可以区分id类型错误还是数据库错误
            print('Delete error.')
            return

    def real_delete(self, id_):
        '''real_delete
        删除目标id以及is_deleted为1的目标行，与delete做拆分提供彻底删除
        INPUT:  id_ 数据库中的对应行
        OUTPUT: 无返回值，异常处理
        '''
        try:
            #检验id类型
            assert isinstance(id_, int)
            self.__cursor.execute('DELETE FROM {} WHERE id={} AND is_deleted=1'.format(self.__default_table, repr(id_)))
            self.__db.commit()
        except Exception as e:
            print('real_delete error.')
            traceback.print_exc()
            return

    def update(self, id_, new_content):
        '''update
        更新数据库中id_对应行的留言内容，修改时同时修改留言最后更新时间
        INPUT:  id_ 数据库中的对应行
                new_content 新的留言内容
        OUTPUT: 无返回值，异常处理
        '''
        try:
            #检查id类型
            assert isinstance(id_, int)
            #获取当前时间
            new_time = get_time()
            #检查content和time的格式是否正确
            self.__check_instance(content=new_content, time=new_time)
            sqltxt = 'UPDATE {} SET content={}, time={} WHERE id={}'.format(self.__default_table,repr(new_content),repr(new_time),id_)
            self.__cursor.execute(sqltxt)
            self.__db.commit()
        except Exception as e:
            print('update error.')
            traceback.print_exc()
            return

    def search(self, id_=None, user=None):
        '''search
        多功能合并:
        id_,user均为defalut则为遍历；
        id_为根据id进行查找
        user为根据user查找
        INPUT:  id  数据库中的对应行
                user    用户名
        OUTPUT: 无返回值，异常处理
        '''
        try:
            # assert (id or user)
            #输出结果按照时间顺序排列
            if id_:
                self.__cursor.execute('SELECT * FROM {} WHERE id={} ORDER BY time DESC'.format(self.__default_table,repr(id)))
            elif user:
                self.__cursor.execute('SELECT * FROM {} WHERE user={} ORDER BY time DESC'.format(self.__default_table,repr(user)))
            else:
                self.__cursor.execute('SELECT * FROM {}'.format(self.__default_table))
            #返回fetchall的结果
            return self.__cursor.fetchall()
            #检查select语句
            # print(f'SELECT * FROM {self.__default_table} WHERE name={repr(user)}')
        except Exception as e:
            print('search index error')
            traceback.print_exc()
            raise e

    def exit(self):
        '''exit
        断开数据库连接，退出程序
        INOUT:  无输入参数
        OUTPUT: 无返回值，异常处理
        '''
        try:
            self.__cursor.close()
            self.__db.close()
            print('The connection with database has been closed.')
        except Exception as e:
            print('exit error.')
            traceback.print_exc()
        finally:
            exit(0)

def get_time():
    '''get_time
    获取当前时间，按照%Y-%m-%d %H:%M:%S格式返回
    INOUT:  无输入参数
    OUTPUT: time 格式为%Y-%m-%d %H:%M:%S
    '''
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def chart_clear(sql:SQL):
    '''chart_clear
    清空sql中对应的表格数据
    INPUT:  sql SQL 连接SQL中制定的表格
    OUTPUT: 无返回值，
    '''
    flag = input('You are trying to clear the whole chart,and this handle is irreversible. Want to continue?(y/n)')
    if flag == 'n':
        return
    elif flag == 'y':
        for i in sql.search():
            sql.delete(i[0])
            sql.real_delete(i[0])
        print('The chart has been cleared.')
    else:
        print('Input error: acceptable input is y or n.')

if __name__ == '__main__':
    pw = input('Please input a password: ')
    sql = SQL(pw)
    #检查清空使用
    chart_clear(sql)
    sql.insert('My name is David.', 'David')
    sql.insert('CR is the best game in the world!', 'JACK')
    sql.insert('I\'m new in here.Hello everyone.' , 'WOWspring')
    sql.insert('AHHHH', 'JACK')

    JACKlist =  sql.search(user='JACK')
    print(JACKlist)
    for l in JACKlist:
        sql.delete(l[0])

    update_test_list = sql.search(user='David')
    sql.update(update_test_list[0][0], 'trying the change')
    sql.exit()