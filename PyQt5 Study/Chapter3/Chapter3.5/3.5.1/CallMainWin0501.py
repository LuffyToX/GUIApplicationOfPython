# -*- coding: utf-8 -*-
# 菜单栏与工具栏

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from MainWin0501 import Ui_MainWindow


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        # 菜单的点击事件：当点击关闭菜单时，连接槽函数 close()
        self.fileCloseAction.triggered.connect(self.close)

        # 菜单的点击事件：当点击打开菜单时，来连接槽函数 openMsg()
        self.fileOpenAction.triggered.connect(self.openMsg)

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:\\", "All Files (*);;Text Files (*.txt)")
        # 在状态栏显示文件地址
        self.statusbar.showMessage(file)


if __name__ == "__main__":
    # 下面这行代码可以确保运行界面与 Qt Designer 预览界面一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())