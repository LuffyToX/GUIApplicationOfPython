# coding:utf-8 -*-
# 双缓冲绘图 绘制矩形，避免出现重影


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QPoint


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()
        self.initUi()

        self.tempPix = QPixmap()                     # 辅助画布
        self.isDrawing = False                       # 标志是否正在绘图

    def initUi(self):
        self.setWindowTitle("Paint")                 # 窗口标题
        self.setGeometry(800, 300, 600, 500)         # 窗口大小
        self.pix = QPixmap(500, 400)                 # 画布大小
        self.pix.fill(Qt.white)                      # 画布背景

    def paintEvent(self, event):
        painter = QPainter(self)
        x = self.lastPoint.x()
        y = self.lastPoint.y()
        w = self.endPoint.x() - x
        h = self.endPoint.y() - y

        # 如果正在绘图，就在辅助画布上绘制
        if self.isDrawing:
            # 将以前 pix 中的内容复制到 tempPix 中，保证以前的内容不消失
            self.tempPix = self.pix
            pp = QPainter(self.tempPix)
            pp.drawRect(x, y, w, h)
            painter.drawPixmap(0, 0, self.tempPix)
        else:
            pp = QPainter(self.pix)
            pp.drawRect(x, y, w, h)
            painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, event):
        # 鼠标左键按下
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint
            # 正在绘制
            self.isDrawing = True

    def mouseReleaseEvent(self, event):
        # 鼠标左键释放
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # 刷新界面（执行 paintEvent）
            self.update()
            self.isDrawing = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())



