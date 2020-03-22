# -*- coding: utf-8 -*-
# QThread 在 UI 界面中分离 UI 主线程与工作线程


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class WorkThread(QThread):
    trigger = pyqtSignal()

    def __int__(self):
        super().__init__()

    def run(self):
        for i in range(2000000000):
            pass
        # 循环完毕后发出信号
        self.trigger.emit()


class MainWindow(QWidget):
    sec = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Thread")
        self.resize(300, 120)

        # LCD显示屏
        self.lcdNumber = QLCDNumber()

        # 按钮
        self.button = QPushButton("测试")
        self.button.clicked.connect(self.work)

        # 每次计时结束，触发 countTime
        self.timer = QTimer()
        self.timer.timeout.connect(self.countTime)

        # 工作线程
        self.workThread = WorkThread()

        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.lcdNumber)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def countTime(self):
        # LED显示数字+1
        self.sec += 1
        self.lcdNumber.display(self.sec)

    def work(self):
        self.timer.start(1000)                           # 计时器每秒计数
        self.workThread.start()                          # 计时开始
        self.workThread.trigger.connect(self.timeStop)   # 当获得循环完毕的信号时，停止计数

    def timeStop(self):
        self.timer.stop()
        print("运行结束用时", self.lcdNumber.value())
        self.sec = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
