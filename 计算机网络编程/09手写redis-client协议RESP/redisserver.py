# coding:utf8
import socket
import subprocess
import struct
import json


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1', 6379))

phone.listen(5)

while True:     # 链接循环
    conn, client_addr = phone.accept()

    while True:

        # 1、接受命令
        cmd = conn.recv(1024)
        if not cmd:
            break

        print cmd

        conn.send('111111111')

    # 6、挂电话
    conn.close()


