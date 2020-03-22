# -*- coding: utf-8 -*-
# QSlider 的使用


import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Dialog(QWidget):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")
        self.resize(300, 100)

        self.qLabel = QLabel("Hello PyQt5")                    # 新建标签对象
        self.qLabel.setAlignment(Qt.AlignCenter)               # 文本居中显示

        self.qSlider = QSlider(Qt.Horizontal)                  # 新建水平方向的滑动条
        self.qSlider.setMinimum(10)                            # 设置滑动条最小值
        self.qSlider.setMaximum(50)                            # 设置滑动条最大值
        self.qSlider.setSingleStep(3)                          # 设置滑动条步长
        self.qSlider.setValue(20)                              # 设置滑动条当前值
        self.qSlider.setTickPosition(QSlider.TicksBelow)       # 设置刻度位置
        self.qSlider.setTickInterval(5)                        # 设置刻度间隔
        self.qSlider.valueChanged.connect(self.valuechange)

        # 垂直布局
        layout = QVBoxLayout()
        layout.addWidget(self.qLabel)
        layout.addWidget(self.qSlider)
        self.setLayout(layout)

    def valuechange(self):
        print('current slider value=%s' % self.qSlider.value())

        # 设置标签字体，并将其大小设为滑动条所示大小
        size = self.qSlider.value()
        self.qLabel.setFont(QFont("Arial", size))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Dialog()
    win.show()
    sys.exit(app.exec_())
