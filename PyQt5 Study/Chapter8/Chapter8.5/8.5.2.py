# -*- coding: utf-8 -*-
# 不规则窗口


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QBitmap


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.move(800, 300)
        self.pix = QBitmap("./images/mask.png")    # 遮罩图片
        self.resize(self.pix.size())               # 将窗口设置为与遮罩同大
        self.setMask(self.pix)                     # 为 MainWindow 增加一个遮罩

    def paintEvent(self, event):
        painter = QPainter(self)
        # 在指定区域直接绘制窗口背景
        painter.drawPixmap(0, 0, self.pix.width(), self.pix.height(), QPixmap("./images/screen.jpg"))
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        # painter.drawPixmap(0, 0, self.width(), self.height(), QPixmap("./images/screen1.jpg"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
