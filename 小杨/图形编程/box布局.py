# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Boxlayout(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        self.setWindowIcon(QtGui.QIcon('pig.png'))
        self.setWindowTitle(u'Box布局')

        ok = QtGui.QPushButton(u'确认')
        cancel = QtGui.QPushButton(u'取消')

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(ok)
        hbox.addWidget(cancel)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.resize(400, 250)

def main():
    app = QtGui.QApplication(sys.argv)
    box = Boxlayout()
    box.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()