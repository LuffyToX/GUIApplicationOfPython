# -*- coding: utf-8 -*-
# 绘制文字


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")                         # 窗口标题
        self.resize(400, 300)                                     # 窗口大小
        self.text = "猪猪猪猪猪"                                   # 待绘制的文字

    def paintEvent(self, event):
        """
        绘制事件，所有的绘制操作都发生在此事件中 """

        painter = QPainter(self)                                  # 新建 Painter() 对象
        painter.begin(self)                                       # 开始绘制
        self.drawText(event, painter)                             # 自定义绘制方法
        painter.end()                                             # 结束绘制

    def drawText(self, event, qp):
        qp.setPen(QColor(168, 34, 3))                             # 设置笔的颜色
        qp.setFont(QFont('SimSun', 20))                           # 设置字体
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)      # 绘制文本


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
