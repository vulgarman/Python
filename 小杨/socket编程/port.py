# -*- coding:utf-8 -*-
from socket import *
import sys
host = sys.argv[1]
service = {'21': 'FTP', '23': 'TELNET', '25': 'SMTP',
           '53': 'DNS','69': 'TFTP', '80': 'HTTP',
           '135': 'RPC', '137': 'NetBIOS',
           '139': 'Samba', '1521': 'Oracle',
           '1433': 'SQL_Server', '3306': 'MySQL',
           '3389': 'Remote_Destop'}
ports = [21, 23, 25, 53, 69, 80, 135, 137, 139, 1521, 1433, 3306, 3389]
print "please waiting ...\n"
for p in ports:
    try:
        tcpclisock = socket(AF_INET, SOCK_STREAM)
        tcpclisock.connect((host,p))
        print service[str(p)] + ' ' +str(p) + '---->opened'
    except error:
        print service[str(p)] + ' ' + str(p) + '----> not opened'
    finally:
        tcpclisock.close()
        del tcpclisock


