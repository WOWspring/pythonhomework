# -*- encoding: utf-8 -*-
'''
@File : 02_getinfo.py
@Time : 2020/05/05 18:33:01
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 2 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；

'''
OSError: [WinError 10049] 在其上下文中，该请求的地址无效。
解决：connect中的地址为空
存疑：udp的时候为什么可以。。

ConnectionRefusedError: [WinError 10061] 由于目标计算机积极拒绝，无法连接。
解决：ip地址不填127.0.0.1就可以正常执行

'''

import socket

tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_s.connect(('192.168.1.100', 8080))

while True:
    data = tcp_s.recv(1024)
    if not data or data.decode('utf-8') == 'exit':
        break
    print('infomation: %s' % data.decode('utf-8'))

print('Connection is closed!')
tcp_s.close()
