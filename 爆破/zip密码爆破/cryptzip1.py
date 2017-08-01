# -*- coding: utf-8 -*-
import zipfile
#注意  ZipFile 这个方法必须大写Z和F。
zFile = zipfile.ZipFile("hello.zip")
wordlist = open('wordlist.txt', 'r')
for words in wordlist.readlines():
    word = words.strip('\n')
    print "测试密码： " + word
try:
    zFile.extractall(pwd = word)
    print '[+] 正确密码为：' + word +'\n'
    exit(0)
except Exception, e:
    pass