# -*- coding: utf-8 -*-
# 自定义信号与内置槽函数


from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
import sys


class MainWindow(QWidget):
    # 自定义信号，不带参数
    # 必须放在类全局域中
    button_clicked_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 300, 200)

        self.btn = QPushButton('关闭', self)

        # 将内置信号链接到自定义槽函数
        # 该槽函数为了发射自定义信号
        self.btn.clicked.connect(self.btn_clicked)

        # 将自定义信号链接到内置槽函数
        self.button_clicked_signal.connect(self.close)

    def btn_clicked(self):
        # 发送自定义信号，无参数
        self.button_clicked_signal.emit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
