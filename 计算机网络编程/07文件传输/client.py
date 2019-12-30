# coding:utf8
import socket
import struct
import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))

download_dir = os.path.join(os.getcwd(), 'download')

while True:

    # 1、发命令
    cmd = raw_input('>>:')

    if not cmd:
        continue
    phone.send(cmd)

    # 2、以写的方式打开一个新文件，接收服务端发来的文件内容写入客户端的新文件

    # 第一步：先收报头的长度
    obj = phone.recv(4)
    header_size = struct.unpack('i', obj)[0]

    # 第二步：再收报头
    header_byte = phone.recv(header_size)

    # 第三步：从报头中解析出对真实数据的描述信息
    header_json = header_byte
    header_dic = json.loads(header_json)
    print header_dic
    total_size = header_dic['total_size']
    file_name = header_dic['filename']

    # 第三步：接受真实数据
    with open(os.path.join(download_dir, file_name), 'wb') as f:
        recv_size = 0
        recv_data = ''
        while recv_size < total_size:
            line = phone.recv(1024)
            f.write(line)
            recv_size += len(line)
            print '总大小%d，已下载%d' % (total_size,recv_size)

# 4、关机
phone.close()
