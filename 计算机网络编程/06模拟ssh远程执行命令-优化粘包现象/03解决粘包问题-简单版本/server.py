# coding:utf8
import socket
import subprocess
import struct


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

        # 2、执行命令，拿到结果
        obj = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        stdout = obj.stdout.read()
        stderr = obj.stderr.read()

        # 3、把命令的结果返回给客户端

        # 第一步：制作固定长度的报头
        total_size = len(stdout) + len(stderr)
        header = struct.pack('i', total_size)   # 这里打包有一个限制，如果total_size过大会有问题（在下一节解决这个问题）

        # 第二步：把报头（固定长度）发送给客户端
        conn.send(header)

        # 第三步：再发送真实数据
        conn.send(stdout)
        conn.send(stderr)

    # 6、挂电话
    conn.close()


# 7、关机
phone.close()