# -*- coding: utf-8 -*-
import threading
class mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global n
        if lock.acquire():
            print 'Thread: ', n
            n += 1
            lock.release()
n = 0
t = []
lock = threading.Lock()
for i in range(10):
    my = mythread()
    t.append(my)

for i in range(10):
    t[i].start()

for i in range(10):
    t[i].join()

