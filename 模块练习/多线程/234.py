# -*- coding: utf-8 -*-
import threading
import time
class mythread(threading.Thread):
    def __init__(self,fun,args):
        threading.Thread.__init__(self)
        self.fun = fun
        self.args = args
    def run(self):
        apply(self.fun, self.args)

def sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
        time.sleep(0.001)
    print sum
print '*******single Thread*****'
time1 =time.time()
sum(1000)
sum(1000)
interval1 = time.time() - time1
print 'interval1: ',interval1

print '*********Multithred ************'

n = [1000,1000]
my = []
time2 = time.time()


for i in range(len(n)):
    t = mythread(sum, (n[i],))
    my.append(t)

for i in range(len(n)):
    my[i].start()

for i in range(len(n)):
    my[i].join(i)

interval2 = time.time() - time2
print 'intervak2: ', interval2