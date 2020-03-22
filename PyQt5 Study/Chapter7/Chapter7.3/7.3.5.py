# -*- coding: utf-8 -*-
# 多线程 信号与槽的使用


import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout
from PyQt5.QtCore import QThread, pyqtSignal


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 400, 300)

        vbox = QVBoxLayout(self)
        self.listWidget = QListWidget()
        vbox.addWidget(self.listWidget)

        # 创建一个线程实例并连接槽函数 outText
        self.td = MyThread("thread1", 6)
        self.td.sinOut.connect(self.outText)
        self.td.start()

    def outText(self, text):
        self.listWidget.addItem(text)


class MyThread(QThread):
    # 带 str 参数的信号
    sinOut = pyqtSignal(str)

    def __init__(self, identity, value, parent=None):
        super(MyThread, self).__init__(parent)

        self.identity = identity    # 线程名称
        self.times = value          # 线程运行时间

    def run(self):
        while self.times > 0 and self.identity:
            # 发射信号
            self.sinOut.emit(self.identity + " ==> " + str(self.times))
            time.sleep(1)
            self.times -= 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
