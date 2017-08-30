# -*- coding: utf-8-*-
from socket import *
host = '192.168.1.85'
port = 12346
bufsiz = 1024

addr = (host, port)

udpClisock = socket(AF_INET,SHUT_RDWR)
#注意 udp无connect

while True:
    data = raw_input('>>>>>')
    if not data:
        break
    udpClisock.sendto(data, addr)
    data,addr = udpClisock.recvfrom(bufsiz)
    print data

udpClisock.close()
