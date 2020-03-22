# -*- coding: utf-8 -*-
# 信号与槽的入门应用 内置信号与槽的使用


from PyQt5.QtWidgets import QPushButton, QApplication, QWidget
from PyQt5.QtWidgets import QMessageBox
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 300, 200)

        self.btn = QPushButton("按钮", self)

        # 将内置信号链接到自定义槽函数
        self.btn.clicked.connect(self.showMsg)

    def showMsg(self):
        QMessageBox.information(self, "信息提示框", "ok，弹出测试信息")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
