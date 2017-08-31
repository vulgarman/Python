# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# 每个PyQt4应用都必须创建一个应用(application)，这个应用对象位于QtGui模块中
# sys.argv参数是由命令行参数组成的列表(list)
app = QtGui.QApplication(sys.argv)
# 创建了一个窗口
widget = QtGui.QWidget()
# 使用resize()方法调整窗体的大小，宽350px,高250px
widget.resize(350, 250)
# 使用move()方法将窗体移动位置
# 屏幕的坐标x为300，y为300.
# 屏幕的坐标是以左上角为原点的，横着是x轴，竖着是y轴
widget.move(300, 300)
# 使用setWindowTitle()设置窗体的标题
widget.setWindowTitle(u'第一个窗口程序')
# show()方法使我们创建的窗体能够在屏幕上显示出来
# 窗体先在内存(memory)中被创建，之后再被显示到屏幕上
widget.show()
# 在显示了窗口之后，我们进入了程序的主循环
# 主循环从窗口接收事件并对部件进行处理
# 如果我们调用exit()函数或者关闭最主要的部件，主循环将终止
# 这里的sys.exit()调用保证程序完全退出
# exec_()中有一个下划线，为什么呢？因为exec是一个python关键字，因此加了下划线
sys.exit(app.exec_())


