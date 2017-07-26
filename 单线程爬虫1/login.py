# -*- coding: UTF-8 -*-
# 默认开头，声明本.py文件中的所有编码都是utf-8.
import requests
# 导入requests模块，该模块
import codecs
#导入codecs模块，
zhuanqu = requests.get('http://cuiqingcai.com')
print zhuanqu.encoding
print zhuanqu.cookies
html = zhuanqu.text
file = codecs.open('2.txt', 'w', 'utf-8')
file.write(html)
file.close()
