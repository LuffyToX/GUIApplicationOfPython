# -*- coding: utf-8 -*-
# QDateTimeEdit 的使用2


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QDateTime


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime(), self)
        self.btn = QPushButton("获得日期和时间")
        self.initUI()

        # 链接槽函数
        self.dateEdit.dateChanged.connect(self.onDateChanged)
        self.dateEdit.dateTimeChanged.connect(self.onDateTimeChanged)
        self.dateEdit.timeChanged.connect(self.onTimeChanged)
        self.btn.clicked.connect(self.onButtonClick)

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.resize(300, 90)

        self.dateEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")             # 设置日期格式
        self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365))   # 设置最小日期 => 当前日期 -365
        self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365))    # 设置最大日期 => 当前日期 +365
        self.dateEdit.setCalendarPopup(True)                              # 弹出日历

        # 垂直布局
        vlayout = QVBoxLayout()
        vlayout.addWidget(self.dateEdit)
        vlayout.addWidget(self.btn)
        self.setLayout(vlayout)

    @staticmethod
    def onDateChanged(date):
        # 日期发生改变时执行
        print(date)

    @staticmethod
    def onDateTimeChanged(dateTime):
        # 无论日期还是时间发生改变，都会执行
        print(dateTime)

    @staticmethod
    def onTimeChanged(time):
        # 时间发生改变时执行
        print(time)

    def onButtonClick(self):
        dateTime = self.dateEdit.dateTime()                # 日期和时间

        maxDateTime = self.dateEdit.maximumDateTime()      # 最大日期和时间
        minDateTime = self.dateEdit.minimumDateTime()      # 最小日期时间

        maxDate = self.dateEdit.maximumDate()              # 最大日期
        minDate = self.dateEdit.minimumDate()              # 最小日期

        maxTime = self.dateEdit.maximumTime()              # 最大时间
        minTime = self.dateEdit.minimumTime()              # 最小时间

        print('\n选择日期时间')
        print('dateTime=%s' % str(dateTime))
        print('maxDate=%s' % str(maxDate))
        print('maxDateTime=%s' % str(maxDateTime))
        print('maxTime=%s' % str(maxTime))
        print('minDate=%s' % str(minDate))
        print('minDateTime=%s' % str(minDateTime))
        print('minTime=%s' % str(minTime))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
