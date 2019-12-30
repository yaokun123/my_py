# coding:utf8
import socket
import os
import struct
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

phone.bind(('127.0.0.1', 8080))

phone.listen(5)

share_dir = os.path.join(os.getcwd(), 'share')

while True:     # 链接循环
    conn, client_addr = phone.accept()

    while True:

        # 1、接受命令
        res = conn.recv(1024)    # get a.txt
        if not res:
            break

        # 2、解析命令，提取相应命令参数
        cmds = res.split()     # ['get','a.txt']
        filename = cmds[1]

        # 3、以读的方式打开a.txt，读取文件内容发送给客户端

        # 第一步：制作固定长度的报头
        header_dic = {
            'filename': filename,
            'md5': 'xxxxxxxx',
            'total_size': os.path.getsize('%s/%s' % (share_dir, filename))
        }
        header_bytes = json.dumps(header_dic)

        # 第二步：先发送报头的长度
        conn.send(struct.pack('i', len(header_bytes)))

        # 第三步：再发报头
        conn.send(header_bytes)

        # 第四步：再发送真实数据
        with open(os.path.join(share_dir, filename), 'rb') as f:
            # conn.send(f.read())
            for line in f:
                conn.send(line)

    # 6、挂电话
    conn.close()


# 7、关机
phone.close()