# -*- coding: utf-8 -*-
# QTooBar 的使用（工具栏）


import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.resize(300, 200)

        # 添加一个工具栏 "File"
        tb = self.addToolBar("File")

        # 添加工具按钮 "open"
        open_ = QAction(QIcon(r".\images\17.ico"), "open", self)
        tb.addAction(open_)

        # 添加工具按钮 "close"
        close_ = QAction(QIcon(r".\images\15.ico"), "close", self)
        tb.addAction(close_)

        # 每当单击工具栏中的按钮时，都将发射 actionTriggered 信号
        tb.actionTriggered[QAction].connect(self.toolbtnpressed)

    @staticmethod
    def toolbtnpressed(a):
        print("pressed tool button is", a.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
