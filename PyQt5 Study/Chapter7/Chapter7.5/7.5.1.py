# -*- coding: utf-8 -*-
# 单一窗口数据传递


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 400, 200)

        # 创建 LCD 和水平滑块
        lcd = QLCDNumber(self)
        slider = QSlider(Qt.Horizontal, self)

        # 垂直布局
        vBox = QVBoxLayout()
        vBox.addWidget(lcd)
        vBox.addWidget(slider)
        self.setLayout(vBox)

        # 只要 slider 的值发生改变，它就会发射一个信号
        slider.valueChanged.connect(lcd.display)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
