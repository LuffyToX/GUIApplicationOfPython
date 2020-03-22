# -*- coding: utf-8 -*-
# QSS 设置窗口背景图片


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 600, 400)
        self.setObjectName("MainWindow")

        # 设置背景图片
        qss_style = " #MainWindow{border-image:url(./images/python.jpg)} "
        self.setStyleSheet(qss_style)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
