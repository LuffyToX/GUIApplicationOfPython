# -*- coding: utf-8 -*-
# 使用自定义参数 partial 函数


import sys
from PyQt5.QtWidgets import *
from functools import partial


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 300, 200)

        button1 = QPushButton('Button 1')
        button2 = QPushButton('Button 2')

        # clicked 信号本身不传递参数
        # 使用 partial() 传递参数
        button1.clicked.connect(partial(self.onButtonClick, 1))
        button2.clicked.connect(partial(self.onButtonClick, 2))

        layout = QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)

        main_frame = QWidget()
        main_frame.setLayout(layout)
        self.setCentralWidget(main_frame)

    def onButtonClick(self, n):
        QMessageBox.information(self, "信息提示框", 'Button {0} clicked'.format(n))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
