# -*- coding: utf-8 -*-
# QPen 的使用


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MainWindow')
        self.setGeometry(900, 300, 350, 300)

    def paintEvent(self, event):
        """
        绘制事件，所有的绘制操作都发生在此事件中
        """
        painter = QPainter()                    # 新建 QPinter() 方法
        painter.begin(self)                     # 开始绘制
        self.drawLines(painter)                 # 自定义绘制方法
        painter.end()                           # 结束绘制

    @staticmethod
    def drawLines(qp):
        """ 画线 """

        pen = QPen(Qt.black, 2, Qt.SolidLine)   # 新建一个 QPen(画笔颜色, 画笔宽度, 样式) 对象

        qp.setPen(pen)                          # 设置用于绘制的笔的颜色、大小、样式
        qp.drawLine(20, 40, 250, 40)            # 画线：(20, 40) -> (250, 40)

        pen.setStyle(Qt.DashLine)               # 设置画笔的样式 => 由一些像素分隔的短线
        qp.setPen(pen)                          # 设置用于绘制的笔的颜色、大小、样式
        qp.drawLine(20, 80, 250, 80)            # 画线：(20, 80) -> (250, 80)

        pen.setStyle(Qt.DashDotLine)            # 设置画笔的样式 => 轮流交替的点和短线
        qp.setPen(pen)                          # 设置用于绘制的笔的颜色、大小、样式
        qp.drawLine(20, 120, 250, 120)          # 画线：(20, 120) -> (250, 120)

        pen.setStyle(Qt.DotLine)                # 设置画笔的样式 => 由一些像素分隔的点
        qp.setPen(pen)                          # 设置用于绘制的笔的颜色、大小、样式
        qp.drawLine(20, 160, 250, 160)          # 画线：(20, 160) -> (250, 160)

        pen.setStyle(Qt.DashDotDotLine)         # 设置画笔的样式 => 一条短线，两个点
        qp.setPen(pen)                          # 设置用于绘制的笔的颜色、大小、样式
        qp.drawLine(20, 200, 250, 200)          # 画线：(20, 200) -> (250, 200)

        pen.setStyle(Qt.CustomDashLine)         # 设置自定义线条样式
        pen.setDashPattern([1, 4, 5, 4])        # 使用数字列表定义样式（奇数列：横线；偶数列：横线间隔）
        qp.setPen(pen)                          # 设置用于绘制的笔的颜色、大小、样式
        qp.drawLine(20, 240, 250, 240)          # 画线：(20, 240) -> (250, 240)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
