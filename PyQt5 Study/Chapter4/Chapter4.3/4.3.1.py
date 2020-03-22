# -*- coding: utf-8 -*-
# QLabel 标签快捷键的使用


import sys
from PyQt5.QtWidgets import *


class Dialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog")

        pLabel1 = QLabel('&Name')              # Alt + N（'&'）
        pLineEdit1 = QLineEdit()
        pLabel1.setBuddy(pLineEdit1)           # 设置伙伴关系 => QLabel 必须是文本内容并使用 '&' 符号设置了助记符

        pLabel2 = QLabel('&Password')          # Alt + P（'&'）
        pLineEdit2 = QLineEdit()
        pLabel2.setBuddy(pLineEdit2)           # 设置伙伴关系

        pButtonOk = QPushButton('&OK')         # Alt + O（'&'）
        pButtonCancle = QPushButton('Cancel')  # Alt + C（'&'）

        """
        布局管理器  ==>
                        水平布局管理器：QHBoxLayout
                        垂直布局管理器：QVBoxLayout
                        栅格布局管理器：QGridLayout
                        表单布局管理器：QFormLayout
        
        addWidget(QWidget widget, Row, Column, rowSpan, columnSpan, Qt.Alignment)
        QWidget widget：           需要添加的控件
        Row：                      控件所在行
        Column：                   控件所在列
        rowSpan：                  控件所在行数
        columnSpan：               控件所在列数
        Qt.Alignment：             控件对齐方式  
        """
        # 栅格布局
        layout = QGridLayout(self)
        layout.addWidget(pLabel1, 0, 0)
        layout.addWidget(pLineEdit1, 0, 1, 1, 2)
        layout.addWidget(pLabel2, 1, 0)
        layout.addWidget(pLineEdit2, 1, 1, 1, 2)
        layout.addWidget(pButtonOk, 2, 1)
        layout.addWidget(pButtonCancle, 2, 2)

        # 如果 layout = QGridLayout() 没有传递 self 参数
        # 那么 layout 添加完控件之后要调用：self.setLayout(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())