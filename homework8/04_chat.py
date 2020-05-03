# -*- encoding: utf-8 -*-
'''
@File : 04_chat.py
@Time : 2020/05/03 10:47:57
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 4 多进程通讯：
#   编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；

from multiprocessing import Process, Queue, Lock
import time


def receive1(Chat_Channel1, mutex):
    #必须使用while True 如果是原来的while not empty的话进程启动之后就跳出循环了
    while True: 
        if not Chat_Channel1.empty():
            mutex.acquire()
            print('process 1 recieve the string: {}'.format(Chat_Channel1.get()))
            mutex.release()

def receive2(Chat_Channel2, mutex):
    while True: 
        if not Chat_Channel2.empty():
            mutex.acquire()
            print('process 2 recieve the string: {}'.format(Chat_Channel2.get()))
            mutex.release()

if __name__ == '__main__':
    Chat_Channel1 = Queue()
    Chat_Channel2 = Queue()
    mutex = Lock()
    plist = []
    p1 = Process(target = receive1, args = (Chat_Channel1, mutex))
    p2 = Process(target = receive2, args = (Chat_Channel2, mutex))
    plist.append(p1)
    plist.append(p2)
    p1.start()
    p2.start()
    # p1.join()
    # p2.join()    
    info = input('请输入发送进程以及发送内容， 空格分隔，‘###’结束：').split()
    #print(info)
    while info[0] != '###':
        if info[0] == '1':
            Chat_Channel2.put(info[1])
        elif info[0] == '2':
            Chat_Channel1.put(info[1])
        else:
            print('没有该进程的通讯通道！请重试')
        time.sleep(0.2)
        info = input('请输入发送进程以及发送内容， 空格分隔，‘###’结束：').split()
        #print(info)
    else:
        # if not Chat_Channel1.empty():
        #     print(Chat_Channel1.get())
        # if not Chat_Channel2.empty():
        #     print(Chat_Channel2.get())
        p1.terminate()
        p2.terminate()
