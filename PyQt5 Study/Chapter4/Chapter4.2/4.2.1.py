# -*- coding: utf-8 -*-
# 屏幕坐标系统显示


import sys
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('MainWindow')
        self.resize(800, 600)                         # 设置客户区大小
        self.move(600, 500)                           # 以屏幕左上角为 (0, 0)

        # 如果这里不传入参数 self，就会被当作窗口
        self.btn1 = QPushButton('QWidget')
        self.btn2 = QPushButton('QWidge.geometry')
        self.btn3 = QPushButton('QWidge.frameGeometry')
        self.lst = QListWidget()

        # 水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn3)

        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.lst)
        self.setLayout(vbox)

        self.btn1.clicked.connect(self.btn1Print)
        self.btn2.clicked.connect(self.btn2Print)
        self.btn3.clicked.connect(self.btn3Print)

    def btn1Print(self):
        self.lst.clear()
        items = [
            "窗口 x 坐标：QWidget.x() = %d\n" % self.x(),
            "窗口 y 坐标：QWidget.y() = %d\n" % self.y(),
            "客户区宽度：QWidget.width() = %d\n" % self.width(),
            "客户区高度：QWidget.height() = %d" % self.height()
        ]
        self.lst.addItems(items)

    def btn2Print(self):
        self.lst.clear()
        items = [
            "客户区 x 坐标：QWidget.geometry().x() = %d\n" % self.geometry().x(),
            "客户区 y 坐标：QWidget.geometry().y() = %d\n" % self.geometry().y(),
            "客户区宽度：QWidget.geometry().width() = %d\n" % self.geometry().width(),
            "客户区高度：QWidget.geometry().height() = %d" % self.geometry().height()
        ]
        self.lst.addItems(items)

    def btn3Print(self):
        self.lst.clear()
        items = [
            "窗口 x 坐标：Widge.frameGeometry().x() = %d\n" % self.frameGeometry().x(),
            "窗口 y 坐标：Widge.frameGeometry().y() = %d\n" % self.frameGeometry().y(),
            "窗口宽度：Widge.frameGeometry().width() = %d\n" % self.frameGeometry().width(),
            "窗口高度：Widge.frameGeometry().height() = %d" % self.frameGeometry().height()
        ]
        self.lst.addItems(items)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
