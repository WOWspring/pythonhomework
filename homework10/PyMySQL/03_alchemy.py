#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/23 15:26
# @Author  : Ryu
# @Site    : 
# @File    : 03_alchemy.py.py
# @Software: PyCharm

# 3  对2中的表结构，用SQLAchemy模块来实现同样的操作；

# 导入:
from sqlalchemy import Column, String, create_engine,INTEGER, DATETIME
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import functools
import traceback
from datetime import datetime
#创建基类
base = declarative_base()

#定义留言对象
class Message(base):
    '''message类
    定义表类，包括私有变量表名，并且标注了表中的结构
    '''
    __tablename__ = 'messageboard'

    id = Column(INTEGER(), primary_key = True)#标记主键
    content = Column(String(1023))
    user = Column(String(10))
    time = Column(DATETIME())
    is_deleted = Column(INTEGER())


    def chart_print(self):
        '''chart_print
        将对象的属性方法打印成一个可读字符串
        INPUT:None
        OUTPUT:目标字符串
        '''
        return "id:%d,user:%s,content:%s,time:%s" % (self.id, self.user, self.content, self.time)

class Data_Format(object):
    format = {
        'content' : (str, 1023),
        'user' : (str, 10),
        'time' : (str, 19), #暂时如此处理
        'is_deleted' : (int, 1)
    }


def exception_conduct(func):
    '''exception_conduct
    异常处理装饰器，调用装饰器可处理异常
    INPUT: func 目标函数
    OUTPUT: wrapper 装饰函数，函数内部处理异常
    '''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            traceback.print_exc()
        # finally:
#            return wrapper   # 订正，wrapper的返回位置错误
        return result       #   不返回在嵌套函数的时候test容易出现None问题
    return wrapper

def format_proofreading(content = None, user = None, time = None):
    '''format_proofreading
     用于检查message类是否格式规范，三者参数默认值均为None
     INPUT: content 留言内容
            user    用户
            time    时间
    OUTPUT:无返回值，对于格式不符合规范的抛出异常
    '''
    try:
        if content != None:
            assert isinstance(Data_Format.format['content'][0], content)
            assert len(content) <= Data_Format.format['content'][1]
        if user != None:
            assert isinstance(Data_Format.format['user'][0], user)
            assert len(user) <= Data_Format.format['user'][1]
        if time != None:
            assert isinstance(Data_Format.format['time'][0], time)
            assert len(time) <= Data_Format.format['time'][1]
    except Exception as e:
        traceback.print_exc()

class Sqlal(object):
    '''Sqlal类
    通过sqlalchemy来完成数据库操作
    __init__    初始化，链接数据库
    insert_chart    添加新的留言记录
    delete_chart    is_deleted置1，逻辑删除
    physicaldelete_chart    利用sql语句删除，物理删除
    update_chart    更新留言内容
    search_chart    查找留言记录,根据输入参数决定不同搜索功能
    clear_chart     清空表格
    close_connect   断开连接，关闭数据库
    '''
    def __init__(self, pw):
        '''__init__方法
        初始化，利用sqlalchemy链接数据库
        INPUT: pw   数据库密码
        OUTPUT:无返回值，连接数据库，db等变量均为实例对象
        '''
        self.__table_name = Message.__tablename__
        DB_Url = 'mysql+pymysql://root:' + pw + "@localhost:3306/test"
        self.__engine = create_engine(DB_Url)
        self.__DBSession = sessionmaker(bind = self.__engine)
        self.__session = self.__DBSession()

    @exception_conduct
    def insert_chart(self, content, user):
        '''insert_chart
        利用session添加新的留言记录
        '''
        time = get_time()
        temp = Message(content = content, user = user, time = time, is_deleted = 0)
        self.__session.add(temp)
        self.__session.commit()

    @exception_conduct
    def delete_chart(self, id_):
        '''delete_chart
        根据id_进行逻辑删除，is_deleted置1
        INPUT:id_    数据库中的id
        OUTPUT:无返回值
        '''
        target = self.__session.query(Message).filter(Message.id == id_).first()
        if target == None:
            print('this id does not exist')
        else:
            target.is_deleted = 1
            self.__session.commit()

    @exception_conduct
    def physicaldelete_chart(self, id_ = None):
        '''physicaldelete_chart
        根据id进行物理删除,根据参数不同执行不同功能（id为None时删除所有is_deleted置1的，否则对应id进行物理删除）
        INPUT:id    数据库中的id
        OUTPUT:无返回值
        '''
        if id_ == None:
            target = self.__session.query(Message).filter(Message.is_deleted == 1).all()
            for t in target:
                self.__session.delete(t)
            self.__session.commit()
        else:
            target = self.__session.query(Message).filter(Message.id == id_, Message.is_deleted == 1).first()
            if target == None:
                print('数据库中没有该id或者该id的留言还没有被逻辑删除')
            else:
                self.__session.delete(target)
                self.__session.commit()

    @exception_conduct
    def update_chart(self, id_, upcontent):
        '''update_chart
        更新id_的留言，同步刷新时间
        INPUT:  id_   数据库中的id
                upcontent   更新的留言内容
                uptime      更新同步的时间
        OUTPUT：无返回值
        '''
        uptime = get_time()
        target = self.__session.query(Message).filter(Message.id == id_).first()
        target.content = upcontent
        target.time = uptime
        self.__session.commit()

    @exception_conduct
    def search_chart(self, id_ = None, user = None):
        '''search_chart
        依据id_和name来查找数据库对应数据，当两者输入都为默认值的时候执行遍历
        INPUT:  id_ 数据库中的id
                user    用户名
        OUTPUT: 以列表的形式返回查询结果
        '''
        target = []
        if  isinstance(id_, int):
            target =  self.__session.query(Message).filter(Message.id == id_).all()
        elif  isinstance(user, str):
            target = self.__session.query(Message).filter(Message.user == user).all()
        else:
            target = self.__session.query(Message).all()
        # print(target)
        return target

    @exception_conduct
    def clear_chart(self):
        '''clear_chart
        清空数据库中的记录
        INPUT:None
        OUTPUT:None
        '''
        flag = input('This operation will clear your database chart all, continue?[y/n]')
        if flag == 'y':
            target = self.__session.query(Message).all()
            for t in target:
                self.__session.delete(t)
            self.__session.commit()

    @exception_conduct
    def close_chart(self):
        '''close_chart
        关闭数据库，断开连接
        '''
        self.__session.close()
        print('The connection with database has been closed.')

def get_time():
    '''get_time
    获取当前时间，按照%Y-%m-%d %H:%M:%S格式返回
    INOUT:  无输入参数
    OUTPUT: time 格式为%Y-%m-%d %H:%M:%S
    '''
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    print('程序运行中会有warning提示，是time格式问题，不影响程序本身')
    sqlal = Sqlal(input('Please input your password to conduct your database:'))
    sqlal.clear_chart()       #'NoneType' object is not callable
    sqlal.insert_chart('This is great!', 'Superman')
    sqlal.insert_chart('I\'am Batman', 'Batman' )
    sqlal.insert_chart('You have failed this city.', 'Arrow')
    sqlal.delete_chart(int(input('Please input the id of message that you want to delete:')))
    sqlal.update_chart(41,'try update_chart function')
    temp = sqlal.search_chart(user = 'Arrow')
    #print(sqlal.search_chart())
    for t in temp:
        t : Message
        print(t.chart_print())
    # test
    # sqlal.search_chart()
    sqlal.close_chart()

