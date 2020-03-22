# -*- coding: utf-8 -*-
# 校验器

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys


class Dialog(QWidget):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")
        pInt = QLineEdit()               # 校验器：限制输入整数
        pDouble = QLineEdit()            # 校验器：限制输入浮点数
        pRegexp = QLineEdit()            # 校验器：检查输入是否符合正则表达式

        # 表单布局管理器
        flo = QFormLayout()
        flo.addRow("整形", pInt)
        flo.addRow("浮点型", pDouble)
        flo.addRow("字母和数字", pRegexp)
        self.setLayout(flo)

        # 设置文本框浮显文字
        pInt.setPlaceholderText("整形")
        pDouble.setPlaceholderText("浮点型")
        pRegexp.setPlaceholderText("字母和数字")

        # 整型 范围：[1, 99]
        pIntValidator = QIntValidator(self)
        pIntValidator.setRange(1, 99)

        # 浮点型 范围：[-360, 360] 精度：小数点后2位
        pDoubleValidator = QDoubleValidator(self)
        pDoubleValidator.setRange(-360, 360)
        pDoubleValidator.setNotation(QDoubleValidator.StandardNotation)
        pDoubleValidator.setDecimals(2)

        # 字符和数字
        reg = QRegExp("[a-zA-Z0-9]+$")
        pRegExpValidator = QRegExpValidator(self)
        pRegExpValidator.setRegExp(reg)

        # 设置验证器
        pInt.setValidator(pIntValidator)
        pDouble.setValidator(pDoubleValidator)
        pRegexp.setValidator(pRegExpValidator)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
