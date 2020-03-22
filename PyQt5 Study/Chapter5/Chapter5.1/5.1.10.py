# -*- coding: utf-8 -*-
# QTableWidget 设置单元格大小


import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem)
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.resize(600, 400)

        # 实例化 QTableWidget() 对象 4×3
        tableWidget = QTableWidget(4, 3)

        # 水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(tableWidget)
        self.setLayout(hbox)

        # 设置水平方向的表格头
        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(kg)'])

        # 设置单元格大小
        # setRowHeight(row, height)       将第 row 行单元格设置成 height 宽度
        # setColumnWidth(col, width)      将第 col 列单元格设置成 width  高度
        tableWidget.setRowHeight(0, 120)
        tableWidget.setColumnWidth(0, 150)

        # 创建单元格
        newItem1 = QTableWidgetItem("张三")
        newItem2 = QTableWidgetItem("男")
        newItem3 = QTableWidgetItem("160")

        # 将单元格添加到表格中
        tableWidget.setItem(0, 0, newItem1)
        tableWidget.setItem(0, 1, newItem2)
        tableWidget.setItem(0, 2, newItem3)

        # 将单元格居中对齐
        newItem1.setTextAlignment(Qt.AlignCenter)
        newItem2.setTextAlignment(Qt.AlignCenter)
        newItem3.setTextAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
