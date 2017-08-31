# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif',10))
        self.setToolTip('This is a <b>Qwidget</b> widget')
        # 生成一个关闭按钮
        btn = QtGui.QPushButton(u'关闭', self)
        # 点击了这个按钮，就会发出“clicked”这个信号
        # QtCore.QCoreApplication这个东西包含了程序的主循环
        # 它处理和分派所有的事件，而instance()方法返回的是目前的实例(insatnce)
        # 我们使用connect()函数将“clicked”事件和可以终止应用的quit()函数联系(connect)在了一起
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.setToolTip(u'点击会<b>关闭</b>本程序')
        btn.resize(btn.sizeHint())
        btn.move(200, 200)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle(u'带图标有提示有动作按钮的窗体')
        self.setWindowIcon(QtGui.QIcon('pig.png'))
        self.resize(350, 250)
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

