# -*- coding: utf-8 -*-
# QTimer 的使用2


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Timer")
        self.setGeometry(800, 300, 300, 100)

        label = QLabel("此窗口会在 5 秒后消失!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        # 设置 5s 后自动退出
        timer = QTimer()
        timer.singleShot(5000, app.quit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
