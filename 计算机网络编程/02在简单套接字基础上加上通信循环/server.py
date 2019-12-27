# coding:utf8
import socket


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(('127.0.0.1', 8080))

phone.listen(5)

conn, client_addr = phone.accept()

while True:     # 通信循环
    data = conn.recv(1024)
    print('这是客户端的数据', data)


    conn.send(data.upper())

# 6、挂电话
conn.close()


# 7、关机
phone.close()