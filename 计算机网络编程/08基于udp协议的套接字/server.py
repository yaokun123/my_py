import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('127.0.0.1', 8080))

while True:
    data, client_addr = server.recvfrom(1024)
    print(data)

    server.sendto(data.upper(), client_addr)

server.close()