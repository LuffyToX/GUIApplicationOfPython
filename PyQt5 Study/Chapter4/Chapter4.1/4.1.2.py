# -*- coding: utf-8 -*-
# 主窗口居中显示


import sys
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")              # 设置主窗口标题
        self.setWindowIcon(QIcon(r".\images\2.ico"))   # 设置主窗口图标
        self.resize(1000, 600)                         # 设置主窗口大小
        self.center()

    def center(self):
        """ 将主窗口居中显示 """
        screen = QDesktopWidget().screenGeometry()     # 获取桌面大小
        size = self.geometry()                         # 获取主窗口大小
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
