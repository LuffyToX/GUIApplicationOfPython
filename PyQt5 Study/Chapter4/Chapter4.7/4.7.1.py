# -*- coding: utf-8 -*-
# QSpinBox 的使用


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Dialog(QWidget):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")
        self.resize(300, 100)

        self.qLable = QLabel("current value:")                # 新建标签对象用于显示当前值
        self.qLable.setAlignment(Qt.AlignCenter)              # 文本居中显示

        self.qSpinBox = QSpinBox()                            # 新建计数器对象
        self.qSpinBox.valueChanged.connect(self.valuechange)

        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.qLable)
        layout.addWidget(self.qSpinBox)
        self.setLayout(layout)

    def valuechange(self):
        # 将标签文本设为计数器的当前值
        self.qLable.setText("current value:" + str(self.qSpinBox.value()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
