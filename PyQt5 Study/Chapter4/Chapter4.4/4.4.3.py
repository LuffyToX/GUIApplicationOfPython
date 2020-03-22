# -*- coding: utf-8 -*-
# 输入掩码

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
import sys


class Dialog(QWidget):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")
        pIP = QLineEdit()               # 掩码：IP 掩码
        pMAC = QLineEdit()              # 掩码：MAC 掩码
        pDate = QLineEdit()             # 掩码：日期掩码
        pLicense = QLineEdit()          # 掩码：许可证掩码

        # 表单布局
        flo = QFormLayout()
        flo.addRow("数字掩码", pIP)
        flo.addRow("Mac掩码", pMAC)
        flo.addRow("日期掩码", pDate)
        flo.addRow("许可证掩码", pLicense)
        self.setLayout(flo)

        # 设置掩码
        pIP.setInputMask("000.000.000.000;_")
        pMAC.setInputMask("HH:HH:HH:HH:HH:HH;_")
        pDate.setInputMask("0000-00-00")
        pLicense.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
