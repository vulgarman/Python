# -*- coding: utf-8 -*-
import requests
heade= {'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; .NET CLR 1.1.4322)',
'Accept-Encoding': 'gzip',
'Cookie':'JSESSIONID=4360C221EB109302BF98509849CDB560',
'Connection':'Keep-Alive'
}

hearder = {"device":"Genymotion,Google Nexus 4 - 4.1.1 - API 16 - 768x1280_2,vbox86p",
           "macadd":"123456",
           "platform":"generic,ANDROID,4.1.1"}

parload = {'USER_ID':110034,'tokencode':117386}
r = requests.post(url = 'http://60.211.217.162:9001/fqApi/api/stuUser/getStuUser.do', data=parload, headers=hearder)
print r

