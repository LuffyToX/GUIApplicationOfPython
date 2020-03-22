# -*- coding: utf-8 -*-
# QTableWidget 设置单元格文本颜色及字体设置


import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem)
from PyQt5.QtGui import QBrush, QColor, QFont


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.resize(430, 230)

        # 实例化 QTableWidget() 对象 4×3
        tableWidget = QTableWidget(4, 3)

        # 水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(tableWidget)
        self.setLayout(hbox)

        # 设置水平方向的表格头
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])

        # 创建单元格
        Item1 = QTableWidgetItem("张三")
        Item2 = QTableWidgetItem("男")
        Item3 = QTableWidgetItem("160")

        # 将单元格添加到表格中
        tableWidget.setItem(0, 0, Item1)
        tableWidget.setItem(0, 1, Item2)
        tableWidget.setItem(0, 2, Item3)

        # 设置单元格颜色
        Item1.setForeground(QBrush(QColor(255, 0, 0)))
        Item2.setForeground(QBrush(QColor(255, 0, 0)))
        Item3.setForeground(QBrush(QColor(255, 0, 0)))

        # 设置单元格字体并加粗
        Item1.setFont(QFont("Times", 12, QFont.Black))
        Item2.setFont(QFont("Times", 12, QFont.Black))
        Item3.setFont(QFont("Times", 12, QFont.Black))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
