# -*- coding: UTF-8 -*-
# 默认开头，声明本.py文件中的所有编码都是utf-8.
import requests
# 导入requests模块，该模块
import codecs
# 导入自然语言编码转换模块，解决打开txt编码问题
zhuanqu = requests.get('http://cuiqingcai.com')
#抓取所有web内容
print zhuanqu.encoding
#打印抓取web的编码格式
print zhuanqu.cookies
#打印抓取web的cookies
html = zhuanqu.text
#定义HTML 等于抓取页面的内容
file = codecs.open('2.txt', 'w', 'utf-8')
#定义文件file
file.write(html)
#将抓取的内容写入文件
file.close()
#关闭文件
