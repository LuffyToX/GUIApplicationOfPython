# -*- coding: utf-8 -*-
# QTabWidget 的使用


import sys
from PyQt5.QtWidgets import *


class TabWidget(QTabWidget):
    # 注意这里继承的是 QTabWidget
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)

        self.setWindowTitle("TabWidget")
        self.resize(300, 100)

        # 新建窗体
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        # 将窗体控件添加到选项卡中
        # 第二个参数可以指定选项卡文本值
        self.addTab(self.tab1, "Tab1")
        self.addTab(self.tab2, "Tab2")
        self.addTab(self.tab3, "Tab3")

        # 加载各选项卡
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def tab1UI(self):
        # 表单布局
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.tab1.setLayout(layout)
        # 设置选项卡的文本值
        # 第一个参数为选项卡的索引
        # self.setTabText(0, "联系方式")

    def tab2UI(self):
        # 水平布局
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        # 表单布局
        layout = QFormLayout()
        layout.addRow(QLabel("性别"), sex)
        layout.addRow("生日", QLineEdit())
        self.tab2.setLayout(layout)
        # self.setTabText(1, "个人详细信息")

    def tab3UI(self):
        # 水平布局
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.tab3.setLayout(layout)
        # self.setTabText(2, "教育程度")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TabWidget()
    win.show()
    sys.exit(app.exec_())
