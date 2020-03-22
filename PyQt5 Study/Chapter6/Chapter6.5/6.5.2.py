# -*- coding: utf-8 -*-
# QGridLayout 跨越行和列的网格单元格


import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("故障申告")
        self.setGeometry(800, 300, 350, 300)

        # 栅格布局
        grid = QGridLayout(self)
        grid.setSpacing(10)

        grid.addWidget(QLabel("标题"), 1, 0)
        grid.addWidget(QLineEdit(), 1, 1)

        grid.addWidget(QLabel('提交人'), 2, 0)
        grid.addWidget(QLineEdit(), 2, 1)

        grid.addWidget(QLabel("申告内容"), 3, 0)
        grid.addWidget(QTextEdit(), 3, 1, 5, 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
