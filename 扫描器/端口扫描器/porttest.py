# -*- coding: utf-8 -*-
import optparse
from socket import *

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('testportfrompython\r\n')
        results = connSkt.recv(1024)
        print '[+] %d/tcp open' % tgtPort
        print '[+] ' +str(results)
        connSkt.close()
    except:
        print '[-]%d/tcp closed' % tgtPort

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown host" %tgtHost
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for: ' +tgtName[0]
    except:
        print '\n[+] Scan Results for: ' +tgtIP
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print 'Scanning port ' + tgtPort
        connScan(tgtHost, int(tgtPort))

def main():
    parser = optparse.OptionParser("usage %prog "+ "-H <target host> -p <target port>")

    parser.add_option('-H', '--host',
                      dest='tgtHost', type='string',
                      help='specify target host')

    parser.add_option('-p', '--port',
                      dest='tgtPort', type='string',
                      help='specify target port[s] separated by comma')

    (options, args) = parser.parse_args()

    tgtHost = options.tgtHost

    # print "host is: " + tgtHost
    # a = options.tgtPort
    # print "a is： " + a
    # b = a.split(', ')
    # print 'b is: ' + b


    tgtPorts = str(options.tgtPort).split(', ')

    if (tgtHost == None) | (tgtPorts[0] ==None):
        print '[-] You must specify a target host and port[s].'
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
