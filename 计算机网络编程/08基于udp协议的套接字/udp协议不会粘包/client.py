# coding:utf-8
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# udp数据不会粘包
client.sendto(b'hello', ('127.0.0.1', 8080))
client.sendto(b'world', ('127.0.0.1', 8080))

client.close()