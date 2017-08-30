# -*- coding: utf-8 -*-
#import idstools
from idstools import unified2

def rollover_hook(closed, opened):
    os.unlink(closed)

reader = unified2.SpoolRecordReader("C:\Users\lele\Desktop",
    "snort.unified2", rollover_hook = rollover_hook,
    follow=True)
for record in reader:
    print(record)