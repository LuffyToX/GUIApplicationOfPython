# -*- coding: utf-8 -*-
# 使用自定义的无边框窗口


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # 设置窗口样式：无边框
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 为便于显示，设置窗口背景颜色（采用QSS）
        self.setStyleSheet(''' background-color:red; ''')

    def showMaximized(self):
        desktop = QApplication.desktop()       # 获取桌面控件
        rect = desktop.availableGeometry()     # 获取屏幕可显示尺寸
        self.setGeometry(rect)                 # 设置窗口尺寸
        self.show()                            # 显示窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.showMaximized()
    sys.exit(app.exec_())
