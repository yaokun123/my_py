# coding:utf8
import socket
import subprocess


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1', 8080))

phone.listen(5)

while True:     # 链接循环
    conn, client_addr = phone.accept()

    while True:

        # 1、接受命令
        cmd = conn.recv(1024)
        if not cmd:
            break
        print '这是客户端的数据', cmd

        # 2、执行命令，拿到结果
        obj = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout = obj.stdout.read()
        stderr = obj.stderr.read()

        # 3、把命令的结果返回给客户端
        conn.send(stdout + stderr)  # bug-1:这是一个可以优化的地方（用粘包来优化）

    # 6、挂电话
    conn.close()


# 7、关机
phone.close()