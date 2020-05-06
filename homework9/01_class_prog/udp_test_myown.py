# -*- encoding: utf-8 -*-
'''
@File : udp_test_myown.py
@Time : 2020/05/03 17:43:37
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

address = ('192.168.119.1', 4567)
#端口不能加引号！

s = input('请输入需要发送的内容')

udp_socket.sendto(s.encode('utf-8'), address)

udp_socket.close()