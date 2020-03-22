# -*- coding: utf-8 -*-
# QHBoxLayout 设置控件对齐方式


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.resize(300, 100)

        # 水平布局
        hbox = QHBoxLayout()
        # 伸缩量为0，且水平居左、垂直居上
        hbox.addWidget(QPushButton(str(1)), 0, Qt.AlignLeft | Qt.AlignTop)
        hbox.addWidget(QPushButton(str(2)), 0, Qt.AlignLeft | Qt.AlignTop)
        hbox.addWidget(QPushButton(str(3)))
        # 伸缩量为0，且水平居左、垂直居下
        hbox.addWidget(QPushButton(str(4)), 0, Qt.AlignLeft | Qt.AlignBottom)
        hbox.addWidget(QPushButton(str(5)), 0, Qt.AlignLeft | Qt.AlignBottom)
        self.setLayout(hbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())