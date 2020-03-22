# -*- coding: utf-8 -*-
# EchoMode 的显示效果

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
import sys


class Dialog(QWidget):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")
        pNormal = QLineEdit()              # 文本框：正常显示所输入的字符（默认情形）
        pNoEcho = QLineEdit()              # 文本框：不显示任何输入的字符，常用于密码类型的输入
        pPassword = QLineEdit()            # 文本框：显示与平台相关的密码掩码字符，而不是实际输入的字符
        pPasswordEchoOnEdit = QLineEdit()  # 文本框：在编辑时显示字符，编辑后显示与平台相关的密码掩码字符

        """
        表单布局管理器 QFormLayout 可以看作是只有两列的 QGridLayout：
        
                                                   第一列：标签域 => label
                                                   第二列：字段域 => field   
        addRow(label, field)
                              label：标签域  =>  显示类控件/字符串
                              field：字段域  =>  输入类控件
        """
        flo = QFormLayout()
        flo.addRow("Normal", pNormal)
        flo.addRow("NoEcho", pNoEcho)
        flo.addRow("Password", pPassword)
        flo.addRow("PasswordEchoOnEdit", pPasswordEchoOnEdit)
        self.setLayout(flo)

        # 设置文本框浮显文字
        pNormal.setPlaceholderText("Normal")
        pNoEcho.setPlaceholderText("NoEcho")
        pPassword.setPlaceholderText("Password")
        pPasswordEchoOnEdit.setPlaceholderText("PasswordEchoOnEdit")

        # 设置文本显示格式
        pNormal.setEchoMode(QLineEdit.Normal)
        pNoEcho.setEchoMode(QLineEdit.NoEcho)
        pPassword.setEchoMode(QLineEdit.Password)
        pPasswordEchoOnEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())

