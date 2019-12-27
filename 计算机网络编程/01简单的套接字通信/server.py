# coding:utf8
import socket

# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print phone     # <socket._socketobject object at 0x10bdd78a0>


# 2、绑定手机卡
phone.bind(('127.0.0.1', 8080))

# 3、开启
phone.listen(5)     # 最大挂起的连接数（允许5个通信同时建立）


# 4、等电话连接
conn, client_addr = phone.accept()
# print res       # (<socket._socketobject object at 0x1115d97c0>, ('127.0.0.1', 56340))


# 5、收、发消息
data = conn.recv(1024)     # 1、单位byte 2、1024代表最大接受1024个bytes
print('这是客户端的数据', data)


conn.send(data.upper())

# 6、挂电话
conn.close()


# 7、关机
phone.close()