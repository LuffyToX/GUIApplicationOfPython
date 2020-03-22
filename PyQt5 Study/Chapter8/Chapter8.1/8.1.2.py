# -*- coding: utf-8 -*-
# 设置窗口样式


from PyQt5.QtCore import Qt
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(800, 300, 500, 300)

        # 窗口样式：窗口无边框
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 加载图片
        self.setObjectName("MainWindow")
        self.setStyleSheet("#MainWindow{border-image:url(images/python.jpg);}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
