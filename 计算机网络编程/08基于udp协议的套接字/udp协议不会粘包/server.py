# coding:utf-8
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('127.0.0.1', 8080))

# 如果这里接受的是一个字节，那么剩下的就会被丢掉（windows会直接报错）
res1 = server.recvfrom(1024)
# res1 = server.recvfrom(1)
print '第一次接受', res1

res2 = server.recvfrom(1024)
print '第二次接受', res2

server.close()