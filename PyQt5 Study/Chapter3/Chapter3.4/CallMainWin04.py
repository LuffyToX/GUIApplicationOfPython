# -*- coding: utf-8 -*-
# 信号/槽

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWin04 import Ui_Form


class SignalSlot(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(SignalSlot, self).__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    # 下面这行代码可以确保运行界面与 Qt Designer 预览界面一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    myWin = SignalSlot()
    myWin.show()
    sys.exit(app.exec_())