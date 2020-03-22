# -*- coding: utf-8 -*-
# QScrollBar 的使用


import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 300, 200)

        self.l1 = QLabel("拖动滑动条去改变颜色")
        self.l1.setFont(QFont("Arial", 16))               # 设置标签字体、大小

        self.s1 = QScrollBar()                            # 新建滑块
        self.s1.setMaximum(255)                           # 设置滑块最大值
        self.s1.sliderMoved.connect(self.sliderval)       # 将滑动信号关联到槽函数

        self.s2 = QScrollBar()
        self.s2.setMaximum(255)
        self.s2.sliderMoved.connect(self.sliderval)

        self.s3 = QScrollBar()
        self.s3.setMaximum(255)
        self.s3.sliderMoved.connect(self.sliderval)

        # 水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(self.l1)
        hbox.addWidget(self.s1)
        hbox.addWidget(self.s2)
        hbox.addWidget(self.s3)
        self.setLayout(hbox)

    def sliderval(self):
        # 输出当前三个滑块位置所代表的值
        print(self.s1.value(), self.s2.value(), self.s3.value())

        # 实例化调色板对象，将 RGB 设为三个滑块的值
        palette = QPalette()
        c = QColor(self.s1.value(), self.s2.value(), self.s3.value(), 255)
        palette.setColor(QPalette.Foreground, c)

        # 设置标签的调色板，加载属性
        self.l1.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
