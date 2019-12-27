# coding:utf8
import socket


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1', 8080))

phone.listen(5)

while True:     # 链接循环
    conn, client_addr = phone.accept()

    while True:
        data = conn.recv(1024)

        if not data:
            break
        print('这是客户端的数据', data)


        conn.send(data.upper())

    # 6、挂电话
    conn.close()


# 7、关机
phone.close()