# -*- coding: utf-8 -*-
# 单线程长时间读取数据造成界面卡死


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    sec = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Thread")
        self.setGeometry(800, 300, 300, 120)

        # LCD显示屏
        self.lcdNumber = QLCDNumber()

        # 按钮
        self.button = QPushButton("测试")
        self.button.clicked.connect(self.work)

        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.lcdNumber)
        layout.addWidget(self.button)
        self.setLayout(layout)

        # 每次计时结束，触发setTime
        self.timer = QTimer()
        self.timer.timeout.connect(self.setTime)

    def setTime(self):
        # LED显示数字 +1
        self.sec += 1
        self.lcdNumber.display(self.sec)

    def work(self):
        # 计时器每秒计数
        self.timer.start(1000)
        for i in range(2000000000):
            pass
        self.timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
