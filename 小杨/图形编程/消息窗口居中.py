# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class MessageBox(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle(u'消息窗口居中')
        self.setWindowIcon(QtGui.QIcon('pig.png'))
        self.resize(550, 450)
        self.center()

    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def closeEvent(self, event):
        reply = QtGui.QMessageBox.question(self, u'警告', u'确认关闭?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    app = QtGui.QApplication(sys.argv)
    ms = MessageBox()
    ms.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()