# -*- coding: utf-8 -*-
# paintEvent 使用 QPaint 绘制背景色


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 600, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.yellow)
        # 设置背景色
        painter.drawRect(self.rect())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
