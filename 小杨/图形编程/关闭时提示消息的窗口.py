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
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle(u'关闭时弹出提示框')
        self.setWindowIcon(QtGui.QIcon('pig.png'))
        self.show()

    # 根据类定义，如果关闭QtGui.QWidget，QtGui.QCloseEvent将会执行
    # 我们需要重新定制closeEvent()这个事件句柄(event handler)
    # 我们设定显示一个有两个选项(yes & no)的消息框(message box)
    # QtGui.QMessageBox.question()方法的第二个参数是出现在标题栏的标题
    # 第三个参数是消息框显示的对话内容
    # 四个参数是出现在消息框的按钮的组合【用或( | )连接】
    # 最后一个参数是默认按钮，即消息框刚跳出来的时候按enter键就可以执行的按钮

    def closeEvent(self,event):
        reply = QtGui.QMessageBox.question(self, 'Message',"Are you sure to quit?",
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()