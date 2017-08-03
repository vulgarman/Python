# -*- coding: utf-8 -*-
# 参考文档：http://shelly-kuang.iteye.com/blog/797713

# 导入模块optparse
import optparse
# 创建一个optparse模块下的OptionParse对象
# 打印的提示选项
# 这两行可以合并一起写
usage = "程序是这样用滴，[ -f <文件名称>][-s <字典名称>] arg1[,arg2..]"
parse = optparse.OptionParser(usage)
# 使用add_option命令行来定义参数，参数主要有 -f 或者 –file 分别是长短参数名
'''
action 是 parse_args() 方法的参数之一，它指示 optparse 当解析到一个命令行参数时该如何处理。
actions 有一组固定的值可供选择，默认是’store ‘，表示将命令行参数值保存在 options 对象里
例如：
parser.add_option("-f", "--file",action="store", type="string", dest="filename")  
args = ["-f", "foo.txt"]  
(options, args) = parser.parse_args(args)  
print options.filename  

最后将会打印出 “foo.txt”。
当 optparse 解析到’-f’，会继续解析后面的’foo.txt’，然后将’foo.txt’保存到 options.filename 里。
当调用 parser.args() 后，options.filename 的值就为’foo.txt’。
'''
parse.add_option("-f", "--file",action="store", type="string", dest="filename")
parse.add_option("-s", "--dict",action="store", type="string", dest="dictname")
# 调用 parse_args() 来解析程序的命令行：
# 你也可以传递一个命令行参数列表到 parse_args()；否则，默认使用 sys.argv[:1]。parse_args() 返回的两个值：
# options，它是一个对象（optpars.Values），保存有命令行参数值。只要知道命令行参数名，如 file，就可以访问其对应的值： options.file 。
# args，它是一个由 positional arguments 组成的列表。
(options, args) = parse.parse_args()
