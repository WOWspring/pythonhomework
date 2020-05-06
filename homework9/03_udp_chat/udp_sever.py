# -*- encoding: utf-8 -*-
'''
@File : udp_sever.py
@Time : 2020/05/05 21:27:18
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 3 编写一个UDP的聊天程序，客户端和服务器端能互相聊天应答；

import socket
import threading

def write(s, addr):
    while True:
        txt = input()
        if txt == 'exit':
            s.close()
            print('Sever is closed')
        else:
            s.sendto(txt.encode('utf-8'), addr)

def read(s):
    while True:
        data, addr = s.recvfrom(1024, 0)
        if data.decode('utf-8') == 'exit':
            s.close()
            print('Sever is closed')
        print('Client : %s' %data.decode('utf-8'))


udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_s.bind(('127.0.0.1', 7777))

temp, addr = udp_s.recvfrom(1024)

th_read = threading.Thread(target = read, args = (udp_s,))
th_read.start()
th_write = threading.Thread(target = write, args = (udp_s, addr))
th_write.start()
