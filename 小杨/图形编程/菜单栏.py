# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)

        self.setWindowTitle(u'我的主程序')
        self.setWindowIcon(QtGui.QIcon('pig.png'))
        self.resize(550, 450)

        exit = QtGui.QAction(QtGui.QIcon('pig.png'), u'退出', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip(u'退出程序')
        exit.connect(exit, QtCore.SIGNAL('triggered()'), QtGui.qApp, QtCore.SLOT('quit()'))
        #
        self.statusBar()
        # 建立菜单栏
        menubar = self.menuBar()
        # 建立一个菜单
        file = menubar.addMenu(u'文件')
        # 绑定前面的action
        file.addAction(exit)

        toolbar = self.addToolBar(u'退出')
        toolbar.addAction(exit)

        text = QtGui.QTextEdit()
        self.setCentralWidget(text)


def main():
    app = QtGui.QApplication(sys.argv)
    ms = MainWindow()
    ms.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()