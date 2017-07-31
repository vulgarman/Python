#-*- coding:utf-8 -*-
import re
#from re import *
#from re improt findall,search,sub,S
secret_code = 'sdfdsfxxIxxfsdklafjdsxxLovexxflksdjflsdxxYouxxfdsfds'
'''
----------------------
正则表达式基本符号 
----------------------
点号  星号  问号  小括号
----------------------
.:匹配任意字符，换行符\n除外
*：匹配前一个字符0次或无限次
?：匹配前一个字符0次或1次
.*:贪心算法
.*?:非贪心算法
():括号内的数据作为结果返回
--------
正则表达式的常用方法
------------------------
findall:匹配所有符合规律的内容，返回包含结果的列表
search:匹配并提取第一个符合规律的内容，返回一个正则表达式对视（object）
sub:替换符合规律的内容，返回替换后的值
'''
#.的使用  .可以当作占位符看待，一个.就是一个占位符
#结果以list展示，并且只有一个值
# a = 'xz123'
# b = re.findall('x...',a)
# print b

#*的使用  *可以匹配它前面的字符0次或无限次。
#结果以list展示，匹配成功的原样显示，匹配不到的位置空输出
# a = 'xyxyxy123'
# b = re.findall('x*',a)
# print b

#？的使用 ?可以匹配它前面的字符0次或者1次
# a = '123xy124'
# b = re.findall('x?',a)
# print b

#.*的使用 .*贪心算法，能取多少取多少
# b = re.findall('xx.*xx',secret_code)
# print b
# #.*?的使用 .*?惰性算法，少量多餐
# #注意？是英文的还是中文的
# c = re.findall('xx.*?xx',secret_code)
# print c
# #(.*?)的使用,对比与上一个没有括号的区别
# #只返回（）里面的东西
# d = re.findall('xx(.*?)xx',secret_code)
# print d
# for i in d:
#     print i

#re.S的作用是 使.不能匹配换行扩展到可以匹配换行
# s = '''fdsfdxx
# lovexxdfksdfkxxyouxxkdfjskdjf'''
#
# f = re.findall('xx(.*?)xx',s,re.S)
# print f
#
#group 只匹配前面里面有几个()
s2 = 'asdfxxIxx123213xxLovexxdfd'
# h = re.search('xx(.*?)xx123213xx(.*?)xx',s2).group(2)
# print h

# i = re.search('xx(.*?)xx',s2).group(1)
# print i

# j = re.findall('xx(.*?)xx123213xx(.*?)xx',s2)
# print j[0][1]

# s3 ='123fsafsdsfa123'
# output = re.sub('123(.*?)123','replace%d123'%123,s3)
# print output

#匹配纯数字
# a = 'asdfasf123123fasd5555fd'
# b = re.findall('(\d+)',a)
# print b


