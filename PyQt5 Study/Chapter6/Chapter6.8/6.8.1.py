# -*- coding: utf-8 -*-
# QSplitter 动态布局管理器的使用


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 500, 300)

        # 左侧窗体控件
        topleft = QFrame()
        topleft.setFrameShape(QFrame.StyledPanel)

        # 底部窗体控件
        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        # 多行文本框
        textedit = QTextEdit()

        # 水平 QSplitter 布局并初始化大小
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(textedit)
        splitter1.setSizes([100, 200])

        # 垂直 QSplitter 布局
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        # 水平布局
        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter2)
        self.setLayout(hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

