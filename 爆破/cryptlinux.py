# -*- coding: utf-8 -*-
#将本文和wordlist.txt仍到linux机器上运行即可。
import crypt
def pojie(salt,hash):
    wordlist  =open("wordlist.txt","r")
    for word in wordlist:
        word = word.strip('\n')
        print "匹配字典中的： " +word
        hashv = crypt.crypt(word,salt)
        print "计算出来的加密哈希值为： " +hashv
        if (str(hashv) == str(hash)):
            print "[+] 密码匹配： " +word+"\n"
            return
    print "[-]字典中没有匹配的密码，请更新字典.\n"
    return
def main():
    passFile =open('/etc/shadow','r')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(":")[0]
            print "需要爆破密码的用户名为： " +user
            password = line.split(":")[1]
            if (password == '*'):
                print "用户"+ user+"禁止登陆"
            elif (password == '!'):
                print "用户"+ user+"没有密码，无需爆破."
            else:
                print "需要爆破的密文为： " +password
                if "$" in password:
                    id = password.split("$")[1]
                    if id != '6':
                        print "密码没有使用sha-512加密，本程序无法破解"
                        return
                    salt1 = password.split("$")[0:2]
                    salt = "$"+id+"$"+salt1+"$"
                    print "加的盐为： " +salt
                    print "[+] Cracking password for: " +user
                    pojie(salt, password)
if __name__ == '__main__':
    main()
