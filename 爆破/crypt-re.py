# -*- coding: utf-8 -*-
#请注意  crypt模块仅支持linux平台，所以win下无法运行
#请注意  txt中win下和linux下的不同。
import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]

    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        print "匹配字典中的: " +word
        cryptWord = crypt.crypt(word, salt)
        print "字典生成的哈希值为 ：" +str(cryptWord)
        if (cryptWord == cryptPass):
            print "[+] Found Password: " +word+"\n"
            # return
    print "[-] Password Not Found. \n"
    return

def main():
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            print "爆破密码的用户名是: " +user
            cryptPass = line.split(':')[1].strip(' ')
            print "爆破密码的哈希值为: " +cryptPass
            print "[*] Cracking Password For: "+user
            testPass(cryptPass)

if __name__ == '__main__':
    main()


