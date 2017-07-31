#-*- coding:utf-8 -*-
import socket
import sys
port = 21
banner = "FreeFloat FTP server"
#print 的时候怎么可以用这种+方式来输出了？
print "[+] checking for "+banner+" on port " +str(port)

services = {'ftp':21,'ssh':22,'smtp':25,'html':80}
print services.keys()
print services.items()
print services.has_key('ftp')
print services['ftp']


portList = []
portList.append(21)
portList.append(80)
portList.append(443)
portList.append(25)
portList.sort()
print portList

#index跟位置有关系，注意list的列表排序
pos = portList.index(80)
print "[+] there are "+str(pos)+" ports to scan before 80."

portList.remove(443)
print portList
cnt = len(portList)
print "[+] Scanning "+str(cnt)+" Total Ports."


socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.0.119", 21))
ans = s.recv(1024)
print ans

if ("FreeFloat Ftp Server (Version 1.00)" in ans):
    print "[+] FreeFloat FTP Server is vulnerable."
elif ("3Com 3CDaemon FTP Server Version 2.0" in banner):
    print "[+]Ability FTP Server is vulnerable."
elif ("Sami FTP Server 2.0.2" in banner):
    print "[+] Sami FTP Server is vulnerable."
else:
    print "[-]FTP Server is not vulnerable"

try:
    s.connect(("192.168.0.119", 21))
except Exception,e:
    print "[-] Error = "+str(e)

def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return

def main():
    ip1 = '192.168.0.119'
    ip2 = '192.168.0.116'
    port = 21
    banner1 = retBanner(ip1,port)
    if banner1:
        print '[+] ' + ip1 + ' : ' + banner1
    banner2 = retBanner(ip2,port)
    if banner2:
        print '[+] ' +ip2 + ': ' +banner2
if __name__ == '__main__':
    main()

def checkVulns(banner):
    if 'FreeFloat ftp Server (Version 1.00)' in banner:
        print '[+] FreeFloat FTP Server is vulnerable'
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print '[+] 3Com 3CDaemon FTP Server Version is vulnerables'
    elif 'Ability Server 2.34' in banner:
        print '[+] Ability FTP Server is vulnerable. '
    elif 'Sami FTP Server 2.0.2' in banner:
        print '[+] Sami FTP Server is vulnerable.'
    else:
        print '[-] FTP Server is not vulnerable.'
    return

def main():
    ip1 = '192.168.95.148'
    ip2 = '192.168.95.149'
    ip3 = '192.168.95.150'
    port = 21
    banner1 = retBanner(ip1, port)
    if banner1:
        print '[+] ' + ip1 + ': ' +banner1.strip('\n')
        checkVulns(banner1)
    banner2 = retBanner(ip2, port)
    if banner2:
        print '[+] ' + ip2 + ': ' +banner2.strip('\n')
        checkVulns(banner2)
    banner3 = retBanner(ip3, port)
    if banner3:
        print '[+] ' + ip3 + ': ' +banner3.strip('\n')
        checkVulns(banner3)
    if __name__ == '__main__':
        main()

# for x in range(1,255):
#     print "192.168.95."+str(x)
#
# for port in portList:
#     print port


for x in range(1,255):
    for prot in portList:
        print "[+] Checking 192.168.95."+str(x)+": "+str(port)










