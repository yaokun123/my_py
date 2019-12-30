# coding:utf8
import socket


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.bind(('127.0.0.1', 8080))

phone.listen(5)

conn, client_addr = phone.accept()

while True:     # 加上通信循环

    # server-bug:如果客户端意外终止，linux会一直接受到空数据,window会抛异常（try...catch）
    # 下一节会专门修复这个bug
    data = conn.recv(1024)
    print '这是客户端的数据', data

    conn.send(data.upper())

# 6、挂电话
conn.close()


# 7、关机
phone.close()