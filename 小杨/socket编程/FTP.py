# -*- coding: utf-8 -*-
import ftplib,os,socket

host = ''
File = 'book.pdf'

username = ''
pwd = ''

try:
    f = ftplib.FTP(host)
    print "Welcome info:" +f.getwelcome() +'\n'
except(socket.error, socket.gaierror),e:
    