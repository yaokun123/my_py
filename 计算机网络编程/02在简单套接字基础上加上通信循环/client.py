# coding:utf8
import socket


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))


while True:     # 通信循环
    msg = raw_input('>>:')

    # client-bug:如果客户端发送空数据，服务端无法recv（其实客户端根本没发送出去）
    # 下一节会专门修复这个bug
    phone.send(msg)

    data = phone.recv(1024)
    print data

# 4、关机
phone.close()
