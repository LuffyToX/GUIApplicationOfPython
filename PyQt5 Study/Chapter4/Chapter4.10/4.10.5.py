# -*- coding: utf-8 -*-
# QPixmap 的使用


import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")               # 窗口标题
        self.resize(300, 300)                           # 窗口大小

        qLabel = QLabel()                               # 新建标签
        qLabel.setPixmap(QPixmap(r".\images\0.ico"))    # 显示 Pixmap 图像

        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(qLabel)
        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
