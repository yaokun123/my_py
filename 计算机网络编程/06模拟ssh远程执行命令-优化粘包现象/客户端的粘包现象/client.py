# coding:utf8
import socket


phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

phone.connect(('127.0.0.1', 8080))

# client 这里连续发送了两个包
phone.send('hello')
phone.send('world')

# 在操作系统中会有一个Nagle算法：会将时间间隔比较短包较小的包合并成一个包


phone.close()
