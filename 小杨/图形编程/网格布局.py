# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Boxlayout(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self)
        self.setWindowIcon(QtGui.QIcon('pig.png'))
        self.setWindowTitle(u'网格布局')