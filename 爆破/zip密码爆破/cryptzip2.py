# -*- coding: utf-8 -*-
import zipfile
def pojie(zFile,password):
    try:
        zFile.extractall(pwd = password)
        return password
    except:
        return

def main():
    zFile = zipfile.ZipFile('hello.zip')
    wordlist = open('wordlist.txt', 'r')
    for words in wordlist.readlines():
        word = words.strip('\n')
        print "测试密码： " +word
        guess = pojie(zFile,word)
        if guess:
            print "[+] 破解成功，密码为： " +word
            exit(0)
        else:
            print "[-] 密码不正确"

if __name__ == '__main__':
    main()