# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class Surface(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        # super(Surface, self).__init__()
        self.initUI()

    def initUI(self):
        # 生成三个按钮
        btn1 = QtGui.QPushButton(u'扫描', self)
        btn1.setToolTip(u'点击开始本次扫描')
        btn1.move(20, 500)

        btn2 = QtGui.QPushButton(u'关于', self)
        btn2.setToolTip(u'查看本程序介绍')
        btn2.move(120, 500)

        btn3 = QtGui.QPushButton(u'退出', self)
        btn3.setToolTip(u'点击<b>关闭</b>本程序')
        self.connect(btn3, QtCore.SIGNAL('clicked()'), QtGui.qApp, QtCore.SLOT('quit()'))
        # btn3.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn3.move(220, 500)

        # 程序名称以及图标
        self.resize(600, 600)
        self.center()
        self.setWindowTitle(u'进化的猪端口扫描器')
        self.setWindowIcon(QtGui.QIcon('pig.png'))

    # 打开程序保证出现在屏幕最中间
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # 关闭程序时弹窗提示
    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, u'提醒', u"你确定要关闭本程序么?",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtGui.QApplication(sys.argv)
    surface = Surface()
    surface.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()