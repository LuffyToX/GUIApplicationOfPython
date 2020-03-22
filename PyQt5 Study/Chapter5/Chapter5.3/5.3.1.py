# -*- coding: utf-8 -*-
# QTimer 的使用1


from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt5.QtCore import QTimer, QDateTime, Qt
import sys


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("Timer")
        self.setGeometry(800, 300, 300, 100)

        # 标签控件
        self.label = QLabel('显示当前时间')
        self.label.setAlignment(Qt.AlignCenter)

        # 按钮控件
        self.startBtn = QPushButton('开始')
        self.endBtn = QPushButton('结束')
        self.startBtn.clicked.connect(self.startTimer)
        self.endBtn.clicked.connect(self.endTimer)

        # 初始化一个定时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)

        # 栅格布局
        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0, 1, 2)
        layout.addWidget(self.startBtn, 1, 0)
        layout.addWidget(self.endBtn, 1, 1)
        self.setLayout(layout)

    def showTime(self):
        time = QDateTime.currentDateTime()                        # 获取系统现在的时间
        timeDisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")   # 设置系统时间显示格式
        self.label.setText(timeDisplay)                           # 在标签上显示时间

    def startTimer(self):
        # 设置计时间隔并启动
        self.timer.start(1000)
        self.startBtn.setEnabled(False)
        self.endBtn.setEnabled(True)

    def endTimer(self):
        # 停止定时器
        self.timer.stop()
        self.startBtn.setEnabled(True)
        self.endBtn.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
