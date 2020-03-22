# -*- coding: utf-8 -*-
# QVBoxLayout 垂直布局管理器


import sys
from PyQt5.QtWidgets import QApplication  ,QWidget ,QVBoxLayout , QPushButton


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setGeometry(800, 300, 200, 300)

        # 垂直布局（从上到下添加控件）
        vbox = QVBoxLayout()
        for i in range(1, 6):
            vbox.addWidget(QPushButton(str(i)))
        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
