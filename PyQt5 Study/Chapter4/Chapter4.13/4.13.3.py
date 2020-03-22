# -*- coding: utf-8 -*-
# QStatusBar 的使用（状态栏）


import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.resize(400, 300)

        # 设置菜单栏
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("show")
        file.triggered[QAction].connect(self.processTrigger)

        # 添加中心控件 QTextEdit()
        self.setCentralWidget(QTextEdit())

        # 设置状态栏
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)

    def processTrigger(self, q):
        # 当菜单栏的 "show" 被点击，将显示状态栏
        if q.text() == "show":
            self.statusBar.showMessage(q.text() + " 菜单选项被点击了", 5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
