# coding:utf8

import socket

class Demo():
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(('192.168.109.245', 6379))
        # self.socket.connect(('127.0.0.1', 6379))

    def set(self, key, val):
        commondList = []
        commondList.append('*3')

        commondList.append('$3')
        commondList.append('SET')

        keyLength = len(key)
        commondList.append('$'+str(keyLength))
        commondList.append(key)

        valLength = len(val)
        commondList.append('$'+str(valLength))
        commondList.append(val)

        commondStr = "\r\n".join(commondList)
        commondStr += "\r\n"

        self.socket.send(commondStr)

        data = self.socket.recv(1024)
        print data
    def get(self,key):
        commondList = []
        commondList.append('*2')

        commondList.append('$3')
        commondList.append('GET')

        keyLength = len(key)
        commondList.append('$' + str(keyLength))
        commondList.append(key)

        commondStr = "\r\n".join(commondList)
        commondStr += "\r\n"

        self.socket.send(commondStr)

        data = self.socket.recv(1024)
        print data



if __name__ == "__main__":
    # Demo().set('name', 'test1')
    Demo().get('name')