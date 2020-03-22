# -*- coding: utf-8 -*-
# QTreeView 系统定制模式


import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.resize(640, 480)

        model = QDirModel()                      # Window 系统提供的模式
        treeView = QTreeView()                   # 创建一个 QTreeView 控件
        treeView.setModel(model)                 # 为 QTreeView 控件添加模式
        self.setCentralWidget(treeView)          # 将树形结构设置为主中心窗口


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
