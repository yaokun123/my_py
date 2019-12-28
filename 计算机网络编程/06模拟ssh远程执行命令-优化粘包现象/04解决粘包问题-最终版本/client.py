# coding:utf8
import socket
import struct
import json


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))


while True:

    # 1、发命令
    cmd = raw_input('>>:')

    if not cmd:
        continue
    phone.send(cmd.encode('utf-8'))

    # 拿到命令结果并打印

    # 第一步：先收报头的长度
    obj = phone.recv(4)
    header_size = struct.unpack('i', obj)[0]

    # 第二步：再收报头
    header_byte = phone.recv(header_size)

    # 第三步：从报头中解析出对真实数据的描述信息
    header_json = header_byte.decode('utf-8')
    header_dic = json.loads(header_json)
    print header_dic
    total_size = header_dic['total_size']

    # 第三步：接受真实数据
    recv_size = 0
    recv_data = ''
    while recv_size < total_size:
        res = phone.recv(1024)
        recv_data += res
        recv_size += len(res)

    print recv_data

# 4、关机
phone.close()
