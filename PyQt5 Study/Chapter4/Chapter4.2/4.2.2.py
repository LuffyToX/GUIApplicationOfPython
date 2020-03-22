# -*- coding: utf-8 -*-
# 为应用设置程序图标


import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QIcon


class Icon(QWidget):
    """ 窗口类 """
    def __init__(self, parent=None):
        super(Icon, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        """ 初始化窗口 """
        self.setGeometry(300, 300, 1000, 600)       # 设置窗口位置及大小
        self.setWindowTitle('MainWindow')           # 设置窗口标题

        # 设置窗口图标  ==>
        #                   SetWindowIcon(QIcon())
        #                   QIcon(icon_path)
        self.setWindowIcon(QIcon(r".\images\10.ico"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Icon()
    win.show()
    sys.exit(app.exec_())