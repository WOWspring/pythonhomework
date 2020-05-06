import socket
import threading

    # 一个UDP连接在接收消息前必须要让系统知道所占端口
    # 也就是需要send一次，否则win下会报错
    # “   data=sock.recv(1024)
    #     OSError: [WinError 10022] 提供了一个无效的参数。   ”

def write(s, addr):
    while True:
        txt = input()
        if txt == 'exit':
            s.close()
            print('Client is closed')
        else:
            s.sendto(txt.encode('utf-8'), addr)

def read(s):
    while True:
        data, addr = s.recvfrom(1024)
        if data.decode('utf-8') == 'exit':
            s.close()
            print('Client is closed')
        print('Sever : %s' %data.decode('utf-8'))


udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_s.sendto(b'Hello!', ('127.0.0.1', 7777))

# temp, addr = udp_s.recvfrom(1024)

th_read = threading.Thread(target = read, args = (udp_s,))
th_read.start()
th_write = threading.Thread(target = write, args = (udp_s, ('127.0.0.1', 7777)))
th_write.start()