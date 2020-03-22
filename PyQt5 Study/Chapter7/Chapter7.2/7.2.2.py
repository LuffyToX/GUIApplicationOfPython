# -*- coding: utf-8 -*-
# 内置信号与自定义槽函数


from PyQt5.QtWidgets import *
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 300, 200)

        btn = QPushButton('关闭', self)

        # 将内置信号链接到自定义槽函数
        btn.clicked.connect(self.btn_close)

    def btn_close(self):
        # 自定义槽函数
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
