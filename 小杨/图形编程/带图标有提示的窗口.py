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
        # 定义显示提示信息的字体，我们使用大小10px的SansSerif字体
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif',10))
        # 为widget窗体使用setToolTip方法写入提示信息，可以用html标签
        self.setToolTip('This is a <b>Qwidget</b> widget')
        # 创建一个按钮
        btn = QtGui.QPushButton('Button', self)
        # 给按钮使用setToolTip方法编辑天使信息
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # 设定按钮大小，其中sizeHint()方法返回了一个推荐的大小
        btn.resize(btn.sizeHint())
        # 移动按钮的位置，相对于widget的x和y坐标
        btn.move(100, 50)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle(u'带图标有提示的窗体')
        self.setWindowIcon(QtGui.QIcon('pig.png'))
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

