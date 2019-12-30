# coding:utf8
import socket
import subprocess
import struct
import json


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
        header_dic = {
            'filename': 'a.txt',
            'md5': 'xxxxxxxx',
            'total_size': total_size
        }
        header_json = json.dumps(header_dic)

        header_bytes = header_json

        # 第二步：先发送报头的长度
        conn.send(struct.pack('i', len(header_bytes)))

        # 第三步：再发报头
        conn.send(header_bytes)

        # 第四步：再发送真实数据
        conn.send(stdout)
        conn.send(stderr)

    # 6、挂电话
    conn.close()


# 7、关机
phone.close()