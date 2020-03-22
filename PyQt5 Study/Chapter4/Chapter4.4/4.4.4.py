# -*- coding: utf-8 -*-
# QLineEdit 综合示例

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt
import sys


class Dialog(QWidget):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        pLineEdit1 = QLineEdit()
        pLineEdit1.setValidator(QIntValidator())             # 设置校验器 => 整型
        pLineEdit1.setMaxLength(4)                           # 设置允许输入字符的最大长度
        pLineEdit1.setAlignment(Qt.AlignRight)               # 居右显示
        pLineEdit1.setFont(QFont("Arial", 15))               # 设置字体

        pLineEdit2 = QLineEdit()
        pLineEdit2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        pLineEdit3 = QLineEdit()
        pLineEdit3.setInputMask('+99_9999_999999')           # 设置掩码

        pLineEdit4 = QLineEdit()
        pLineEdit4.textChanged.connect(self.textchanged)     # 当修改文本内容时，这个信号会被发射

        pLineEdit5 = QLineEdit()
        pLineEdit5.setEchoMode(QLineEdit.Password)           # 设置文本框显示格式 => 显示与平台相关的掩码字符
        pLineEdit5.editingFinished.connect(self.enterPress)  # 当结束编辑文本时，这个信号会被发射

        pLineEdit6 = QLineEdit("Hello PyQt5")
        pLineEdit6.setReadOnly(True)                         # 设置文本框为只读

        # 表单布局
        flo = QFormLayout()
        flo.addRow("integer validator", pLineEdit1)
        flo.addRow("Double validator", pLineEdit2)
        flo.addRow("Input Mask", pLineEdit3)
        flo.addRow("Text changed", pLineEdit4)
        flo.addRow("Password", pLineEdit5)
        flo.addRow("Read Only", pLineEdit6)
        self.setLayout(flo)

    @staticmethod
    def textchanged(text):
        print("输入的内容为: " + text)

    @staticmethod
    def enterPress():
        print("已输入值")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
