# -*- coding: utf-8 -*-
# QCalendar 的使用


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.cal = QCalendarWidget(self)                    # 新建 QCalendarWidget() 对象
        self.lbl = QLabel(self)                             # 新建 QLabel() 对象
        self.initUI()                                       # 初始化界面

        # 从窗口组件选定一个日期，就会发射一个 QDate 信号
        self.cal.clicked[QDate].connect(self.showDate)

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 400, 350)

        self.cal.setMinimumDate(QDate(1980, 1, 1))          # 设置最小日期
        self.cal.setMaximumDate(QDate(3000, 1, 1))          # 设置最大日期
        self.cal.setGridVisible(True)                       # 设置日历控件显示网格
        self.cal.move(30, 20)

        date = self.cal.selectedDate()                      # 当前选定的日期
        self.lbl.setText(date.toString("yyyy-MM-dd dddd"))  # 将当前日期转换成指定格式
        self.lbl.move(30, 300)

    def showDate(self, date):
        self.lbl.setText(date.toString("yyyy-MM-dd dddd"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
