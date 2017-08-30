# -*- coding:utf-8 -*-
import requests
def request(x):
#    url = x
    re = requests.get(x)
    print re.status_code

request('http://www.baidu.com')
