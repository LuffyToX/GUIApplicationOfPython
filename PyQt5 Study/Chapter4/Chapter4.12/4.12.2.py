# -*- coding: utf-8 -*-
# QDateTimeEdit 的使用1


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QDateTime, QTime


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.resize(300, 90)

        # 设置默认显示的日期时间
        dateTimeEdit = QDateTimeEdit(self)
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime(), self)
        dateEdit = QDateTimeEdit(QDate.currentDate(), self)
        timeEdit = QDateTimeEdit(QTime.currentTime(), self)

        # 设置日期时间格式
        dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH-mm-ss")
        dateEdit.setDisplayFormat("yyyy.MM.dd")
        timeEdit.setDisplayFormat("HH:mm:ss")

        # 垂直布局
        vlayout = QVBoxLayout()
        vlayout.addWidget(dateTimeEdit)
        vlayout.addWidget(dateTimeEdit2)
        vlayout.addWidget(dateEdit)
        vlayout.addWidget(timeEdit)
        self.setLayout(vlayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
