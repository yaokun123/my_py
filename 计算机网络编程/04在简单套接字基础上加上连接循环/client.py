# coding:utf8
import socket


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))


while True:
    msg = raw_input('>>:')

    if not msg:
        continue
    phone.send(msg.encode('utf-8'))

    data = phone.recv(1024)
    print data

# 4、关机
phone.close()
