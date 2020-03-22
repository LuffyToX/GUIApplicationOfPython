# -*- coding: utf-8 -*-
# QRadioButton 按钮的使用

import sys
from PyQt5.QtWidgets import *


class Dialog(QWidget):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        # 如果改变单选钮状态（on <=> off），将触发 toggled 信号
        # 将单选钮 rbtn1 设置成默认被选中状态
        self.rbtn1 = QRadioButton("RadioButton1")
        self.rbtn1.setChecked(True)
        self.rbtn1.toggled.connect(lambda: self.btnstate(self.rbtn1))

        self.rbtn2 = QRadioButton("RadioButton2")
        self.rbtn2.toggled.connect(lambda: self.btnstate(self.rbtn2))

        # 水平布局
        layout = QHBoxLayout()
        layout.addWidget(self.rbtn1)
        layout.addWidget(self.rbtn2)
        self.setLayout(layout)

    @staticmethod
    def btnstate(rbtn):
        if rbtn.text() == "RadioButton1":
            if rbtn.isChecked():
                print(rbtn.text() + " is selected")
            else:
                print(rbtn.text() + " is deselected")

        if rbtn.text() == "RadioButton2":
            if rbtn.isChecked():
                print(rbtn.text() + " is selected")
            else:
                print(rbtn.text() + " is deselected")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
