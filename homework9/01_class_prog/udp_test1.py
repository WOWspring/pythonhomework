import socket

def main():
    #1 创建一个udp套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    
    # 2. 准备接收方的地址 使用udp套接字发送数据:发什么,发给谁
    # '192.168.1.24'表示目的ip地址
    # 8888表示目的端口
    dest_addr = ('192.168.119.1', 5757)  # 注意 是元组，ip是字符串，端口是数字

    # 3. 从键盘获取数据
    send_data = input("请输入要发送的数据:")
    # 4. 发送数据到指定的电脑上的指定程序中
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
    
    # 5 关闭套接字
    udp_socket.close()
   
if __name__ == "__main__":
    main()
