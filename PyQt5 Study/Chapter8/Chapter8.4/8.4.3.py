# -*- coding: utf-8 -*-
# QPalette 设置窗口背景色


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 600, 400)

        palette = QPalette()                             # 获取调色板对象
        palette.setColor(QPalette.Background, Qt.red)    # 设置调色板颜色
        self.setPalette(palette)                         # 将调色板对象加载到主窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
