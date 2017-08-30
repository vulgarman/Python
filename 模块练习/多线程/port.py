# -*- coding:utf-8 -*-
from socket import *
import sys, time, threading
class Mythread(threading.Thread):
    def __init__(self, fun, args):
        threading.Thread.__init__(self)
        self.fun = fun
        self.args = args
    def run(self):
        apply(self.fun, self.args)
def scan(h,p):
    try:
        tcpclisock = socket(AF_INET, SOCK_STREAM)
        tcpclisock.connect((h, p))
        if lock.acquire():
            print str(p) + '---> opend'
            lock.release()
    except error:
        if lock.acquire():
            print str(p) + '---> not opend'
            lock.release()
    finally:
        tcpclisock.close()
        del tcpclisock
host = sys.argv[1]
ports = [21, 23, 25, 53, 69, 80, 135, 137, 139, 1521, 1433, 3306, 3389]
lock = threading.Lock()
mt = []
for p in ports:
    t = Mythread(scan,(host,p))
    mt.append(t)
print "please waiting ... \n"
t1 =time.time()
for m in mt:
    m.start()
for m in mt:
    m.join()
print 'interval: ', time.time() - t1


