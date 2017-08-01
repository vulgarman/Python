# -*- coding: utf-8 -*-
#多线程，这个还没理解，回头还的在搞
import zipfile
from threading import Thread

def pojie(zFile,password):
    try:
        zFile.extractall(pwd=password)
        print "[+] Found password " +password +"\n"
    except:
        pass

def main():
    zFile = zipfile.ZipFile('hello.zip')
    passFile = open('wordlist.txt', 'r')
    for words in passFile.readlines():
        password = words.strip("\n")
        print "测试密码： " +password
        t = Thread(target=pojie, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()