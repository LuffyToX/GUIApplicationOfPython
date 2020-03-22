# -*- coding: utf-8 -*-
# QHBoxLayout 水平布局管理器的使用


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 300, 100)

        # 水平布局（从左到右添加控件）
        hbox = QHBoxLayout()
        for i in range(1, 6):
            hbox.addWidget(QPushButton(str(i)))
        # 设置控件间的间距
        # hbox.setSpacing(0)
        self.setLayout(hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
