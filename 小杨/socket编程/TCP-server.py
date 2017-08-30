# -*- coding: utf-8-*-
from socket import *
import os
host = '192.168.1.85'
port = 12345
bufsiz = 1024
addr = (host, port)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(addr)
tcpSerSock.listen(5)
def getstatusoutput(cmd):
    info = os.popen(cmd)
    info_text = info.read()
    info_status = info.close()
    return info_text, info_status
while True:
    print "wait for connection ...."
    tcpCliscock, addr1 = tcpSerSock.accept()
    print '...connected from:', addr1
    while True:
        data = tcpCliscock.recv(bufsiz)
        if not data:
            break
        text,status = getstatusoutput(data.strip())
        if not status:
            tcpCliscock.send(text)
        else:
            tcpCliscock.send("error cmd")
    tcpCliscock.close()
tcpSerSock.close()



