# -*- coding: utf-8 -*-
# 不规则窗口


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QBitmap


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 600, 500)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, 280, 390, QPixmap(r"./images/dog.jpg"))
        painter.drawPixmap(300, 0, 280, 390, QBitmap(r"./images/dog.jpg"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
