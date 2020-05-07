# -*- encoding: utf-8 -*-
'''
@File : chatroom_client.py
@Time : 2020/05/07 14:38:04
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

import socket
import severaddr
import os
import threading

chat_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
chat_client.connect(severaddr.addr)


def recive_message():
    #成功打开线程之后在终端回复文字表明链接成功
    print('接受线程开启，正确。可以接受消息')
    while True:

        try:  
            result = chat_client.recv(1024)
            print(result.decode('utf-8'))          
        except ConnectionResetError:
            print('服务器被关闭，通信结束。')
            chat_client.close()
            #退出循环
            break
    os._exit(0)

def write_message():
    #成功打开线程之后在终端回复文字表明链接成功
    print('发送线程开启，正确。可以发送消息')
    print('输入文字后回车发送消息，exit退出聊天')
    while True:
        result = input()
        if result == 'exit':
            print('您退出了聊天')
            chat_client.close()
            break
        else:
            chat_client.send(result.encode('utf-8'))
    os._exit(0)

client_thread = [threading.Thread(target = recive_message), threading.Thread(target = write_message)]

for t in client_thread:
    t.start()