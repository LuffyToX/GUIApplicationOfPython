# -*- coding: utf-8 -*-
# paintEvent 使用 QPaint 绘制背景图片


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QPainter


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 600, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("./images/screen.jpg")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
