# -*- coding: utf-8 -*-
from PyQt4 import QtGui
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 新建一个类Example,继承自QtGui.QWidget
# 重写类的构造函数，以方便给其增加新的属性
# 继承类的构造函数增加属性首先显示调用父类的构造函数来继承父类的所有属性，
# 使用super().__init__()或parentClassName.__init__()
# 给类Example增加了initUI属性。
# 基本上就是这么个写法，其他的后面具体在学习


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()


    def initUI(self):
        # 我们的新类是一个widget，拥有他的所有方法
        # setGeometry这个方法，它做了两件事情：将部件定位并设定了它的大小
        # 其实就是resize和move的混合函数
        # 前两个参数是部件相对于父元素的x，y坐标
        # 后两个参数是部件的宽和高
        self.setGeometry(300,300,350,250)
        self.setWindowTitle(u'带图标的窗体')
        # 为了调用setWindowIcon方法设定应用的图标
        # 创建了一个QtGui.QIon对象，创建时的参数就是我们想要的图标的路径
        self.setWindowIcon(QtGui.QIcon('pig.png'))
        self.show()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

