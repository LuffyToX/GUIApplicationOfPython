# -*- coding: utf-8 -*-
# 多窗口数据传递 信号与槽


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class DateDialog(QDialog):
    # 自定义带 str 参数的信号
    Signal_OneParameter = pyqtSignal(str)

    def __init__(self, parent=None):
        super(DateDialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        self.label = QLabel(self)
        self.label.setText('前者发射内置信号\n后者发射自定义信号')

        self.datetime_inner = QDateTimeEdit(self)
        self.datetime_inner.setCalendarPopup(True)
        self.datetime_inner.setDateTime(QDateTime.currentDateTime())

        self.datetime_emit = QDateTimeEdit(self)
        self.datetime_emit.setCalendarPopup(True)
        self.datetime_emit.setDateTime(QDateTime.currentDateTime())
        self.datetime_emit.dateTimeChanged.connect(self.emit_signal)

        # 使用两个按钮（ok、cancel）分别连接 accept()、reject() 槽函数
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

        # 垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.datetime_inner)
        vbox.addWidget(self.datetime_emit)
        vbox.addWidget(buttons)
        self.setLayout(vbox)

    def emit_signal(self):
        date_str = self.datetime_emit.dateTime().toString()
        # 发射自定义信号，槽函数在主窗口中
        self.Signal_OneParameter.emit(date_str)


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle("MainWindow")
        self.setGeometry(800, 300, 400, 90)

        self.open_btn = QPushButton('获取时间')
        self.lineEdit_inner = QLineEdit(self)
        self.lineEdit_emit = QLineEdit(self)
        self.open_btn.clicked.connect(self.openDialog)

        self.lineEdit_inner.setText('接收子窗口内置信号的时间')
        self.lineEdit_emit.setText('接收子窗口自定义信号的时间')

        # 栅格布局
        grid = QGridLayout()
        grid.addWidget(self.lineEdit_inner)
        grid.addWidget(self.lineEdit_emit)
        grid.addWidget(self.open_btn)
        self.setLayout(grid)

    def openDialog(self):
        dialog = DateDialog(self)

        # 连接子窗口的内置信号与主窗口的槽函数
        dialog.datetime_inner.dateTimeChanged.connect(self.deal_inner_slot)
        # 连接子窗口的自定义信号与主窗口的槽函数
        dialog.Signal_OneParameter.connect(self.deal_emit_slot)

        dialog.show()

    """ 子窗口内置信号的槽函数 """
    def deal_inner_slot(self, date):
        self.lineEdit_inner.setText(date.toString())

    """ 子窗口自定义信号的槽函数 """
    def deal_emit_slot(self, dateStr):
        self.lineEdit_emit.setText(dateStr)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
