# -*- coding: utf-8 -*-
from socket import *
from time import ctime

host = ''
port = 12346
bufsiz = 1024
addr = (host, port)

udpSersock = socket(AF_INET,SHUT_RDWR)
udpSersock.bind(addr)

while True:
    print "waiting for connecting......."
    data,addr= udpSersock.recvfrom(bufsiz)
    udpSersock.sendto('[%s], %s' % (ctime(), data.upper()), addr)
    print '.....recevied from and return to :', addr
udpSersock.close()