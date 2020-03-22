# -*- coding: utf-8 -*-
# QTableWidget 表格中快速定位到指定行


import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtGui import QColor, QBrush


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.resize(600, 800)

        # 实例化 QTableWidget() 对象 30×4
        tableWidget = QTableWidget(30, 4)

        # 水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(tableWidget)
        self.setLayout(hbox)

        # 设置每个单元格的文本值
        for i in range(30):
            for j in range(4):
                itemContent = '(%d,%d)' % (i, j)
                tableWidget.setItem(i, j, QTableWidgetItem(itemContent))

        # 遍历表格查找对应的单元格
        text = "(10,1)"
        items = tableWidget.findItems(text, QtCore.Qt.MatchExactly)
        item = items[0]

        # 选中单元格
        # item.setSelected(True)

        # 设置单元格的背景颜色为红色
        item.setForeground(QBrush(QColor(255, 0, 0)))

        # 快速定位到指定行
        row = item.row()
        tableWidget.verticalScrollBar().setSliderPosition(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

