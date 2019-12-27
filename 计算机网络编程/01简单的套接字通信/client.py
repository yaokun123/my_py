# coding:utf8
import socket

# 1、买手机
phone = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# print phone     # <socket._socketobject object at 0x10bdd78a0>


# 2、拨号
phone.connect(('127.0.0.1', 8080))


# 3、发、收消息
phone.send('hello'.encode('utf-8'))

data = phone.recv(1024)
print data

# 4、关机
phone.close()
