# -*- coding: utf-8 -*-
# QTableWidget 改变单元格中显式的图片大小


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.resize(1000, 900)

        # 实例化 QTableWidget() 对象 4×3
        tableWidget = QTableWidget(4, 3)

        # 水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(tableWidget)
        self.setLayout(hbox)

        # 设置水平方向的表格头和垂直方向的表格头
        tableWidget.setHorizontalHeaderLabels(['Row1', 'Row2', 'Row3', 'Row4'])
        tableWidget.setVerticalHeaderLabels(['Col1', 'Col2', 'Col3'])

        # 将单元格设为禁止编辑的（默认情况下：单元格是可编辑的）
        tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        tableWidget.setIconSize(QSize(300, 200))          # 设置图片大小
        for i in range(3):
            tableWidget.setColumnWidth(i, 300)            # 让列宽和图片相同
        for i in range(5):
            tableWidget.setRowHeight(i, 200)              # 让行高和图片相同

        # 单元格
        for k in range(12):
            i = k // 3                                    # //cols == current row
            j = k % 3                                     # % cols == current col
            item = QTableWidgetItem()                     # 新建单元格
            item.setFlags(Qt.ItemIsEnabled)               # 用户点击单元格时，图片被选中
            item.setIcon(QIcon(r".\images\%d.ico" % k))   # 添加图片
            tableWidget.setItem(i, j, item)               # 将单元格添加到表格中


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
