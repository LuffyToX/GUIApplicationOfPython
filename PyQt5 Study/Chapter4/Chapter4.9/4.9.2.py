# -*- coding: utf-8 -*-
# QMessageBox 的使用


import sys
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("MainWindow")
        self.resize(300, 100)

        self.btn = QPushButton(self)
        self.btn.setText("点击弹出消息框")
        self.btn.clicked.connect(self.msg)

    def msg(self):
        """ 使用消息对话框 """
        QMessageBox.information(self, "标题", "对话框消息正文", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
