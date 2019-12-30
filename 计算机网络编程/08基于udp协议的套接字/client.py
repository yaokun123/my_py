import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = raw_input('>>').strip()

    client.sendto(msg, ('127.0.0.1', 8080))

    data, server_addr = client.recvfrom(1024)

    print data, server_addr

client.close()