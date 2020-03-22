# -*- coding: utf-8 -*-
# 装饰器信号与槽


from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QMessageBox
import sys


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 300, 200)

        # 使用 setObjectName() 方法设置对象名称
        self.okButton = QPushButton("OK", self)
        self.okButton.setObjectName("okButton")

        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        self.setLayout(layout)

        # 信号自动连接到槽函数的核心代码
        QtCore.QMetaObject.connectSlotsByName(self)

    # 通过装饰器的方式定义槽函数
    # on_发送者对象名_信号名
    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        QMessageBox.information(self, "信息提示框", "'ok' clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
