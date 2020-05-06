# -*- encoding: utf-8 -*-
'''
@File : tcp_client.py
@Time : 2020/05/05 16:55:54
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

import socket

tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_s.connect(('127.0.0.1', 9998))

print(tcp_s.recv(1024).decode('utf-8'))

for data in [b'A', b'B', b'C']:
    tcp_s.send(data)
    print(tcp_s.recv(1024).decode('utf-8'))
tcp_s.send(b'exit')
tcp_s.close()