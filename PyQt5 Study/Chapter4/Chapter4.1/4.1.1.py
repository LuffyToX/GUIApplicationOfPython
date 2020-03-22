# -*- coding: utf-8 -*-
# 创建主窗口


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.resize(1000, 600)                           # 设置主窗口大小 (width, height)
        self.setWindowTitle("MainWindow")                # 设置主窗口标题
        self.setWindowIcon(QIcon(r".\images\2.ico"))     # 设置主窗口图标

        # 获取状态栏对象
        # showMessage(message, timeout=0)
        # timeout => 状态栏信息显示时间(ms)
        status = self.statusBar()
        status.showMessage("这是状态栏提示", 5000)

        # QMainWindow 中有一个控件（QWidget）占着中心窗口
        # 可以使用 setCentralWidget() 来设置中心窗口
        text = QTextEdit()
        self.setCentralWidget(text)

        # QMainWindow 不能设置布局，因为它有自己的布局
        # self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
