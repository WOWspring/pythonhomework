# -*- encoding: utf-8 -*-
'''
@File : tcp_sever.py
@Time : 2020/05/05 11:58:34
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

'''
This is the tcp_sever program,
'''
import socket
import time
import threading

def tcplink(sork, addr):
    print('Successfully connect the %s' % addr[0])  #原程序的小修改
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    print('Connection is closed!')
    sock.close()


tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_s.bind(('', 9998))

tcp_s.listen(5)

print('Welcome to connection!')


while True:
    sock, addr = tcp_s.accept()
    print(sock)
    print(addr)
    t = threading.Thread(target = tcplink, args = (sock, addr))
    t.start()


