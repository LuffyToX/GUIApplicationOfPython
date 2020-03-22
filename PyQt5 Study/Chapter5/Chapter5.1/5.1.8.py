# -*- coding: utf-8 -*-
# QTableWidget 单元格排序、对齐


import sys
from PyQt5.QtWidgets import (QWidget, QTableWidget, QHBoxLayout, QApplication, QTableWidgetItem)
from PyQt5.QtCore import Qt


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
        Item11 = QTableWidgetItem("张三")
        Item12 = QTableWidgetItem("男")
        Item13 = QTableWidgetItem("160")

        Item21 = QTableWidgetItem("李四")
        Item22 = QTableWidgetItem("女")
        Item23 = QTableWidgetItem("155")

        Item31 = QTableWidgetItem("王五")
        Item32 = QTableWidgetItem("男")
        Item33 = QTableWidgetItem("170")

        # 将单元格添加到表格中
        tableWidget.setItem(0, 0, Item11)
        tableWidget.setItem(0, 1, Item12)
        tableWidget.setItem(0, 2, Item13)

        tableWidget.setItem(1, 0, Item21)
        tableWidget.setItem(1, 1, Item22)
        tableWidget.setItem(1, 2, Item23)

        tableWidget.setItem(2, 0, Item31)
        tableWidget.setItem(2, 1, Item32)
        tableWidget.setItem(2, 2, Item33)

        # Qt.AscendingOrder  升序
        # Qt.DescendingOrder 降序
        # 第一个参数指定列
        tableWidget.sortItems(2, Qt.DescendingOrder)

        # 将单元格居中对齐
        Item11.setTextAlignment(Qt.AlignCenter)
        Item12.setTextAlignment(Qt.AlignCenter)
        Item13.setTextAlignment(Qt.AlignCenter)

        Item21.setTextAlignment(Qt.AlignCenter)
        Item22.setTextAlignment(Qt.AlignCenter)
        Item23.setTextAlignment(Qt.AlignCenter)

        Item31.setTextAlignment(Qt.AlignCenter)
        Item32.setTextAlignment(Qt.AlignCenter)
        Item33.setTextAlignment(Qt.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
