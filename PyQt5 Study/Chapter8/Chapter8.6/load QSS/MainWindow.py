# -*- coding: utf-8 -*-
# 加载 QSS 文件


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton
from loadQSS import LoadQss


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 600, 400)

        btn = QPushButton("添加")
        btn.setToolTip("测试提示")

        vbox = QVBoxLayout()
        vbox.addWidget(btn)
        self.setLayout(vbox)

        # 加载 QSS 样式文件
        styleFile = './style.qss'
        qssStyle = LoadQss.readQss(styleFile)
        self.setStyleSheet(qssStyle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())



