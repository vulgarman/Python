# -*- coding: utf-8 -*-
from socket import *
host = '192.168.1.85'
port = 12345
bufsiz = '1024'
addr = (host, port)
tcpclientsoc = socket(AF_INET,SOCK_STREAM)
tcpclientsoc.connect(addr)
while True:
    data = raw_input('>>>> ')
    if not data:
        break
    tcpclientsoc.send(data)
    data = tcpclientsoc.recv(bufsiz)
    print data
tcpclientsoc.close()
