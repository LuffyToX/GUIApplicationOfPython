# -*- coding: utf-8 -*-
# QStackedWidget 的使用


import sys
from PyQt5.QtWidgets import *


class StackWidget(QWidget):
    def __init__(self):
        super(StackWidget, self).__init__()

        self.setGeometry(800, 300, 30, 10)
        self.setWindowTitle("StackWidget")

        # 添加条目
        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, '联系方式')
        self.leftlist.insertItem(1, '个人信息')
        self.leftlist.insertItem(2, '教育程度')

        # 新建窗体
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        # 将窗体添加到堆栈窗口控件中
        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)

        # 水平布局
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)
        self.setLayout(hbox)

        # 加载各窗口
        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

        # QStackedWidget 控件不能在页面之间切换
        # 它与当前选中的 QListWidget 控件中的选项链接
        self.leftlist.currentRowChanged.connect(self.display)

    def stack1UI(self):
        # 表单布局
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.stack1.setLayout(layout)

    def stack2UI(self):
        # 水平布局
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        # 表单布局
        layout = QFormLayout()
        layout.addRow(QLabel("性别"), sex)
        layout.addRow("生日", QLineEdit())
        self.stack2.setLayout(layout)

    def stack3UI(self):
        # 水平布局
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.stack3.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = StackWidget()
    win.show()
    sys.exit(app.exec_())
