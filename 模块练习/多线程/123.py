# -*- coding: utf-8 -*-
import threading
import time
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
mythread = []
time2 = time.time()


for i in range(len(n)):
    t = threading.Thread(target= sum, args= (n[i],))
    mythread.append(t)

for i in range(len(n)):
    mythread[i].start()

for i in range(len(n)):
    mythread[i].join(i)

interval2 = time.time() - time2
print 'intervak2: ', interval2