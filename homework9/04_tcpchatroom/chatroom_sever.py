# -*- encoding: utf-8 -*-
'''
@File : chatroom_sever.py
@Time : 2020/05/06 17:20:51
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib


'''
服务器负责和各个客户端链接，并且代为转发各个客户端的消息
'''
import os
import socket
import threading
import severaddr
import datetime
from get_time import get_time

#服务器写成一个类会比较好

class ChatSever:

    def __init__(self):
        #服务器终端的socket套接字
        self.tcp_termin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #初始化一个成员字典，用于记录客户端的信息
        self.members = {}
        #先把端口信息保存了
        self.addr = severaddr.addr


    def start_sever(self):
        #添加异常处理
        try:
            self.tcp_termin.bind(self.addr)
        except Exception as e:
            print(e)
        #设定监听的端口数量为6
        self.tcp_termin.listen(6)
        print('多人聊天室服务器终端开启……')
        print('输入dir查看当前聊天室的成员信息，输入exit终止服务')

        #开始死循环监听
        self.sever_accept()

    def sever_accept(self):
        x = threading.Thread(target = self.input_order)
        x.start()
        while True:
            sock, addr = self.tcp_termin.accept()
            self.members[addr] = sock
            print('用户{}加入聊天室！当前共有{}名成员'.format(addr, len(self.members)))
            t = threading.Thread(target =self.recv_send, args = (sock, addr))
            t.start()
    
    def recv_send(self, sock, addr):
        while True:
            try:            
                data = sock.recv(1024)
                message = '{}  {} : \n{}'.format(get_time(), addr, data.decode('utf-8'))
                #服务器接收到数据之后，再发给各个客户端
                for client in self.members.values():
                    client.send(message.encode('utf-8'))
            except ConnectionResetError:
                print('用户{}退出聊天。'.format(addr))
                self.members.pop(addr)
                #退出循环
                break

    def dirmembers(self):
        print(self.members)

    def stop_sever(self):
        #关闭各个客户端的socket
        for client in self.members.values():
            client.close()
        #服务器关闭
        self.tcp_termin.close()
        print('通讯结束！')
        os._exit(0)

    def input_order(self):
        while True:
            term = input()
            if term == 'dir':
                self.dirmembers()
            elif term == 'exit':
                self.stop_sever()
            else:
                print('命令无效')

if __name__ == '__main__':    
    chat_sever = ChatSever()
    chat_sever.start_sever()
    while True:
        term = input()
        if term == 'dir':
            chat_sever.dirmembers()
        elif term == 'exit':
            chat_sever.stop_sever()
        else:
            print('命令无效')
