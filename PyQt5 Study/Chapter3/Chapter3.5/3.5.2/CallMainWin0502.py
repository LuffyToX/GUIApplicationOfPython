# -*- coding: utf-8 -*-
# 调用窗体

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from MainWin0502 import Ui_MainWindow
from ChildrenWin0502 import Ui_ChildrenForm


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        self.child = ChildrenForm()  # 生成子窗口实例

        # 菜单的点击事件：当单击关闭菜单时，连接槽函数 close()
        self.fileCloseAction.triggered.connect(self.close)

        # 菜单的点击事件：当单击打开菜单时，连接槽函数 openMsg()
        self.fileOpenAction.triggered.connect(self.openMsg)

        # 单击 "添加窗体"，子窗口就会显示在主窗口的 MainGridLayout 中
        self.addWinAction.triggered.connect(self.childShow)

    def childShow(self):
        """ 添加子窗口 """
        if __name__ == '__main__':
            self.MainGridLayout.addWidget(self.child)
            self.child.show()

    def openMsg(self):
        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:\\", "All Files (*);;Text Files (*.txt)")
        # 在状态栏显示文件地址
        self.statusbar.showMessage(file)


class ChildrenForm(QWidget, Ui_ChildrenForm):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    # 下面这行代码可以确保运行界面与 Qt Designer 预览界面一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

