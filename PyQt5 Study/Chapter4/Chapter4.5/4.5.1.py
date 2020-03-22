# -*- coding: utf-8 -*-
# QPushButton 按钮的使用


import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        # QPushButton.setCheckable(True)  ==>  将按钮设置成可以被选中
        # 执行以上代码后的按钮有两种状态：'被选中' 和 '未被选中'，可通过点击按钮来切换这两种状态
        # '被选中' 状态  =>  isChecked() 返回 True
        # '未被选中' 状态  =>  isChecked() 返回 False
        # QPushButton.toggle()  ==>  换按钮的状态：'被选中' <=> '未被选中'
        self.btn1 = QPushButton("Button1")
        self.btn1.setCheckable(True)              # 按钮初始状态为 '未被选中'
        self.btn1.toggle()                        # 将按钮状态切换为 '被选中'
        self.btn1.clicked.connect(self.btnstate)

        self.btn2 = QPushButton('image')
        self.btn2.setIcon(QIcon(QPixmap(r".\images\0.ico")))
        self.btn2.clicked.connect(lambda: self.whichbtn(self.btn2))  # 通过 lambda 方式传递额外参数

        self.btn3 = QPushButton("Disabled")
        self.btn3.setEnabled(False)         # 设置按钮是否可以被点击 False => 该按钮不可被点击

        self.btn4 = QPushButton("&Download")
        self.btn4.setDefault(True)          # True => 设置为默认按钮（回车，空格键也可触发）
        self.btn4.clicked.connect(lambda: self.whichbtn(self.btn4))

        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)
        layout.addWidget(self.btn3)
        layout.addWidget(self.btn4)
        self.setLayout(layout)

    def btnstate(self):
        if self.btn1.isChecked():           # 返回按钮的状态：'按下'/'未按下'<=>  True/False
            print("button pressed")
        else:
            print("button released")

    def whichbtn(self, btn):
        print("clicked button is " + btn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())


