# coding:utf8
import socket


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))


while True:

    # 1、发命令
    cmd = raw_input('>>:')

    if not cmd:
        continue
    phone.send(cmd.encode('utf-8'))

    # 拿到命令结果并打印
    data = phone.recv(1024)    # 1024是一个坑，如果服务端返回的数据大于1024个字节怎么办（比如ifconfig）
    print data

# 4、关机
phone.close()
