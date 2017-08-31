# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(600, 600)
        self.center()
        self.setWindowTitle(u'出现在屏幕最中间')
        self.setWindowIcon(QtGui.QIcon('pig.png'))
        self.show()

    def center(self):
        # 用frameGeometry方法得到了主窗口的矩形框架
        qr = self.frameGeometry()
        # QtGui.QDesktopWidget这个类提供了用户桌面的信息，包括屏幕大小
        # 调用这些方法来得到屏幕分辨率，并最终得到屏幕中间点的坐标cp
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        # 矩形框架移至屏幕正中央
        qr.moveCenter(cp)
        # 应用窗口移至矩形框架的左上角点，这样应用窗口就位于屏幕的中央了
        self.move(qr.topLeft())


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()