# coding:utf8
import socket


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 关闭程序，端口过一会才能被回收，加上这句，关闭程序后端口会被尽快回收
phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1', 8080))

phone.listen(5)

conn, client_addr = phone.accept()

while True:
    data = conn.recv(1024)

    # server-bug:如果客户端被干掉，linux会一直接受到空数据,window会抛异常（try...catch）
    if not data:
        break
    print('这是客户端的数据', data)

    conn.send(data.upper())

# 6、挂电话
conn.close()


# 7、关机
phone.close()