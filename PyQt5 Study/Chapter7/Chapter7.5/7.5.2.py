# -*- coding: utf-8 -*-
# 多窗口数据传递 调用属性


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DateDialog(QDialog):
    def __init__(self, parent=None):
        super(DateDialog, self).__init__(parent)
        self.setWindowTitle("DateDialog")

        self.datetime = QDateTimeEdit(self)
        self.datetime.setCalendarPopup(True)
        self.datetime.setDateTime(QDateTime.currentDateTime())

        # 使用两个按钮（ok、cancel）分别连接 accept()、reject() 槽函数
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        # 垂直布局
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.datetime)
        vbox.addWidget(buttons)

    """ 从对话框中获取当前日期和时间 """
    def dateTime(self):
        return self.datetime.dateTime()

    """ 静态方法创建对话框并返回 (date, time, accepted) """
    @staticmethod
    def getDateTime(parent=None):
        # 实例化 QDataDialog 对象
        dialog = DateDialog(parent)
        date = dialog.dateTime()

        # 判断用户点击 'Ok'/'Cancel'
        result = dialog.exec_()
        return date.date(), date.time(), result == QDialog.Accepted


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 500, 300)

        self.lineEdit = QLineEdit(self)
        self.button1 = QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.onButton1Click)

        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.onButton2Click)

        # 栅格布局
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.lineEdit)
        gridLayout.addWidget(self.button1)
        gridLayout.addWidget(self.button2)
        self.setLayout(gridLayout)

    """ 直接在主窗口中实例化对话框 """
    def onButton1Click(self):
        dialog = DateDialog(self)
        result = dialog.exec_()
        date = dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        print('\n日期对话框的返回值')
        print('date=%s' % str(date.date()))
        print('time=%s' % str(date.time()))
        print('result=%s' % result)
        dialog.destroy()

    """ 在主窗口中调用子窗口的静态函数 """
    def onButton2Click(self):
        date, time, result = DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        print('\n日期对话框的返回值')
        print('date=%s' % str(date))
        print('time=%s' % str(time))
        print('result=%s' % result)
        if result == QDialog.Accepted:
            print('点击确认按钮')
        else:
            print('点击取消按钮')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
