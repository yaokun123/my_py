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
    data = phone.recv(1024)    # 1024是一个坑

    # 在这里就是服务端的粘包导致的，如果服务端发送的数据大于1024那么客户端第一次(ifconfig)
    # 只能接受1024个byte，剩下的就跟其他包粘在一起了
    # 所以当你再发送ls命令的时候还会看到上次发送的ifconfig的返回结果
    print data

# 4、关机
phone.close()
