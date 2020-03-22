# -*- coding: utf-8 -*-
# 为标签、按钮添加背景图片


import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.move(800, 300)

        # 标签 大小、样式
        label = QLabel()
        label.setStyleSheet("QLabel{border-image: url(./images/python.jpg);}")
        label.setFixedWidth(476)
        label.setFixedHeight(259)

        # 按钮 大小范围、样式
        btn = QPushButton(self)
        btn.setObjectName('btn')
        btn.setMaximumSize(48, 48)
        btn.setMinimumSize(48, 48)
        style = '''
                    #btn{
                        border-radius: 4px;
                        background-image: url('./images/add.png');
                        }
                    #btn:Pressed{
                        background-image: url('./images/addhover.png');
                        }
                '''
        btn.setStyleSheet(style)

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addStretch()
        vbox.addWidget(btn)
        self.setLayout(vbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

