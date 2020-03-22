# -*- coding: utf-8 -*-
# 布局管理器

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from MainWin03 import Ui_LayoutManage


class LayoutManage(QMainWindow, Ui_LayoutManage):
    def __init__(self, parent=None):
        super(LayoutManage, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        """ pushButton_start 是 '开始' 按钮的 objectName """
        print('收益_min：', self.doubleSpinBox_returns_min.text())
        print('收益_max：', self.doubleSpinBox_returns_max.text())
        print('最大回撤_min：', self.doubleSpinBox_maxdrawdown_min.text())
        print('最大回撤_max：', self.doubleSpinBox_maxdrawdown_max.text())
        print('sharp比_min：', self.doubleSpinBox_sharp_min.text())
        print('sharp比_max：', self.doubleSpinBox_sharp_max.text())


if __name__ == "__main__":
    # 下面这行代码可以确保运行界面与 Qt Designer 预览界面一致
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    ui = LayoutManage()
    ui.show()
    sys.exit(app.exec())