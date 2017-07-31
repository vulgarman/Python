#  -*- coding:utf-8 -*-
import re
import codecs
old_url = 'http://www.jikexueyuan.com/course/android?pageNum=3'
totalpage =20
f = codecs.open('1.html','r')
html = f.read()
f.close()

#爬取标题
tittle = re.search('<title>(.*?)</title>',html).group(1)
print "本页面标题是：",tittle

#爬取链接
links = re.findall('href="(.*?)"',html,re.S)
for link in links:
    print link

#爬取部分文字信息，先抓大在抓小
texts_fied = re.findall('<ul>(.*?)</ul>',html,re.S)[0]
#print text_fied
texts = re.findall('">(.*?)<',texts_fied,re.S)
for text in texts:
    print text

#sub实现翻页
for i in range(1,totalpage+1):
    new_link = re.sub('pageNum=\d+','pageNum=%d'%i,old_url,re.S)
    print new_link
