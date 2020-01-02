# -*- coding: utf8 -*-

import socket
import time
from thread import SocketIoThread


class SocketServer:

    def __init__(self,port,IO):
        self.io = IO
        self.io.setServer(self)
        self.uid = 0
        self.port = port
        self.IoList = {}

    def run(self):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        sock.bind(('',self.port))
        sock.listen(100)
        #socket(服务器端的socket资源)：<socket._socketobject object at 0x107378fa0>

        while True:
            try:
                #connection(客户端的socket资源):<socket._socketobject object at 0x107591050>
                #address(客户端的地址):('127.0.0.1', 62016)
                connection,address = sock.accept()
                self.uid += 1
                self.IoList[self.uid] = SocketIoThread(connection,self.uid,self.io)
                self.IoList[self.uid].start()
            except:
                time.sleep(1)


    def sendData(self,uid,text):
        if self.IoList.has_key(uid):
            print uid,text
            self.IoList[uid].sendData(text)
