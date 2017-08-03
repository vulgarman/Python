# -*- coding: utf-8 -*-
import optparse

usage = '%prog -H <target host> -p <target_port>'
parser = optparse.OptionParser(usage, version='1.0')
parser.add_option('-H', dest='tgtHost',
                  type='string',
                  help='specify target host')
parser.add_option('-P', dest='tgtPort',
                  type='int',
                  help='specify target port')
(options,args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort
if (tgtHost == None) | (tgtPort == None):
    print parser.usage
    exit(0)



