# coding:utf-8 -*-
# 双缓冲绘图 绘制矩形，出现重影


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

    def initUi(self):
        self.setWindowTitle("Paint")              # 窗口标题
        self.setGeometry(800, 300, 600, 500)      # 窗口大小
        self.pix = QPixmap(500, 400)              # 画布大小
        self.pix.fill(Qt.white)                   # 画布背景

    def paintEvent(self, event):
        painter = QPainter(self)
        x = self.lastPoint.x()
        y = self.lastPoint.y()
        w = self.endPoint.x() - x
        h = self.endPoint.y() - y

        pp = QPainter(self.pix)
        pp.drawRect(x, y, w, h)
        painter.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, event):
        # 鼠标左键按下
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint

    def mouseMoveEvent(self, event):
        # 鼠标左键按下的同时移动鼠标
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            # 刷新界面（执行 paintEvent）
            self.update()

    def mouseReleaseEvent(self, event):
        # 鼠标左键释放
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # 刷新界面（执行 paintEvent）
            self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())



