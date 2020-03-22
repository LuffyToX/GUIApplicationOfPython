# -*- coding: utf-8 -*-
# 绘制点


import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.resize(400, 300)

    def paintEvent(self, event):
        """
        绘制事件，所有的绘制操作都发生在此事件中 """

        painter = QPainter()              # 新建 QPainter() 方法
        painter.begin(self)               # 开始绘制
        self.drawPoints(painter)          # 自定义绘制方法
        painter.end()                     # 结束绘制

    def drawPoints(self, qp):
        qp.setPen(Qt.red)                 # 设置画笔颜色
        size = self.size()                # 获取窗口大小

        # 正弦图像
        for i in range(1000):
            x = 100 * (-1 + 2.0 * i / 1000) + size.width() / 2.0
            y = -50 * math.sin((x - size.width() / 2.0) * math.pi / 50) + size.height() / 2.0
            qp.drawPoint(x, y)            # 绘制点


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
