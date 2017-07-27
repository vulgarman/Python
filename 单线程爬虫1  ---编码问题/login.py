#  -*- coding:utf-8 -*-
#定义本.py文件的编码格式为utf-8，如果在本文件中出现了非utf-8的编码格式
# 则调用sys.defaultencoding 来指明默认的编码，很多情况下 sys.defaultencoding 是 ANSCII。
#python 里面的编码和解码也就是 unicode 和 str 这两种形式的相互转化。
#编码是指从编码是 unicode -> str，解码是指 str -> unicode
#查询编码的命令是？
#如果出现了无法解码的情况，首先讲变量编码成utf-8，则不会在出现编码问题了。
import requests
#import  sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
r = requests.get('http://cuiqingcai.com')
print "本web页面的编码是:\n%s"  %r.encoding
print "本web页面的源码如下:\n%s"  %r.text.encode('utf-8')
#print r.text
