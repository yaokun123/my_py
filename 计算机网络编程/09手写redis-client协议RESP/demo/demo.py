# coding:utf8

import socket


class Demo(object):
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('192.168.109.245', 6379))
        # self.socket.connect(('127.0.0.1', 6379))

    def set(self, key, val):
        commond_list = list()
        commond_list.append('*3')

        commond_list.append('$3')
        commond_list.append('SET')

        key_length = len(key)
        commond_list.append('$'+str(key_length))
        commond_list.append(key)

        val_length = len(val)
        commond_list.append('$'+str(val_length))
        commond_list.append(val)

        commond_str = "\r\n".join(commond_list)
        commond_str += "\r\n"

        self.socket.send(commond_str)

        data = self.socket.recv(1024)
        self.decode_resp(data)

    def get(self, key):
        commond_list = list()
        commond_list.append('*2')

        commond_list.append('$3')
        commond_list.append('GET')

        key_length = len(key)
        commond_list.append('$' + str(key_length))
        commond_list.append(key)

        commond_str = "\r\n".join(commond_list)
        commond_str += "\r\n"

        self.socket.send(commond_str)

        data = self.socket.recv(1024)
        self.decode_resp(data)

    @staticmethod
    def decode_resp(data):
        # 先读取一个字节
        res = data.split("\r\n")
        res1 = res[0]

        op = res1[0:1]

        if op == "+":
            # 单行回复
            print res1[1:]
        elif op == "$":
            # 多行字符串
            length = res1[1:]
            print length + ":" + res[1]


if __name__ == "__main__":
    while True:
        cmd = raw_input('>>:')

        if not cmd:
            continue

        cmds = cmd.split(' ')

        if cmds[0].upper() == 'SET' and len(cmds) == 3:
            Demo().set(cmds[1], cmds[2])
        elif cmds[0].upper() == 'GET' and len(cmds) == 2:
            Demo().get(cmds[1])
        elif cmds[0].upper() == 'EXIT':
            break
        else:
            print '命令暂不支持'
