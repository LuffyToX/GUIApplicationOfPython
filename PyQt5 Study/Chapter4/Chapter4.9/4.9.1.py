# -*- coding: utf-8 -*-
# QDialog 的使用


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.resize(350, 300)

        # 如果不为控件指定一个父对象（self），那么该控件将被当作窗口处理
        self.btn = QPushButton(self)
        self.btn.setText("弹出对话框")
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.showdialog)

    @staticmethod
    def showdialog():
        dialog = QDialog()
        btn = QPushButton("ok", dialog)                # 这里为按钮控件指定了父对象 dialog
        btn.move(50, 50)                               # 相对于 dialog 窗口的位置
        dialog.setWindowTitle("Dialog")                # 设置 dialog 的标题
        dialog.setWindowModality(Qt.ApplicationModal)  # 设置窗口模态  ==>  不和其他任何窗口交互
        dialog.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
