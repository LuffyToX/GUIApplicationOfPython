# -*- coding: utf-8 -*-
# 动画 改变窗体大小


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.OrigHeight = 400
        self.ChangeHeight = 150
        self.setGeometry(QRect(800, 300, 500, self.OrigHeight))

        self.btn = QPushButton('收缩', self)
        self.btn.setGeometry(10, 10, 60, 35)
        self.machine = QStateMachine()
        self.btn.clicked.connect(self.change)

    """ 动画效果修改窗体大小 """
    def change(self):
        CurrentHeight = self.height()
        if self.OrigHeight == CurrentHeight:
            startHeight = self.OrigHeight
            endHeight = self.ChangeHeight
            self.btn.setText('展开')
        else:
            startHeight = self.ChangeHeight
            endHeight = self.OrigHeight
            self.btn.setText('收缩')

        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(800)
        self.animation.setStartValue(QRect(800, 300, 500, startHeight))
        self.animation.setEndValue(QRect(800, 300, 500, endHeight))
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
